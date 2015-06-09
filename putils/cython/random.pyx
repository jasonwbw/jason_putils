#cython: boundscheck=False
#cython: cdivision=True

cimport cython
import numpy as np
import time

cimport numpy as np

from libc.math cimport exp
from libc.stdlib cimport rand, RAND_MAX
from scipy.special import expit

REAL = np.float32
ctypedef np.float32_t REAL_t
#end define

cdef np.ndarray[REAL_t, ndim=2] _add_random(np.ndarray[REAL_t, ndim=2] A, const int isLinear):
    cdef:
        int i, j
        float r
        int A_n = A.shape[0]
        int A_m = A.shape[1]
        np.ndarray[REAL_t, ndim=2] C

    C = np.zeros((A_n, A_m), dtype = REAL)
    for i in xrange(A_n):
        for j in xrange(A_m):
            if isLinear == 1:
                C[i, j] = A[i, j] + rand() / float(RAND_MAX)
            else:
                r = rand() / float(RAND_MAX)
                if A[i, j] > r:
                    C[i, j] = 1
                else:
                    C[i, j] = 0
    return C 

def add_random(A, isLinear):
    if isLinear:
        return _add_random(A, 1)
    else:
        return _add_random(A, 0)

fast_add_random = add_random
#end add_random