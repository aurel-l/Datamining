size_values = 1


def value(sequence):
    """
    Computes the mean weight of the input sequence's aminoacids
    :param values: input sequence
    :type values: Bio.SeqRecord.SeqRecord
    :returns array with one value, the relative weight of the sequence's aa
    :rtype array[int]
    """
    return [sequence.annotations["sequence_mass"] / len(sequence)]
