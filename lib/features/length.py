size_values = 1


def value(sequence):
    """
    Computes the length of the input sequence
    :param values: input sequence
    :type values: Bio.SeqRecord.SeqRecord
    :returns array containing one value, the length of the sequence
    :rtype array[int]
    """
    return [len(sequence)]
