#!/usr/bin/python3

from Bio.SeqIO import parse as _parse
import numpy as _np
from sys import argv as _argv
import os as _os
from importlib import import_module as _import_module

from lib.progress import Progress as _Progress
from lib.worker import Worker as _Worker


def _worker_fun(length, feature, pipe):
    module = _import_module('lib.features.{}'.format(feature))

    mm = _np.memmap(
        'warehouse{}{}.dat'.format(_os.path.sep, feature),
        dtype=_np.float64,
        mode='w+',
        shape=(length, module.size_values)
    )
    for i in range(length):
        mm[i] = module.value(pipe.recv())
    pipe.close()


def main(file_name, features=[], n_proteins=None, log=True):
    if not n_proteins:
        # Tries to get the number of proteins in the file if not provided
        try:
            # Quickest way, with unix command 'wc'
            n_proteins = int(_os.popen(
                'grep "</entry" {} | wc -l'.format(file_name)
            ).readline())
            if not n_proteins:
                raise ValueError
        except:
            # Slowest way, parsing the file with BioPython
            n_proteins = 0
            g = _parse(open(file_name, encoding='utf-8'), 'uniprot-xml')
            for _ in g:
                n_proteins += 1

    try:
        # tries to create a directory for the data warehouse
        _os.makedirs('warehouse')
    except OSError:
        # already exists
        _os.system('rm warehouse/*.dat 2> /dev/null')

    workers = [_Worker(
        target=_worker_fun,
        args=[n_proteins, feature]
    ) for feature in features]

    if log:
        print('extracting data from {} proteins'.format(n_proteins))
        progress = _Progress(60, n_proteins)

    for (seq, i) in zip(
        _parse(open(file_name, encoding='utf-8'), 'uniprot-xml'),
        range(n_proteins)
    ):
        for w in workers:
            w.feed(seq)
        if log:
            progress.increment()

    # clean up processes and pipes
    for w in workers:
        w.join()

    if log:
        progress.finish()

    return {
        'n_proteins': n_proteins,
        'features': features
    }

if __name__ == '__main__':
    try:
        n_proteins = int(_argv[2])
    except:
        n_proteins = None
    main(_argv[1], ['aminoacids', 'structure', 'length'], n_proteins, True)
