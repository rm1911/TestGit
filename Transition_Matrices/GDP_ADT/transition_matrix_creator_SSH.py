# IMPORT MODULES #
from scipy.sparse import lil_matrix
import numpy as np
from netCDF4 import Dataset
import math
#----------------------------------------------------------------------------------------------------#
# BUOY DATA EXTRACTION #

#file1 = Dataset("/work/rm1911/GDP_Data/buoydata_1_5000_SSH.nc", 'r')
#file2 = Dataset("/work/rm1911/GDP_Data/buoydata_5001_10000_SSH.nc", 'r')
#file3 = Dataset("/work/rm1911/GDP_Data/buoydata_10001_15000_SSH.nc", 'r')
file4 = Dataset("/work/rm1911/GDP_Data/buoydata_15001_jun16_SSH.nc", 'r')

#ID1 = file1.variables['ID']
#LON1 = file1.variables['LON']
#LAT1 = file1.variables['LAT']
#ADT1 = file1.variables['ADT']
#ID2 = file2.variables['ID']
#LON2 = file2.variables['LON']
#LAT2 = file2.variables['LAT']
#ADT2 = file2.variables['ADT']
#ID3 = file3.variables['ID']
#LON3 = file3.variables['LON']
#LAT3 = file3.variables['LAT']
#ADT3 = file3.variables['ADT']
ID4 = file4.variables['ID']
LON4 = file4.variables['LON']
LAT4 = file4.variables['LAT']
ADT4 = file4.variables['ADT']

#ID=np.concatenate( (np.array(ID1),np.array(ID2),np.array(ID3),np.array(ID4)) )
#LON=np.concatenate( (np.array(LON1),np.array(LON2),np.array(LON3),np.array(LON4)) )
#LAT=np.concatenate( (np.array(LAT1),np.array(LAT2),np.array(LAT3),np.array(LAT4)) )
#ADT=np.concatenate( (np.array(ADT1),np.array(ADT2),np.array(ADT3),np.array(ADT4)) )
ID=np.array(ID4)
LON=np.array(LON4)
LAT=np.array(LAT4)
ADT=np.array(ADT4)
#----------------------------------------------------------------------------------------------------#
def adtlonlat2i(adt,dadt,lon,lat,res,cell_no):
        adt=adt + 2
        lat=lat+90
        ix=int(lon/res)
        iy=int(lat/res)*(360/res)
        return (int(adt/dadt)*cell_no) + ix+iy

def i2adtlonlat(i,res,cell_no):
        adt=(i/cell_no)
        i=i%cell_no
        lon = res*(i%(360/res))
        lat = res*(i/(360/res))
        return lon, lat-90, (adt*dadt)-2

#-------------------------------------------------------------------------------------------------$
def TM_creator(dadt,dx,dt,tau):
	# positions every 6 hour ->  multiply dt & tau by four
	dt=dt*4
	tau=tau*4

	if dx==0.5:
		res="half"
	else:
		res=str(dx)

	# CREATE LABELLING ARRAY 
	# each dx cells contains index number
        lats=np.arange(-90, 90+dx, dx)
        lons=np.arange(0, 360+dx, dx)
	cells=(lats.size-1)*(lons.size-1)
	adt_range=np.arange(-2,2.2+dadt,dadt)
	# SET-UP SPARSE MATRIX
        matrix=lil_matrix( ( (lats.size-1)*(lons.size-1)*(adt_range.size-1),(lons.size-1)*(lats.size-1)*(adt_range.size-1) ) )

	# LOOP THROUGH BUOYDATA - ASSIGN INDEX VALUE BASED ON COORDINATES
	for i in range (0,ID.size-dt,tau):
		print "{0}".format(100.0*i/ID.size)
		if ID[i]==ID[i+dt]:
			if LON[i]>=360 or LON[i+dt]>=360 or abs(LAT[i])>=90 or abs(LAT[i+dt])>=90 or LON[i]==0 or LON[i+dt]==0 or ADT[i]>999 or ADT[i+dt]>999 or math.isnan(ADT[i])==True or math.isnan(ADT[i+dt])==True:
				pass
			else:
				print ADT[i], LON[i], LAT[i], ADT[i+dt], LON[i+dt], LAT[i+dt]
				IN=adtlonlat2i(ADT[i],dadt,LON[i],LAT[i],dx,cells)
				OUT=adtlonlat2i(ADT[i+dt],dadt,LON[i+dt],LAT[i+dt],dx,cells)
				matrix[IN,OUT]=matrix[IN,OUT]+1

	# WRITING SPARSE MATRIX TO FILE

	file=open("/work/rm1911/Markov_Chain_Analysis/GDP_ADT/TM_dx{0}_dt{1}_tau{2}_dadtp2_count.dat".format(res,dt/4,tau/4), "w")
	file.write("{0}".format(matrix))
	file.close()

#----------------------------------------------------------------------------------------------------#
# REPEAT TM_CREATOR FOR A RANGE OF SET-UP PARAMETERS
# avoids re-opening buoydata files

TM_creator(0.2,1,60,1)

