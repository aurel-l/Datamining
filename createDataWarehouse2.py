#!/usr/bin/python3

from Bio import SeqIO
import numpy as np
from sys import argv
import os
from multiprocessing import Pipe, Process
from standardization import aminoacids, length, structure

fileHandler = open(argv[1], encoding = 'utf-8')
try:
    nProteins = int(argv[2])
except:
    nProteins = 0
    for _ in SeqIO.parse(fileHandler, 'uniprot-xml'):
        nProteins += 1

try:
    # tries to create a directory for the data warehouse
    os.makedirs('warehouse')
except OSError:
    # already exists or error with rights
    pass

workers = [aminoacids.worker, length.worker, structure.worker]
pipes = [Pipe() for _ in workers]
processes = [Process(target = w, args = (p[1], nProteins)) for (w, p) in zip(workers, pipes)]

for p in processes:
    p.start()

for (seq, i) in zip(SeqIO.parse(open('data.xml'), 'uniprot-xml'), range(nProteins)):
    for p in pipes:
        p[0].send(seq)

for (process, pipe) in zip(processes, pipes):
    pipe[0].send(False)
    process.join()
    pipe[1].close()


