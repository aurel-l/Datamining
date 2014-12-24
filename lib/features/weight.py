from Bio.SeqUtils import molecular_weight

size_values = 1


def value(sequence):
    """
    Calcul the weight of the input sequence
    :param values: input sequence
    :type values: Bio.SeqRecord.SeqRecord
    :returns weight of the sequence
    :rtype array[float]
    """
    ### BUG
    # breaks when 'X' in sequence
    return [molecular_weight(sequence.seq)]
