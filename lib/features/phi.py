import numpy as np

size_values = 1

DictPhi = {
	'A' : 6.0 ,
	'G' : 6.0 ,
	'V' : 6.0 ,
	'L' : 6.0 ,
	'I' : 6.1 ,
	'P' : 6.3 ,
	'F' : 5.5 ,
	'W' : 5.9 ,
	'N' : 5.4 ,
	'Q' : 5.7 ,
	'Y' : 5.7 , 
	'S' : 5.7 ,
	'T' : 6.5 ,
	'C' : 5.0 ,
	'M' : 5.8 ,
	'K' : 9.8 ,
	'R' : 10.8 ,
	'H' : 7.6 ,
	'D' : 3.0 ,
	'E' : 3.2 ,
	'X' : 6.1 ,
	'B' : 4.2 ,
	'Z' : 4.45 ,
	'J' : 6.05
}

_PositivCharge = []
_NegativCharge = []



def piMoyen(DictPhi):
	"""
    Calculating the average pi of the dictionnary of 21 aa
    to calculate X pi if it is only an average (ignoring the proportion)
    :param values: values to be put inside the csv line
    :type values: dictionary data type
    :returns the average pi of the 21 aa only
    :rtype decimal
    """
	Liste = []
	for cle, values in DictPhi.items():
		Liste.append(values)
	piM = np.mean(Liste)

	return piM



def value(seq):
	"""
    Run a sequence and compare to all the amino acids stored on a dictionnary 
    Then, calcul the average Pi of this sequence
    :param values: a sequence, here it is oneExempleSequenceTest
    :type values: str
    :returns the sequence average pi 
    :rtype array[float]
    """
	ListSeq = []
	ListValues = []
	# add the aa on the String on a List
	for i in range(0,len(seq)):
		ListSeq.append(seq[i])
	
	# run this new List containing the sequence aa
	for j in range(0,len(ListSeq)):
		# run the stored dictionary pi values 
		for cle, values in DictPhi.items():
			# when the aa equals the aa stored,
			# overwriting the pi on the List
			if (ListSeq[j] == cle):
				if(ListSeq[j] != cle):
					print "Cet aa n'est pas dans le stock ",ListSeq[j]
				#ListSeq[j] = values
				ListValues.append(values)

	# pi average of this sequence
	piMeanSeq = np.mean(ListValues)

	return [piMeanSeq]


def triCharge(sequence):
	"""
    Sort in two groups the sequences : Positiv or negativ
    :param values: a sequence, here it is oneExempleSequenceTest
    :type values: str
    """
	if(value(sequence) > 7):
		_PositivCharge.append(sequence)
		print 'This sequence add on the positiv group.'
	else:
		_NegativCharge.append(sequence)
		print 'This sequence add on the negativ group.'







