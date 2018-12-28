import numpy as np

def pearson_r(x, y) :

    '''Compute Pearson correlation coefficient between two arrays.'''
    # Compute correlation matrix and return entry [0,1]

    return np.corrcoef(x, y)[0,1]
