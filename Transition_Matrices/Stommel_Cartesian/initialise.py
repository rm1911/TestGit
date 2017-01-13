import numpy as np
from scipy.sparse import lil_matrix

def initialise(lonarray,latarray,sparse):
	"""
	Requires coordinate arrays for at the relevant resolution and the sparse matrix entries	
	"""
	full=lil_matrix( ( (latarray.size-1)*(lonarray.size-1),(lonarray.size-1)*(latarray.size-1) ) )
	for i in range(sparse[0].size):
		full[sparse[0][i], sparse[1][i]]=sparse[2][i]
	return full
