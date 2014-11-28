#!/usr/bin/python3
# -*- coding: utf-8 -*-

# If the Phi is greather than the pH, the molecule will have a positive charge
# pI is the pH value when the net charge of the molecule is null
# 3 cat are defined : 
#    - "acide" : Asp, Glu
#    - "basic" : Lys, Arg, His
#    - "neutre" : the others

import numpy as np
from Bio import SeqIO
import sys
import time

begin = time.time()

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
}


def affichage(DictPhi):
	"""
    Display a dictionary
    :param values: dictionary containing all de pi values for each amino acids
    :type values: dictionary data type
    """
	for cle, values in DictPhi.items():
		print "L'acide amine",cle," a comme Phi ",values


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


# An exemplary sequence to be treated
oneExempleSequenceTest = 'MAVVLPAVVEELLSEMAAAVQESARIPDEYLLSLKFLFGSSATQALDLVDRQSITLISSPSGRRVYQVLGSSSKTYTCLASCHYCSCPAFAFSVLRKSDSILCKHLLAVYLSQVMRTCQQLSVSDKQLTDILLMEKKQEA'
otherExample = "MSGPVPSRARVYTDVNTHRPREYWDYESHVVEWGNQDDYQLVRKLGRGKYSEVFEAINITNNEKVVVKILKPVKKKKIKREIKILENLRGGPNIITLADIVKDPVSRTPALVFEHVNNTDFKQLYQTLTDYDIRFYMYEILKALDYCHSMGIMHRDVKPHNVMIDHEHRKLRLIDWGLAEFYHPGQEYNVRVASRYFKGPELLVDYQMYDYSLDMWSLGCMLASMIFRKEPFFHGHDNYDQLVRIAKVLGTEDLYDYIDKYNIELDPRFNDILGRHSRKRWERFVHSENQHLVSPEALDFLDKLLRYDHQSRLTAREAMEHPYFYPVVKEQSQPCADNAVLSSGLTAAR"
# Code a utiliser dans un fichier en amont pour récupérer les sequences 
# de toutes les proteines
"""
sequences = SeqIO.parse(sys.stdin, 'uniprot-xml')

nSeq =0
DictSequences ={}


for index, record in enumerate(sequences):
	nSeq += 1
	#print "index %i, sequence = %s \n"\
	#	% (index, record.seq)


	DictSequences ={index, record.seq}


	sys.stdout.write("\b" * 80
                     + 'analyzed {} sequences in {:.3f} seconds'.format(nSeq,
                     round(time.time() - begin, 3)))
	
"""


# fonction permettant de parcourir une sequence et de la comparer
# avec le Stock des valeurs de Pi pour calculer son Pi moyen
# entree : String de la sequence
# sortie : doit retourner un Pi moyen
def traitementSequence(seq):
	"""
    Run a sequence and compare to all the amino acids stored on a dictionnary 
    Then, calcul the average Pi of this sequence
    :param values: a sequence, here it is oneExempleSequenceTest
    :type values: str
    :returns the sequence average pi 
    :rtype decimal
    """
	ListSeq = []
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
				ListSeq[j] = values

	# pi average of this sequence
	piMeanSeq = np.mean(ListSeq)

	return piMeanSeq


# MAIN

#affichage(DictPhi)
#print "Pi moyen est ",piMoyen(DictPhi)

print "Le Pi moyen de la sequence",oneExempleSequenceTest,"\nest de : ",traitementSequence(oneExempleSequenceTest)




