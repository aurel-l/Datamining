_occurrences = {
    'A': 0.078,
    'C': 0.019,
    'D': 0.053,
    'E': 0.063,
    'F': 0.039,
    'G': 0.072,
    'H': 0.023,
    'I': 0.053,
    'K': 0.059,
    'L': 0.091,
    'M': 0.023,
    'N': 0.043,
    'O': 0.0,
    'P': 0.052,
    'Q': 0.042,
    'R': 0.051,
    'S': 0.068,
    'T': 0.059,
    'U': 0.0,
    'V': 0.066,
    'W': 0.014,
    'Y': 0.032
}
_placeholders = {
    'B': {
        'R': _occurrences['R'] / (_occurrences['R'] + _occurrences['D']),
        'D': _occurrences['D'] / (_occurrences['R'] + _occurrences['D'])
    },
    'Z': {
        'Q': _occurrences['Q'] / (_occurrences['Q'] + _occurrences['E']),
        'E': _occurrences['E'] / (_occurrences['Q'] + _occurrences['E'])
    },
    'J': {
        'L': _occurrences['L'] / (_occurrences['L'] + _occurrences['I']),
        'I': _occurrences['I'] / (_occurrences['L'] + _occurrences['I'])
    },
    'X': _occurrences
}
_alphabet = list(_occurrences.keys())
_extended = list(_placeholders.keys())

def value(sequence):
    """
    Computes the proportion of every aminoacid in a sequence
    :param sequence: sequence to be analyzed
    :type values: Bio.SeqRecord.SeqRecord
    :returns dict containing, for every aminoacid, its proportion in the sequence
    :rtype dict
    """
    results = {aa: 0 for aa in _occurrences}
    for letter in sequence.seq:
        if letter in _alphabet:
            results[letter] += 1
        elif letter in _extended:
            for (letter, value) in _placeholders[letter].items():
                results[letter] += value
    length = len(sequence)
    return {key: value / length for (key, value) in results.items()}

