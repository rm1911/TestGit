import numpy as np
from netCDF4 import Dataset
import datetime as dt
from py import path
from glob import glob
import datetime

buoydata=np.loadtxt("./Original_Data/buoydata_1_5000.dat", unpack=True )
#buoydata=np.loadtxt("./Original_Data/buoydata_test.dat", unpack=True )
metadata=np.genfromtxt("./Metadata/dirfl_1_5000.dat", unpack=True, dtype='str' )

buoydata_ID=np.array(buoydata[0], dtype='int')
buoydata_MM=buoydata[1]
buoydata_DD=np.rint(buoydata[2])
buoydata_YY=buoydata[3]
buoydata_LAT=buoydata[4]
buoydata_LON=buoydata[5]
buoydata_TEMP=buoydata[6]
buoydata_VE=buoydata[7]
buoydata_VN=buoydata[8]
buoydata_SPD=buoydata[9]
buoydata_VARLAT=buoydata[10]
buoydata_VARLON=buoydata[11]
buoydata_VARTEMP=buoydata[12]

buoydata_ADT=np.zeros((buoydata_VARTEMP.size))
buoydata_ADT.fill(999.999)

path = "./AVISO/*/*.nc"
date=datetime.date(1993,1,1)
count=0
for filename in glob(path):
	print (filename)
	with Dataset(filename) as dataset:
		#for line in f:
		index=np.argwhere( (buoydata_DD==date.day) & (buoydata_MM==date.month) & (buoydata_YY==date.year) )
		#print (index.size)
		if index.size>0:
			SSH=dataset.variables['adt']
			for i in index:
				i=np.float(i)
				if np.abs(buoydata_LAT[i]<90) and buoydata_LON[i]<360:
					reading=SSH[0][(90+buoydata_LAT[i])/0.25][buoydata_LON[i]/0.25]
					buoydata_ADT[i]=reading
	date+=datetime.timedelta(days=1)
	
new_buoys=Dataset('./buoydata_test.nc','w',format='NETCDF4')
new_buoys.createDimension('vars',14)
new_buoys.createDimension('readings',len(buoydata_ID) )

# 1 ID
ID = new_buoys.createVariable("ID", "i4", ("readings"))
ID.long_name = "Identity Number for each drifter"
ID.standard_name = "ID"
ID[:] = buoydata_ID

# 2 MM
MM = new_buoys.createVariable("MM", "i4", ("readings"))
MM.long_name = "Month"
MM.standard_name = "MM"
MM[:] = buoydata_MM

# 3 DD
DD = new_buoys.createVariable("DD", "f4", ("readings"))
DD.long_name = "Day"
DD.standard_name = "DD"
DD[:] = buoydata[2]

# 4 YY
YY = new_buoys.createVariable("YY", "i4", ("readings"))
YY.long_name = "Year"
YY.standard_name = "YY"
YY[:] = buoydata_YY

# 5 LAT
LAT = new_buoys.createVariable("LAT", "f4", ("readings"))
LAT.long_name = "Latitude"
LAT.standard_name = "LAT"
LAT[:] = buoydata_LAT

# 6 LON
LON = new_buoys.createVariable("LON", "f4", ("readings"))
LON.long_name = "Longitude"
LON.standard_name = "LON"
LON[:] = buoydata_LON

# 7 TEMP
TEMP = new_buoys.createVariable("TEMP", "f4", ("readings"))
TEMP.long_name = "Temperature"
TEMP.standard_name = "TEMP"
TEMP[:] = buoydata_TEMP

# 8 VE
VE = new_buoys.createVariable("VE", "f4", ("readings"))
VE.long_name = "Velocity_Eastwards"
VE.standard_name = "VE"
VE[:] = buoydata_VE

# 9 VN
VN = new_buoys.createVariable("VN", "f4", ("readings"))
VN.long_name = "Velocity_Northwards"
VN.standard_name = "VN"
VN[:] = buoydata_VN

# 10 SPD
SPD = new_buoys.createVariable("SPD", "f4", ("readings"))
SPD.long_name = "SPEED"
SPD.standard_name = "SPD"
SPD[:] = buoydata_SPD

# 11 VARLAT
VARLAT = new_buoys.createVariable("VARLAT", "f4", ("readings"))
VARLAT.long_name = "Latitude variance"
VARLAT.standard_name = "VARLAT"
VARLAT[:] = buoydata_VARLAT

# 12 VARLON
VARLON = new_buoys.createVariable("VARLON", "f4", ("readings"))
VARLON.long_name = "Longitude variance"
VARLON.standard_name = "VARLON"
VARLON[:] = buoydata_VARLON

# 13 VARTEMP
VARTEMP = new_buoys.createVariable("VARTEMP", "f4", ("readings"))
VARTEMP.long_name = "Temperature variance"
VARTEMP.standard_name = "VARTEMP"
VARTEMP[:] = buoydata_VARTEMP

# 14 ADT
ADT = new_buoys.createVariable("ADT", "f4", ("readings"))
ADT.long_name = "Absolute Dynamic Topography"
ADT.standard_name = "ADT"
ADT[:] = buoydata_ADT

new_buoys.close()