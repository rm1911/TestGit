import numpy as np

def lonlat2i(lon,lat,res):
	lat=lat+90
	ix=int(lon/res)
	iy=int(lat/res)*(360/res)
	return ix+iy

#print lonlat2i(1.5, -89.5, 1)

#for b in np.arange(-89.5,90.5,1):
#	for a in np.arange(0.5,360.5,1):
#		print a,b, lonlat2i(a,b,2)


def i2lonlat(i,res):
	return res*(i%(360/res)),res*(i/(360/res))-90

#for i in range(0,362,1):
#	print i, i2lonlat(i,2)

print lonlat2i(30, -30, 2)
print i2lonlat(5415,2)
