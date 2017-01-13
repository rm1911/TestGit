import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset

years=["1993"]#range(1993,2013,1)
months=["01"]#,"02","03","04","05","06","07","08","09","10","11","12"]
days=["01","02","03","04","05","06","07","08","09"]+range(10,29,1)

average_grid=np.zeros((720,1440))

count=0
for year in years:
	for month in months:
		for day in days:
			print year, month, day
			pfile=Dataset("{0}/dt_global_allsat_madt_h_{0}{1}{2}_20140106.nc".format(year,month,day),"r")
			count+=1.

			SSH = pfile.variables['adt']
			average_grid=average_grid+SSH[0]

			#plt.pcolormesh(SSH[0])
			#plt.colorbar()
			#plt.show()					

lons=np.arange(0,360,0.25)
lats=np.arange(0,180,0.25)

average_grid=average_grid/count
file=open("SSH_profiling.dat","w")
for i in range(average_grid.shape[0]):
#	print np.mean(average_grid[i])
	file.write("{0}".format(np.mean(average_grid[i]) ) )
	file.write("\n")
file.close()

"""
plt.pcolormesh(lons,lats,average_grid/count)
plt.colorbar(orientation='horizontal', label="Sea Surface Height [m]")
plt.clim(-1.75,1.75)
plt.xlim([0,360])
plt.ylim([0,180])
plt.xticks([0,90,180,270,360],["0E","90E","180E","90W","0E"])
plt.yticks([0,30,60,90,120,150,180],["90S","60S","30S","0","30N","60N","90N"])
plt.show()
"""
