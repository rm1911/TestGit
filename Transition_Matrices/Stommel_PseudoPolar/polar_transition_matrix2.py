from netCDF4 import Dataset
from scipy.sparse import lil_matrix
import numpy as np

# TM Set-up Parameters #
#----------------------------------------------------------------------------------------------------#
# DATA EXTRACTION #


pfile=Dataset("/work/rm1911/parcels/Particle_Files/StommelParticle_polar.nc", 'r')

p_psi = pfile.variables['psi']
p_theta = pfile.variables['theta']
p_time = pfile.variables['time']

#----------------------------------------------------------------------------------------------------#
# TRAJECTORY PICKING #

def TM_creator(dpsi,dtheta,dt,tau):

        # Specific to moving eddies test
        psigrid=np.arange(0, 320000+dpsi, dpsi) # streamfunction diff from x0,y0 at [1560,5000]
        tgrid=np.arange(0, 360+dtheta, dtheta)

        countmatrix=np.zeros((tgrid.size-1, psigrid.size-1))
        count=0
        for x in range(tgrid.size-1):
                for y in range(psigrid.size-1):
                        count=count+1
                        countmatrix[x][y]=count-1

        matrix=lil_matrix( ( (tgrid.size-1)*(psigrid.size-1),(tgrid.size-1)*(psigrid.size-1) ) )

	for p in range (len(p_psi)):
		print 100.0*p/len(p_psi)
		for i in range(0, len( p_psi[p, :]) - dt, tau):
			IN=countmatrix[p_theta[p, :][i]/dtheta][p_psi[p, :][i]/dpsi]
			OUT=countmatrix[p_theta[p, :][i+dt]/dtheta][p_psi[p, :][i+dt]/dpsi]
			matrix[IN,OUT]=matrix[IN,OUT]+1

#----------------------------------------------------------------------------------------------------#

# WRITING SPARSE MATRIX TO FILE

	file=open("/work/rm1911/parcels/PTM_dt{0}_dpsi{1}_dtheta{2}_tau{3}_matrix_count.dat".format(dt,dpsi,dtheta,tau), "w")
	file.write("{:}".format(matrix))
	file.close()


# dt/tau = 1 step : 1 day

#TM_creator(dpsi,dtheta,dt,tau)

TM_creator(2000,4,60,20)

#TM_creator(2000,1,60,20)
#TM_creator(2000,1,180,20)
#TM_creator(4000,1,60,20)
