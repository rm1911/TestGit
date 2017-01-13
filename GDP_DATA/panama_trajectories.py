import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import random
import six
from mpl_toolkits.basemap import Basemap

buoydata_1=np.loadtxt("panama_drifters.dat",unpack=True,delimiter=",")
buoydata_ID=buoydata_1[0] #np.concatenate((buoydata_1[0],buoydata_2[0]))
buoydata_lat=buoydata_1[4] #np.concatenate((buoydata_1[4],buoydata_2[4]))
buoydata_lon=buoydata_1[5] #np.concatenate((buoydata_1[5],buoydata_2[5]))

m = Basemap(projection='cass',llcrnrlon=270, urcrnrlon=291, llcrnrlat=4, urcrnrlat=15, lon_0=280, lat_0=8,resolution='f')
m.drawcoastlines()
m.fillcontinents(color='green',lake_color='white')

m.drawmapboundary(fill_color='white')

lats=[]
lons=[]

colours=list(six.iteritems(colors.cnames))
clist=[]
for i in colours:
	clist.append(str(i[0]))

for i in range(buoydata_ID.size-1):
	if buoydata_ID[i]==buoydata_ID[i+1]:
		if buoydata_lon[i]<=360 or abs(buoydata_lat[i])<=90:
			lats.append(buoydata_lat[i])
			lons.append(buoydata_lon[i])
			#print (100.0*i/buoydata_YY.size)
	else:
		m.plot(lons,lats, latlon=True, color=random.choice(clist), marker='o', markersize=0.001)
		lats=[]
		lons=[]

# draw parallels and meridians.
# label parallels on right and top
# meridians on bottom and left
parallels1 = np.arange(4.,15,1.)
parallels2 = np.arange(4.,15,2.)
# labels = [left,right,top,bottom]
m.drawparallels(parallels1,dashes=[1,3], labels=[0,0,0,0])
m.drawparallels(parallels2,dashes=[5,1], labels=[1,0,0,0])

meridians1 = np.arange(270.,291.,1.)
meridians2 = np.arange(270.,291.,2.)
m.drawmeridians(meridians1,dashes=[1,3], labels=[0,0,0,0])
m.drawmeridians(meridians2,dashes=[5,1], labels=[0,0,0,1])

plt.savefig("Panama_trajectories.png")
plt.close()