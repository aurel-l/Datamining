import numpy as _np
from os import path as _path

_alphabet = 'ACDEFGHIKLMNOPQRSTUVWY'
sizeValues = len(_alphabet)# 22
_occurrences = _np.array([
    7.8, 1.9, 5.3, 6.3, 3.9, 7.2, 2.3, 5.3, 5.9, 9.1, 2.3,
    4.3, 0, 5.2, 4.2, 5.1, 6.8, 5.9, 0, 6.6, 1.4, 3.2
]) / 100

def _fillPlaceHolder(*aminoacids):
    """
    Computes the aminoacid occurrences corresponding to a placeholder letter
    :param aminoacids: aminoacids that the placeholder replaces
    :type values: tuple
    :returns array with new aminoacid occurrences
    :rtype numpy.ndarray
    """
    indices = [_alphabet.index(aa) for aa in aminoacids]
    values = [_occurrences[i] for i in indices]
    total = _np.sum(values)
    array = _np.zeros(sizeValues)
    for (i, v) in zip(indices, values):
        array[i] = v / total
    return array

_placeholders = {
    'B': _fillPlaceHolder('R', 'D'),
    'Z': _fillPlaceHolder('Q', 'E'),
    'J': _fillPlaceHolder('L', 'I'),
    'X': _occurrences
}

def value(sequence):
    """
    Computes the proportion of every aminoacid in a sequence
    :param sequence: sequence to be analyzed
    :type values: Bio.SeqRecord.SeqRecord
    :returns array containing, for every aminoacid, its proportion in the sequence
    :rtype numpy.ndarray
    """
    results = _np.zeros(sizeValues)
    for letter in sequence.seq:
        try:
            index = _alphabet.index(letter)
            results[index] += 1
        except ValueError:
            try:
                results += _placeholders[letter]
            except KeyError:
                pass
    return results / len(sequence)

def worker(pipe, length):
    mm = _np.memmap(_path.join('warehouse', 'aminoacids.dat'), dtype='float32', mode='w+', shape=(length, sizeValues))
    i = 0
    seq = pipe.recv()
    while seq:
        mm[i] = value(seq)
        i += 1
        seq = pipe.recv()

