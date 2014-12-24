import numpy as _np

_structures = ['helix', 'strand', 'turn']
size_values = len(_structures)


def value(sequence):
    results = _np.zeros(size_values, dtype=_np.float64)
    for f in sequence.features:
        try:
            results[_structures.index(f.type)] += len(f)
        except ValueError:
            pass
    return results / len(sequence)
