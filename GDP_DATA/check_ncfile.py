from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np

file = Dataset("./buoydata_1_5000_SSH.nc ", 'r')

#print (file.variables.keys() )

LON = file.variables['LON']
LAT = file.variables['LAT']
ADT = file.variables['ADT']

ADT=np.array(ADT)

ADT[ADT>900]=np.nan

plt.scatter(LON[-4000000:], LAT[-4000000:], c=ADT[-4000000:], s=0.5, lw=0)
plt.xlim([0,360])
plt.ylim([-90,90])
plt.xticks([0,90,180,270,360],["0","90E","180E","270E","0"])
plt.yticks([-90,-60,-30,0,30,60,90],["90S","60S","30S","0","30N","60N","90N"])
plt.colorbar(label="Absolute Dynamic Topography [m]")
plt.clim(-2,2)
plt.savefig("./SSH_trajectories.png")
#plt.show()