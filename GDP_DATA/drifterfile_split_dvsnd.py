import numpy as np

buoydata_1=np.loadtxt("buoydata_1_5000.dat",unpack=True)
drogued_1=np.loadtxt("drogue_1_5000.dat",unpack=True)
print "Buoy & Drogue Dataset 1 Extracted"
buoydata_2=np.loadtxt("buoydata_5001_10000.dat",unpack=True)
drogued_2=np.loadtxt("drogue_5001_10000.dat",unpack=True)
print "Buoy & Drogue Dataset 2 Extracted"
buoydata_3=np.loadtxt("buoydata_10001_jun15.dat",unpack=True)
drogued_3=np.loadtxt("drogue_10001_jun15.dat",unpack=True)
print "Buoy & Drogue Dataset 3 Extracted"

buoydata_ID=np.concatenate((buoydata_1[0],buoydata_2[0],buoydata_3[0]))
buoydata_MM=np.concatenate((buoydata_1[1],buoydata_2[1],buoydata_3[1]))
buoydata_DD=np.concatenate((buoydata_1[2],buoydata_2[2],buoydata_3[2]))
buoydata_YY=np.concatenate((buoydata_1[3],buoydata_2[3],buoydata_3[3]))
buoydata_LAT=np.concatenate((buoydata_1[4],buoydata_2[4],buoydata_3[4]))
buoydata_LON=np.concatenate((buoydata_1[5],buoydata_2[5],buoydata_3[5]))
buoydata_TEMP=np.concatenate((buoydata_1[6],buoydata_2[6],buoydata_3[6]))
buoydata_VE=np.concatenate((buoydata_1[7],buoydata_2[7],buoydata_3[7]))
buoydata_VN=np.concatenate((buoydata_1[8],buoydata_2[8],buoydata_3[8]))
buoydata_SPD=np.concatenate((buoydata_1[9],buoydata_2[9],buoydata_3[9]))
buoydata_VARLAT=np.concatenate((buoydata_1[10],buoydata_2[10],buoydata_3[10]))
buoydata_VARLON=np.concatenate((buoydata_1[11],buoydata_2[11],buoydata_3[11]))
buoydata_VARTEMP=np.concatenate((buoydata_1[12],buoydata_2[12],buoydata_3[12]))
buoydata_DROGUED=np.concatenate((drogued_1,drogued_2,drogued_3))


yesfile=open("all_drogued_drifters.dat","w")
nofile=open("all_undrogued_drifters.dat","w")

for i in range(buoydata_ID.size):
	print "Separating files: ", 100.0*i/buoydata_ID.size
	print 100.0*i/buoydata_ID.size
	if buoydata_DROGUED[i]==1:
		yesfile.write("%d, %d, %f, %d, %f, %f, %f, %f, %f, %f, %f, %f, %f \n" % (buoydata_ID[i],buoydata_MM[i],buoydata_DD[i],buoydata_YY[i],buoydata_LAT[i],buoydata_LON[i],buoydata_TEMP[i],buoydata_VE[i],buoydata_VN[i],buoydata_SPD[i],buoydata_VARLAT[i],buoydata_VARLON[i],buoydata_VARTEMP[i]) )
	elif buoydata_DROGUED[i]==0:
		 nofile.write("%d, %d, %f, %d, %f, %f, %f, %f, %f, %f, %f, %f, %f \n" % (buoydata_ID[i],buoydata_MM[i],buoydata_DD[i],buoydata_YY[i],buoydata_LAT[i],buoydata_LON[i],buoydata_TEMP[i],buoydata_VE[i],buoydata_VN[i],buoydata_SPD[i],buoydata_VARLAT[i],buoydata_VARLON[i],buoydata_VARTEMP[i]) )

yesfile.close()
nofile.close()
