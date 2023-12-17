import numpy as np
from scipy.sparse import coo_array

def SAM(k, n, PP, PP2, Jac, J0):
    nz_M = []
    nnz_M = []
    nz_LS = []
    nnz_LS = []
    if k == 2:
        for j in range(n):
            nz_M.append(np.nonzero(PP[j])[1])
            nnz_M.append(len(nz_M[j]))
            nz_LS.append(np.nonzero(PP2[j])[1])
            nnz_LS.append(len(nz_LS[j]))

        max_col = max(nnz_M)
        max_row = max(nnz_LS)
        G = np.zeros((max_row, max_col))
        M = np.zeros((max_row))#rhs?

        rowM = []
        colM = []
        valM = []
        for j in range(n):
            #get the submatrix from G
            G = [[Jac[nz_LS[j][row], nz_M[j][col]] for col in range(nnz_M[j])] for row in range(nnz_LS[j])]

            #M = np.linalg.solve(np.array(G[:nnz_LS[j]][:nnz_M[j]]), )
            #np.linalg.solve does not work for not Square A. use least squares:
            M = np.linalg.lstsq([g_col[:nnz_M[j]] for g_col in G[:nnz_LS[j]]], [col[j] for col in J0.todense()[nz_LS[j]].tolist()])
            M = M[0] #just solution
            np.append(rowM, nz_M[j])
            jarray = np.full((nnz_M[j]), j)
            np.append(colM, jarray)
            np.append(valM, np.array(M[:nnz_M[j]]))

        MM = coo_array(np.array(valM[len(valM)-nnz_M[j]:]),
                       (np.array(rowM[len(rowM)-nnz_M[j]:]),
                        np.array(colM[len(colM)-nnz_M[j]:])))
        
        return #['SAM', Jac[:][perm[:]], L, U, MM]

