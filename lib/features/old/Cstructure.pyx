import numpy as _np
cimport numpy as _np
cimport cython

_structures = ['helix', 'strand', 'turn']
sizeValues = len(_structures)

@cython.boundscheck(False)
@cython.wraparound(False)
def value(sequence):
    cdef double[:] results
    cdef _np.intp_t i
    cdef unsigned int l
    
    results = _np.zeros(sizeValues, dtype = _np.float64)
    for f in sequence.features:
        try:
            i = _structures.index(f.type)
            l = len(f)
            results[i] += l
        except ValueError:
            pass
    l = len(sequence)
    results = _np.divide(results, l)
    return results

