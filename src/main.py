import scipy.io
from scipy.sparse import coo_matrix, find
import numpy as np
from SAM import SAM

# Load .mat file
mat_file_path = "\\SAMs398\\src\\testSystems.mat"
mat_contents = scipy.io.loadmat(mat_file_path)

# k = 0
Jac = mat_contents["saveSys"][0][0]
n = Jac.shape[0]
I, J, _ = find(Jac) #dont need values
findJ = coo_matrix((np.ones_like(I), (I, J)), shape=Jac.shape, dtype=bool)
PP = findJ.todense().astype(bool)
PP2 = np.matmul(PP, PP) #equivelent of double multiplication

nnzMM = np.count_nonzero(PP2)
rowM = np.zeros((2*nnzMM,1))
colM = np.zeros((2*nnzMM,1))
valM = np.zeros((2*nnzMM,1))
J0 = Jac

#other preprocessing
nz_M = []
nnz_M = []
nz_LS = []
nnz_LS = []
for j in range(n):
    nz_M.append(np.nonzero(PP[j])[1])
    nnz_M.append(len(nz_M[j]))
    nz_LS.append(np.nonzero(PP2[j])[1])
    nnz_LS.append(len(nz_LS[j]))

MMs = np.zeros((70), dtype= np.object_)
np.put(MMs, 0, J0) #maybe
for i in range(69):
    k = i+1
    Jac = mat_contents["saveSys"][k][0]
    kMM = SAM(k, n, Jac, J0, nnz_LS, nnz_M, nz_LS, nz_M)
    np.put(MMs, k, kMM,)

print("done")