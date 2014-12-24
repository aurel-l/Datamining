from Bio.SeqUtils import *
from ProtParam import ProteinAnalysis as PA 




def calculW(sequence):
	"""
    Calcul the weight of the input sequence
    (other version)
    :param values: input sequence
    :type values: Bio.SeqRecord.SeqRecord
    :returns weight of the sequence
    :rtype int
    """

	X = PA(str(sequence))
	return X.molecular_weight()



def calcul_weight(sequence):
	"""
    Calcul the weight of the input sequence
    :param values: input sequence
    :type values: Bio.SeqRecord.SeqRecord
    :returns weight of the sequence
    :rtype int
    """

	for i in range (0,len(sequence)):
		if (sequence[i] == 'B' ):

			# B --> R = 5.1 ou D = 5.3
			"""
			else if(sequence[i] == 'Z'):
			# Z --> Q = 4.2 ou E = 6.3
			
			else if(sequence[i] == 'J'):
			# J --> L = 9.1 ou I = 5.3

			else:
			"""

	return molecular_weight(sequence,"protein")






