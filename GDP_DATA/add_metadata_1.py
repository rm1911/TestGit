import numpy as np
import datetime as dt
# Add "Drogue" column to drifter data files #
# Download metadata

#buoydata_1=np.loadtxt("./Drifter_Data_Storage/buoy_example.dat",unpack=True)
buoydata_1=np.loadtxt("./Drifter_Data_Storage/buoydata_1_5000.dat",unpack=True)
#buoydata_1=np.loadtxt("./Drifter_Data_Storage/buoydata_5001_10000.dat",unpack=True)
#buoydata_1=np.loadtxt("./Drifter_Data_Storage/buoydata_10001_jun15.dat",unpack=True)
metadata_1=np.loadtxt("./Drifter_Data_Storage/dirfl_1_5000.dat",unpack=True,dtype='string')

#metadata_1[12] # Drogue Date Lost

#file=open("drogued_list_example.dat","w")
file=open("drogue_1_5000.dat","w")

for i in range(buoydata_1[0].size):
	print 100.0*i/buoydata_1[0].size
	for m in range(metadata_1[0].size):	
		if buoydata_1[0][i]==float(metadata_1[0][m]):
			split=metadata_1[12][m].split('/',2)
			date1=dt.date(int(split[0]),int(split[1]),int(split[2]))
			date2=dt.date(int(buoydata_1[3][i]),int(buoydata_1[1][i]),int(buoydata_1[2][i]))
			if date1<=date2:
				file.write("0 \n")
			else:
				file.write("1 \n")
file.close()
