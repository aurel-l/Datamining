#!/usr/bin/python
# -*- coding: utf-8 -*-

# Selection des champs d'interet

from Bio import SeqIO
import sys
import time


# Creation et eciture du nouveau fichier
def writeInFile(path,texte1,texte2,texte3):
	newFile = open(path, "a") # fichier en ajout
	newFile.writelines(texte1)
	newFile.writelines(texte2)
	newFile.writelines(texte3)
	newFile.close()

# Lecture du fichier
def readFile(path):
	fic = open(path,"r")
	line = fic.readline()
	line = line.strip()
	print line
	fic.close()



begin = time.time()

nSeq = 0

sequences = SeqIO.parse(sys.stdin, 'uniprot-xml')

# Pour sauvegarder les sequences au format Fasta si nécessaire 
# comme SeqIO ne permet pas d'ecrire au format uniprot

#output_handle = open("Sequence.fasta","w")
#SeqIO.write(sequences, output_handle, "fasta")



for index, record in enumerate(sequences):
	nSeq += 1
	

	chain="index %i, name = %s, ID = %s, annotations = %s, length %i,  with %i features"\
		% (index, record.name, record.id, record.annotations, len(record.seq), len(record.features))
	

	name ="index %i, name = %s, ID =%s"\
		% (index, record.name, record.id)

	taille ="length %i"\
		% (len(record.seq))

	features ="with %i features"\
		% (len(record.features))

	

	fullName ="<",name," /> \n"
	fullTaille="\t <",taille," />\n"
	fullFeatures="\t\t <",features," />\n"
	#FullTaille ="\t<",taille," />\n"


	writeInFile("NewFile.xml",fullName,fullTaille,fullFeatures)

	sys.stdout.write("\b" * 80
                     + 'analyzed {} sequences in {:.3f} seconds'.format(nSeq,
                     round(time.time() - begin, 3)))

sys.stdout.write('\n')













