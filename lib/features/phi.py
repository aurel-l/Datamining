size_values = 1
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
    'O': 0.000,
    'P': 0.052,
    'Q': 0.042,
    'R': 0.051,
    'S': 0.068,
    'T': 0.059,
    'U': 0.000,
    'V': 0.066,
    'W': 0.014,
    'Y': 0.032,
}
_dict_phi = {
    'A':  6.00,
    'C':  5.07,
    'D':  2.77,
    'E':  3.22,
    'F':  5.48,
    'G':  5.97,
    'H':  7.59,
    'I':  6.02,
    'K':  9.74,
    'L':  5.98,
    'M':  5.74,
    'N':  5.41,
    'O':  0,  # unknown, redefined later
    'P':  6.30,
    'Q':  5.95,
    'R': 10.76,
    'S':  5.68,
    'T':  6.60,
    'U':  5.47,
    'V':  5.96,
    'W':  5.89,
    'Y':  5.66
}


def _fill_placeholder(aminoacids):
    sum_values_weighted = 0.0
    sum_weights = 0.0
    for letter in aminoacids:
        weight = _occurrences[letter]
        sum_values_weighted += _dict_phi[letter] * weight
        sum_weights += weight
    return sum_values_weighted / sum_weights

_dict_phi['B'] = _fill_placeholder('DN')
_dict_phi['Z'] = _fill_placeholder('EQ')
_dict_phi['J'] = _fill_placeholder('IL')
_dict_phi['X'] = _fill_placeholder('ACDEFGHIKLMNOPQRSTUVWY')
_dict_phi['O'] = _dict_phi['X']


def value(sequence):
    """
    Run a sequence and compare to all the amino acids stored on a dictionnary
    Then, calcul the average Pi of this sequence
    :param values: a sequence, here it is oneExempleSequenceTest
    :type values: str
    :returns the sequence average pi
    :rtype array[float]
    """
    total_phi = 0.0
    for letter in sequence.seq:
        try:
            value = _dict_phi[letter]
        except KeyError:
            value = _dict_phi['X']
        total_phi += value
    return [total_phi / len(sequence)]
