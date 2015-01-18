import numpy as _np

_structures = ['helix', 'strand', 'turn']
size_values = len(_structures)


def value(sequence):
    """
    Computes the average presence of given structures in a sequence by aa
    :param sequence: sequence to be analyzed
    :type sequence: Bio.SeqRecord.SeqRecord
    :returns: array containing, for every structure, its presence in the seq
    :rtype: numpy.ndarray[numpy.float64]
    """
    results = _np.zeros(size_values, dtype=_np.float64)
    for f in sequence.features:
        try:
            results[_structures.index(f.type)] += len(f)
        except ValueError:
            pass
    return results / len(sequence)
