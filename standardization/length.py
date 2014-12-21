import numpy as _np
from os import path as _path

sizeValues = 1

def value(sequence):
    """
    Computes the length of the input sequence
    :param values: input sequence
    :type values: Bio.SeqRecord.SeqRecord
    :returns length of the sequence
    :rtype int
    """
    return len(sequence)

def worker(pipe, length):
    mm = _np.memmap(_path.join('warehouse', 'lengths.dat'), dtype='float32', mode='w+', shape=(length, sizeValues))
    i = 0
    seq = pipe.recv()
    while seq:
        mm[i] = value(seq)
        i += 1
        seq = pipe.recv()

