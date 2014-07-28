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


cdef np.ndarray[REAL_t, ndim=2] _multi_onenum(np.ndarray[REAL_t, ndim=2] A, const float p, const int ismulti):
    cdef:
        int i, j
        np.ndarray[REAL_t, ndim=2] C

    C = np.zeros((A.shape[0], A.shape[1]), dtype = REAL)
    for i in xrange(A.shape[0]):
        for j in xrange(A.shape[1]):
            if ismulti == 1:
                C[i, j] = A[i, j] * p
            else:
                C[i, j] = A[i, j] / p
    return C

def multi_onenum(A, p, multi = True):
    if multi:
        return _multi_onenum(A, p, 1)
    else:
        return _multi_onenum(A, p, 0)

fast_multi_onenum = multi_onenum
#end matrix multi one number