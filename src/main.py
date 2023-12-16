import scipy.io
from scipy.sparse import coo_matrix, find
import numpy as np
from SAM import SAM

# Load .mat file
mat_file_path = "\\SAMs398\\src\\testSystems.mat"
mat_contents = scipy.io.loadmat(mat_file_path)

# k = 0
Jac = mat_contents["saveSys"][0][0]
I, J, _ = find(Jac) #dont need values
findJ = coo_matrix((np.ones_like(I), (I, J)), shape=Jac.shape, dtype=bool)
PP = findJ.todense().astype(bool)
PP2 = np.logical_and(PP, PP) #equivelent of double multiplication

nnzMM = np.count_nonzero(PP2)
rowM = np.zeros((2*nnzMM,1))
colM = np.zeros((2*nnzMM,1))
valM = np.zeros((2*nnzMM,1))
J0 = Jac

# print(coo_matrix(PP))
# print(coo_matrix(PP2))

# for i in range(69):
# Jac = mat_contents["saveSys"][1][0]
# SAM(2, 100, PP, Jac, J0)
