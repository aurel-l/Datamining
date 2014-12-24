import numpy as _np
cimport numpy as _np
cimport cython

sizeValues = 1

@cython.boundscheck(False)
@cython.wraparound(False)
def value(sequence):
    """
    Computes the length of the input sequence
    :param values: input sequence
    :type values: Bio.SeqRecord.SeqRecord
    :returns length of the sequence
    :rtype int
    """
    cdef unsigned int l
    
    l = len(sequence)
    return l

