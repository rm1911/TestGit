from netCDF4 import Dataset
from scipy.sparse import lil_matrix
import numpy as np

# TM Set-up Parameters #
#----------------------------------------------------------------------------------------------------#
# DATA EXTRACTION #

print
print "STAGE 1: Extracting trajectory time series"

pfile=Dataset("/work/rm1911/parcels/Particle_Files/StommelParticle.nc", 'r')
p_lon = pfile.variables['lon']
p_lat = pfile.variables['lat']
p_time = pfile.variables['time']

print "STAGE 1: Complete"

#----------------------------------------------------------------------------------------------------#
# TRAJECTORY PICKING #

def TM_creator(dx,dt,tau):
	print
	print "STAGE 2: Picking start and end coordinates"

        # Specific to moving eddies test
        lats=np.arange(0, 1E7+dx, dx)
        lons=np.arange(0, 1E7+dx, dx)

        countmatrix=np.zeros((lats.size-1, lons.size-1))
        count=0
        for x in range(lons.size-1):
                for y in range(lats.size-1):
                        count=count+1
                        countmatrix[x][y]=count-1

        matrix=lil_matrix( ( (lats.size-1)*(lons.size-1),(lons.size-1)*(lats.size-1) ) )
	print "STAGE 2: Countmatrix formed"
	for p in range (len(p_lon)):

		print "STAGE 2: {:}, {:}".format(p, 100.0*p/len(p_lon))
		for i in range(0, len( p_lon[p, :]) - dt, tau):
			IN=countmatrix[p_lat[p, :][i]/dx][p_lon[p, :][i]/dx]
			OUT=countmatrix[p_lat[p, :][i+dt]/dx][p_lon[p, :][i+dt]/dx]
			matrix[IN,OUT]=matrix[IN,OUT]+1
		
	print "STAGE 2: Complete"

#----------------------------------------------------------------------------------------------------#

# WRITING SPARSE MATRIX TO FILE

	print
	print "STAGE 3: Writing to file"

	file=open("/work/rm1911/Markov_Chain_Analysis/Stommel_Cartesian/TM_dt{0}_dx{1}_tau{2}_matrix_count.dat".format(dt,dx,tau), "w")
	file.write("{:}".format(matrix))
	file.close()

	print "STAGE 3: Complete"
	print
	print ("TRANSITION MATRIX GENERATED. NICE ONE.")


# .nc file one timestep = 1 days
# TM_creator(dx,dt,tau)

TM_creator(5E4,20,20)

#TM_creator(5E4,60,20)
#TM_creator(5E4,180,20)
#TM_creator(1E5,60,20)
