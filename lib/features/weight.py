# -*- coding: utf-8 -*-
from Bio.SeqUtils import molecular_weight
import length

size_values = 1

# 1) Remplacer dans IUPACData.py les 2 dictionnaires suivants (Bio-->Data)
#     --> ca gere le pb de l'acide amine X non reconnu
# 2) Ensuite dans le fichier IUPAC.py (Bio-->Alphabet )j'ai tente de changer protein_letters en extended_protein_letters
# pour gérer tous les noms de proteines mais il semble y avoir autre chose a faire (pb a partir de 'B')

protein_weights = {
    "A": 89.0932,
    "B": 132.6103, # add
    "C": 121.1582,
    "D": 133.1027,
    "E": 147.1293,
    "F": 165.1891,
    "G": 75.0666,
    "H": 155.1546,
    "I": 131.1729,
    "J": 131.1729, # add
    "K": 146.1876,
    "L": 131.1729,
    "M": 149.2113,
    "N": 132.1179,
    "O": 255.3134, 
    "P": 115.1305,
    "Q": 146.1445,
    "R": 174.201,
    "S": 105.0926,
    "T": 119.1192,
    "U": 168.0532,
    "V": 117.1463,
    "W": 204.2252,
    "Y": 181.1885,
    "X": 143.6986, # add 
    "Z": 146.6369, # add
    }

monoisotopic_protein_weights = {
    "A": 89.047678,
    "B": 132.545500, # add
    "C": 121.019749,
    "D": 133.037508,
    "E": 147.053158,
    "F": 165.078979,
    "G": 75.032028,
    "H": 155.069477,
    "I": 131.094629,
    "J": 131.094629, # add
    "K": 146.105528,
    "L": 131.094629,
    "M": 149.051049,
    "N": 132.053492,
    "O": 255.158292,
    "P": 115.063329,
    "Q": 146.069142,
    "R": 174.111676,
    "S": 105.042593,
    "T": 119.058243,
    "U": 168.964203,
    "V": 117.078979,
    "W": 204.089878,
    "Y": 181.073893,
    "X": 143.656733, # add
    "Z": 146.561150, # add
    }


def value(sequence):
	"""
    Calcul the weight of the input sequence
    :param values: input sequence
    :type values: Bio.SeqRecord.SeqRecord
    :returns weight of the sequence
    :rtype array[float]
    """

    #Always bug for unknown aminoacids :(

	return [molecular_weight(sequence,"protein")/length.value(sequence)]






