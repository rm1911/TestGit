import numpy as np
import matplotlib as mpl
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
from my_round import my_round
from mpl_toolkits.basemap import Basemap
### Drifter Coverage Map: Drogued vs Undrogued

n=0.5
lats=np.arange(-90,90.5,n)
lons=np.arange(0,360.5,n)

timemap1=np.loadtxt("./Drifte_Coverage/Halfdeg_coverage_total.dat",unpack=True)
#timemap1=np.loadtxt("halfdeg_coverage_test1.dat",unpack=True)
#timemap2=np.loadtxt("halfdeg_coverage_test2.dat",unpack=True)
#timemap1=np.loadtxt("./Drifte_Coverage/1deg_coverage_drogued.dat",unpack=True)
#timemap2=np.loadtxt("./Drifte_Coverage/1deg_coverage_undrogued.dat",unpack=True)
#timemap1=np.loadtxt("./Drifte_Coverage/1deg_coverage_NONINO.dat",unpack=True)
#timemap2=np.loadtxt("./Drifte_Coverage/1deg_coverage_ELNINO.dat",unpack=True)
#timemap3=np.loadtxt("./Drifte_Coverage/1deg_coverage_LANINA.dat",unpack=True)

def grid(vector,res,latarray,lonarray):
	# INPUT: Data vector
	# OUTPUT: 2D grid
	array=np.zeros((latarray.size-1,lonarray.size-1))
	count=-1
	for i in range(latarray.size-1):
		for j in range(lonarray.size-1):
			count=count+1
			array[i][j]=vector[count]

	return array


timemap1=grid(timemap1,n,lats,lons)
#timemap2=grid(timemap2,n,lats,lons)
#timemap3=grid(timemap3,n,lats,lons)

masked1=np.ma.array(timemap1,mask=np.isnan(timemap1))
#masked2=np.ma.array(timemap2,mask=np.isnan(timemap2))
#masked3=np.ma.array(timemap3,mask=np.isnan(timemap3))
#cmap=mpl.colors.ListedColormap(['w','b','y','r'])
#bounds=[0,1,2,3,4]

cmap=matplotlib.colors.ListedColormap(['w','#8080ff','#3333ff','#ffcc80','#ff9900','#ff8080','#ff0000'])
bounds=[0,1,np.log10(50),2,np.log10(500),3]
norm=mpl.colors.BoundaryNorm(bounds,cmap.N)

#plt.subplot(311)
m = Basemap(projection='robin',lon_0=270,lat_0=0,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='white',lake_color='white')
m.drawmapboundary(fill_color='white')
lonarray,latarray=np.meshgrid(lons[:-1],lats[:-1])
c=m.pcolormesh(lonarray,latarray,np.log10(masked1),cmap=cmap,vmin=0,vmax=3,norm=norm,latlon=True)
#plt.title("Standard State - No Nino")

"""
plt.subplot(312)
m = Basemap(projection='robin',lon_0=270,lat_0=0,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='white',lake_color='white')
m.drawmapboundary(fill_color='white')
lonarray,latarray=np.meshgrid(lons[:-1],lats[:-1])
c=m.pcolormesh(lonarray,latarray,np.log10(masked2),cmap=cmap,vmin=0,vmax=4,norm=norm,latlon=True)
plt.title("El Nino")

plt.subplot(313)
m = Basemap(projection='robin',lon_0=270,lat_0=0,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='white',lake_color='white')
m.drawmapboundary(fill_color='white')
lonarray,latarray=np.meshgrid(lons[:-1],lats[:-1])
c=m.pcolormesh(lonarray,latarray,np.log10(masked3),cmap=cmap,vmin=0,vmax=4,norm=norm,latlon=True)
plt.title("La Nina")

plt.show()
"""
fig = plt.figure(figsize=(8, 3))
ax = fig.add_axes([0.05, 0.475, 0.9, 0.15])

cb2=mpl.colorbar.ColorbarBase(ax,cmap=cmap,label="Number of coordinate readings",ticks=bounds,norm=norm,orientation='horizontal',spacing='proportional')
cb2.ax.set_xticklabels(['0','10$^1$',' ','10$^2$',' ','10$^3$'])
plt.show()
