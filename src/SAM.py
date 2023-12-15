import numpy as np
from scipy.sparse import coo_array

def SAM(perm, k, n, PP, Jac, j0, L, U):
    nz_M = []
    nnz_M = []
    nz_LS = []
    nnz_LS = []
    if k == 2:
        for j in range(n):
            nz_M.append(np.nonzero(PP)[j])
            nnz_M.append(len(nz_M[j]))
            nz_LS.append(np.nonzero(PP)[j])
            nnz_LS.append(len(nz_LS[j]))

        max_col = max(nnz_M)
        max_row = max(nnz_LS)
        G = np.zeros((max_row, max_col))
        M = np.zeros((max_row))#rhs?

        rowM = []
        colM = []
        valM = []

