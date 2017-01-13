import numpy as np
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
from my_round import my_round
from mpl_toolkits.basemap import Basemap


#Each line in the data files is a six-hourly update
#Lines counted as 6 hours periods

#buoydata_1=np.loadtxt("./elnino_drifters.dat",unpack=True,delimiter=",")
#buoydata_1=np.loadtxt("./elnino_drifters.dat",unpack=True,delimiter=",")
#buoydata_1=np.loadtxt("./lanina_drifters.dat",unpack=True,delimiter=",")

buoydata_1=np.loadtxt("./all_drogued_drifters.dat",unpack=True,delimiter=",")
buoydata_2=np.loadtxt("./all_undrogued_drifters.dat",unpack=True,delimiter=",")
#buoydata_1=np.loadtxt("./BD_test2.dat",unpack=True,delimiter=",")

buoydata_ID=np.concatenate((buoydata_1[0],buoydata_2[0]))
buoydata_LAT=np.concatenate((buoydata_1[4],buoydata_2[4]))
buoydata_LON=np.concatenate((buoydata_1[5],buoydata_2[5]))

n=0.5
lats=np.arange(-90,90.5,n)
lons=np.arange(0,360.5,n)

timemap=np.zeros( (lats.size-1,lons.size-1) )
drifternum=np.zeros( (lats.size-1,lons.size-1) )

for i in range(buoydata_ID.size-1):
	if buoydata_LON[i]>=360 or abs(buoydata_LAT[i])>=90:
		print ("Dodgy values")
	else:
		print (100.0*i/buoydata_ID.size)
		lat=buoydata_LAT[i]
		lon=buoydata_LON[i]
		timemap[(lat+90)/n][lon/n]=timemap[(lat+90)/n][lon/n]+1
		# makes of use of the irregular numpy rounding i.e. 7.6-->7.0
		#if buoydata_ID[i+1]==buoydata_ID[i] and my_round(buoydata_LON[i],n)!=my_round(buoydata_LON[i+1],n) and my_round(buoydata_LAT[i],n)!=my_round(buoydata_LAT[i+1],n):
		#	drifternum[(lat+90)/n][lon/n]==drifternum[(lat+90)/n][lon/n]+1

# Writing drifter coverage vector to file for analysis

file=open("Halfdeg_coverage_total.dat","w")

for i in range(lats.size-1):
	for j in range(lons.size-1):
		if timemap[i][j]==0:
			timemap[i][j]=np.float('nan')
		file.write("{:} \n".format(timemap[i][j]))
file.close()