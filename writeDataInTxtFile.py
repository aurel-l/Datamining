#!/usr/bin/python
# -*- coding: utf-8 -*-

# Selection des champs d'interet

from Bio import SeqIO
import sys
import time


# Creation et eciture du nouveau fichier
def writeInFile(path,texte):
	newFile = open(path, "a") # fichier en ajout
	newFile.writelines(texte)
	
	newFile.close()

# Lecture du fichier
def readFile(path):
	fic = open(path,"r")
	line = fic.readline()
	line = line.strip()
	print line
	fic.close()



begin = time.time()

nSeq = 0

sequences = SeqIO.parse(sys.stdin, 'uniprot-xml')


for index, record in enumerate(sequences):
	nSeq += 1
	

	chain="index %i, name = %s, ID = %s, description = %s, length %i,  with %i features\n"\
		% (index, record.name, record.id, record.description, len(record.seq), len(record.features))
	

	


	writeInFile("HumanProtein.txt",chain)

	sys.stdout.write("\b" * 80
                     + 'analyzed {} sequences in {:.3f} seconds'.format(nSeq,
                     round(time.time() - begin, 3)))

sys.stdout.write('\n')













