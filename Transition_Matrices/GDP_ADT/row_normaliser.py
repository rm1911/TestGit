from sklearn.preprocessing import normalize 
import numpy as np 
from scipy.sparse import lil_matrix 
from initialise import initialise

# Input data must be integers, conversion during numpy array set-up 
# cannot round correctly

def normaliser(dadt,dx,dt,tau):
	lats=np.arange(-90, 90+dx, dx)
	lons=np.arange(0, 360+dx, dx)
	adt_range=np.arange(-2,2.2+dadt,dadt)
	if dx==0.5:
		dx="half"
	matrix = np.loadtxt("TM_dx{1}_dt{0}_tau{2}_dadtp2_count.dat".format(dt,dx,tau),unpack=True)
	normalized = normalize(initialise(lons,lats,adt_range,matrix), norm='l1', axis=1)
	normalized = lil_matrix(normalized)

	file = open("./TM_dx{0}_dt{1}_tau{2}_dadtp2_rownorm.dat".format(dx,dt,tau),"w")
	file.write("{:}".format(normalized))
	file.close()

dx=1
dt=60
tau=1
dadt=0.2
normaliser(dadt,dx,dt,tau)
