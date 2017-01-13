import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import random
import six
from mpl_toolkits.basemap import Basemap

colours=list(six.iteritems(colors.cnames))
clist=[]
for i in colours:
	clist.append(str(i[0]))
	
buoydata_1=np.loadtxt("./kuroshio_undrogued_drifters_half.dat",unpack=True,delimiter=",")
#buoydata_2=np.loadtxt("./all_undrogued_drifters.dat",unpack=True,delimiter=",")

buoydata_ID=buoydata_1[0]#np.concatenate((buoydata_1[0],buoydata_2[0]))
buoydata_lat=buoydata_1[4]#np.concatenate((buoydata_1[4],buoydata_2[4]))
buoydata_lon=buoydata_1[5]#np.concatenate((buoydata_1[5],buoydata_2[5]))



m = Basemap(projection='cass',llcrnrlon=130, urcrnrlon=160, llcrnrlat=20, urcrnrlat=40, lon_0=145, lat_0=30,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='green',lake_color='white')
m.drawmapboundary(fill_color='white')

lats=[]
lons=[]
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
parallels = np.arange(20.,41,1.)
# labels = [left,right,top,bottom]
m.drawparallels(parallels,labels=[False,False,False,False])
meridians = np.arange(130.,161.,1.)
m.drawmeridians(meridians,labels=[False,False,False,False])

		
#plt.xlim([0,360])
#plt.ylim([-90,90])
#plt.xticks((0,45,90,135,180,225,270,315,360),["0","45E","90E","135E","180E","135W","90W","45W","0"])
#plt.yticks((-90,-60,-30,0,30,60,90),["90S","60S","30S","0","30N","60N","90N"])

plt.show()
