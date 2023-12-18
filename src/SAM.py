import numpy as np
from scipy.sparse import coo_array

def SAM(k, n, Jac, J0, nnz_LS, nnz_M, nz_LS, nz_M):
    max_col = max(nnz_M)
    max_row = max(nnz_LS)
    G = np.zeros((max_row, max_col))
    M = np.zeros((max_row))

    rowM = []
    colM = []
    valM = []
    for j in range(n):
        #get the submatrix from G
        G = [[Jac[nz_LS[j][row], nz_M[j][col]] \
              for col in range(nnz_M[j])] \
                for row in range(nnz_LS[j])]

        #np.linalg.solve does not work for not Square A. use least squares:
        M = np.linalg.lstsq([g_col[:nnz_M[j]] \
                for g_col in G[:nnz_LS[j]]],\
                [col[j] for col in J0.todense()[nz_LS[j]].tolist()])
        M = M[0] #just solution (also gives residual)

        rowM = np.append(rowM, nz_M[j][:nnz_M[j]])
        jarray = np.full((nnz_M[j]), j, dtype=np.int64)
        colM = np.append(colM, jarray)
        valM = np.append(valM, np.array(M[:nnz_M[j]]))

    MM = coo_array((valM, (rowM.astype(np.int64), colM.astype(np.int64))))
    
    return MM