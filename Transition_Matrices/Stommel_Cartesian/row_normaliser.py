from sklearn.preprocessing import normalize 
import numpy as np 
from scipy.sparse import lil_matrix 
from initialise import initialise

# Input data must be integers, conversion during numpy array set-up 
# cannot round correctly

def normaliser(dx,dt,tau):
	lats=np.arange(0, 1E7+dx, dx)
	lons=np.arange(0, 1E7+dx, dx)

	matrix = np.loadtxt("TM_dt{0}_dx{1}_tau{2}_matrix_count.dat".format(dt,dx,tau),unpack=True)
	normalized = normalize(initialise(lons,lats,matrix), norm='l1', axis=1)
	normalized = lil_matrix(normalized)

	file = open("./TM_dt{0}_dx{1}_tau{2}_matrix_rownorm.dat".format(dt,dx,tau),"w")
	file.write("{:}".format(normalized))
	file.close()

dx=1E5
dt=60
tau=20
normaliser(dx,dt,tau)
