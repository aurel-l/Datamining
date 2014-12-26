# -*- coding: utf-8 -*-

size_values = 1

# sequence.next()
def value(sequence):
    """
    Calcul the weight of the input sequence
    :param values: input sequence
    :type values: Bio.SeqRecord.SeqRecord
    :returns weight of the sequence
    :rtype array[int]
    """

    mass = sequence.annotations["sequence_mass"]
    return [mass/len(sequence.seq)]
    
    






