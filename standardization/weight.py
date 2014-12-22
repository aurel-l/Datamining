from Bio.SeqUtils import *



def calcul_weight(sequence):
	"""
    Calcul the weight of the input sequence
    :param values: input sequence
    :type values: Bio.SeqRecord.SeqRecord
    :returns weight of the sequence
    :rtype int
    """

	return molecular_weight(sequence)






