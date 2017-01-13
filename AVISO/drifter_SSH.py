import numpy as np
import matplotlib.pyplot as plt

#buoydata=np.loadtxt("./Modified_Data/test_drifters.dat", unpack=True )
buoydata=np.loadtxt("./Modified_Data/buoydata_1_5000_SSH_drg.dat2", unpack=True )
buoydata_LAT=buoydata[4]
buoydata_LON=buoydata[5]
buoydata_SSH=buoydata[13]



plt.scatter(buoydata_LON, buoydata_LAT, c=buoydata_SSH, s=10, lw=0)
plt.xlim([0,360])
plt.ylim([-90,90])
plt.colorbar()
plt.clim(-2,2)
plt.show()

