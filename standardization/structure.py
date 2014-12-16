import numpy as np

# Helix, beta strand and turn score

    
def value(sequence):
    lengths = {
        'helix': 0,
        'strand': 0,
        'turn': 0
    }
    for f in sequence.features:
        try:
            lengths[f.type] += len(f)
        except KeyError:
            pass
    total = len(s)
    return np.array([
        lengths['helix'] / total,
        lengths['strand'] / total,
        lengths['turn'] / total
    ])

