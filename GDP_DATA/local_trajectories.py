import numpy as np

# Drifters which pass through North Pacific Patch
# Drifters which pas through Algulhas Current

buoydata_1=np.loadtxt("all_drogued_drifters.dat",unpack=True,delimiter=',')
buoydata_2=np.loadtxt("all_undrogued_drifters.dat",unpack=True,delimiter=',')

buoydata_ID=buoydata_1[0]
buoydata_MM=buoydata_1[1]
buoydata_DD=buoydata_1[2]
buoydata_YY=buoydata_1[3]
buoydata_LAT=buoydata_1[4]
buoydata_LON=buoydata_1[5]
buoydata_TEMP=buoydata_1[6]
buoydata_VE=buoydata_1[7]
buoydata_VN=buoydata_1[8]
buoydata_SPD=buoydata_1[9]
buoydata_VARLAT=buoydata_1[10]
buoydata_VARLON=buoydata_1[11]
buoydata_VARTEMP=buoydata_1[12]

panfile=open("Panama_drifters.dat","w")
traj=False

for i in range(buoydata_ID.size-1):
	print (100.0*i/buoydata_ID.size)
	if buoydata_LON[i]>=269 and buoydata_LON[i]<291 and buoydata_LAT[i]>=-1 and buoydata_LAT[i]<17:
		traj=True
	if buoydata_ID[i]!=buoydata_ID[i+1]:
		traj=False
	if traj==True:
		panfile.write("%d, %d, %f, %d, %f, %f, %f, %f, %f, %f, %f, %f, %f \n" % (buoydata_ID[i],buoydata_MM[i],buoydata_DD[i],buoydata_YY[i],buoydata_LAT[i],buoydata_LON[i],buoydata_TEMP[i],buoydata_VE[i],buoydata_VN[i],buoydata_SPD[i],buoydata_VARLAT[i],buoydata_VARLON[i],buoydata_VARTEMP[i]) )
	
panfile.close()