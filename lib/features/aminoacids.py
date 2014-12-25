import numpy as _np

_alphabet = 'ACDEFGHIKLMNOPQRSTUVWY'
size_values = len(_alphabet)
_occurrences = _np.array([
    7.8, 1.9, 5.3, 6.3, 3.9, 7.2, 2.3, 5.3, 5.9, 9.1, 2.3,
    4.3, 0, 5.2, 4.2, 5.1, 6.8, 5.9, 0, 6.6, 1.4, 3.2
], dtype=_np.float64) / 100


def _fill_placeholder(aminoacids):
    """
    Computes the aminoacid occurrences corresponding to a placeholder letter
    :param aminoacids: aminoacids that the placeholder replaces
    :type values: string
    :returns array with new aminoacid occurrences
    :rtype numpy.ndarray
    """
    indices = [_alphabet.index(aa) for aa in aminoacids]
    values = [_occurrences[i] for i in indices]
    total = _np.sum(values)
    array = _np.zeros(size_values, dtype=_np.float64)
    for (i, v) in zip(indices, values):
        array[i] = v / total
    return array

_placeholders = {
    'B': _fill_placeholder('DN'),
    'Z': _fill_placeholder('EQ'),
    'J': _fill_placeholder('IL'),
    'X': _occurrences
}


def value(sequence):
    """
    Computes the proportion of every aminoacid in a sequence
    :param sequence: sequence to be analyzed
    :type values: Bio.SeqRecord.SeqRecord
    :returns array containing, for every aa, its proportion in the sequence
    :rtype numpy.ndarray[numpy.float64]
    """
    results = _np.zeros(size_values, dtype=_np.float64)
    for letter in sequence.seq:
        try:
            index = _alphabet.index(letter)
            results[index] += 1
        except ValueError:
            try:
                results += _placeholders[letter]
            except KeyError:
                results += _placeholders['X']
    return results / len(sequence)
