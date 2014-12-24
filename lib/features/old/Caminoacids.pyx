import numpy as _np
cimport numpy as _np
cimport cython

cdef unicode _alphabet = u'ACDEFGHIKLMNOPQRSTUVWY'
sizeValues = 22 # len(_alphabet)
cdef double *_placeholderX = [
    .078, .019, .053, .063, .039, .072, .023, .053, .059, .091, .023,
    .043, .0, .052, .042, .051, .068, .059, .0, .066, .014, .032
]
cdef double *_placeholderB = [
    .0, .0, .5096153846153846, .0, .0, .0, .0, .0, .0, .0, .0,
    .0, .0, .0, .0, .49038461538461536, .0, .0, .0, .0, .0, .0, 
]
cdef double *_placeholderZ = [
    .0, .0, .0, .6, .0, .0, .0, .0, .0, .0, .0,
    .0, .0, .0, .4, .0, .0, .0, .0, .0, .0, .0, 
]
cdef double *_placeholderJ = [
    .0, .0, .0, .0, .0, .0, .0, .3680555555555556, .0, .6319444444444444, .0,
    .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, 
]

@cython.boundscheck(False)
@cython.wraparound(False)
def value(sequence):
    """
    Computes the proportion of every aminoacid in a sequence
    :param sequence: sequence to be analyzed
    :type values: Bio.SeqRecord.SeqRecord
    :returns array containing, for every aminoacid, its proportion in the sequence
    :rtype numpy.ndarray
    """
    cdef _np.intp_t i
    cdef unsigned int length
    cdef unicode letter
    cdef double[:] *results = [
        .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0,
        .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, 
    ]
    
    length = len(sequence)
    for letter in sequence.seq:
        try:
            i = _alphabet.index(letter)
            results[i] += (1. / length)
        except ValueError:
            if letter == 'B':
                placeholder = _placeholderB
            elif letter == 'Z':
                placeholder = _placeholderZ
            elif letter == 'J':
                placeholder = _placeholderJ
            else:
                placeholder = _placeholderX
            for i in range(sizeValues):
                results += (placeholder / length)
    print(<double[:]>results)
    return results


