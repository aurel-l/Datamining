#!/usr/bin/python3

from Bio import SeqIO
import sys
import os


def seqGenerator():
    """
    Creates a sequence generator from the first argument
    by default, or from the standard input
    :returns generator of sequences from the data source
    :rtype generator
    """
    try:
        return SeqIO.parse(
            open(sys.argv[1], encoding='utf-8'),
            'uniprot-xml'
        )
    except:
        print('Taking standard input as data source')
        return SeqIO.parse(sys.stdin, 'uniprot-xml')


def csvLine(*values):
    """
    Creates a tab-separated csv-formatted string with the provided values
    :param values: values to be put inside the csv line
    :type values: tuple
    :returns formatted string
    :rtype str
    """
    return (('{}\t') * (len(values) - 1) + '{}\n').format(*values)


def infoForm(s):
    """
    Formats a string in csv with wanted data from a sequence
    :param s: input sequence
    :type s: Bio.SeqRecord.SeqRecord
    :returns formatted string
    :rtype str
    """
    return csvLine(
        s.id,
        s.name,
        len(s),
        s.seq
    )


def featForm(f, idSeq):
    """
    Formats a string in csv with wanted data from a sequence feature
    :param f: input feature
    :type f: Bio.SeqFeature.SeqFeature
    :param idSeq: ID of the sequence the feature belongs to
    :type idSeq: str
    :returns formatted string
    :rtype str
    """
    try:
        length = len(f)
    except TypeError:
        length = None
    return csvLine(
        idSeq,
        f.type,
        length
    )


try:
    # tries to create a directory for the data warehouse
    os.makedirs('warehouse')
except OSError:
    # already exists or error with rights
    pass

with open(
    os.path.join('warehouse', 'features.csv'), 'w', encoding='utf-8'
) as featFile, open(
    os.path.join('warehouse', 'info.csv'), 'w', encoding='utf-8'
) as infoFile:
    # csv header for features file
    featFile.write('idSeq\ttype\tlength\n')
    # csv header for info file
    infoFile.write('idSeq\tname\tlength\tseq\n')
    for i, s in enumerate(seqGenerator()):
        infoFile.write(infoForm(s))
        for f in s.features:
            featFile.write(featForm(f, s.id))
        sys.stdout.write(
            '\b' * 80 +
            'Analyzed {} sequences'.format(i + 1)
        )
    sys.stdout.write('\n')
