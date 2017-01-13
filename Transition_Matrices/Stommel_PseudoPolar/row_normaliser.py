from sklearn.preprocessing import normalize 
import numpy as np 
from scipy.sparse import lil_matrix 
from initialise import initialise

# Input data must be integers, conversion during numpy array set-up 
# cannot round correctly

def normaliser(dpsi,dtheta,dt,tau):
	psigrid=np.arange(0, 320000+dpsi, dpsi)
	tgrid=np.arange(0, 360+dtheta, dtheta)

	matrix = np.loadtxt("PTM_dt{0}_dpsi{1}_dtheta{2}_tau{3}_matrix_count.dat".format(dt,dpsi,dtheta,tau),unpack=True)
	normalized = normalize(initialise(psigrid,tgrid,matrix), norm='l1', axis=1)
	normalized = lil_matrix(normalized)

	file = open("./PTM_dt{0}_dpsi{1}_dtheta{2}_tau{3}_matrix_rownorm.dat".format(dt,dpsi,dtheta,tau),"w")
	file.write("{:}".format(normalized))
	file.close()

dpsi=2000
dtheta=4
dt=60
tau=20

normaliser(dpsi,dtheta,dt,tau)
