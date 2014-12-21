import numpy as _np
from os import path as _path

_structures = ['helix', 'strand', 'turn']
sizeValues = len(_structures)

def value(sequence):
    results = _np.zeros(sizeValues)
    for f in sequence.features:
        try:
            results[_structures.index(f.type)] += len(f)
        except ValueError:
            pass
    return results / len(sequence)

def worker(pipe, length):
    mm = _np.memmap(_path.join('warehouse', 'structures.dat'), dtype='float32', mode='w+', shape=(length, sizeValues))
    i = 0
    seq = pipe.recv()
    while seq:
        mm[i] = value(seq)
        i += 1
        seq = pipe.recv()

