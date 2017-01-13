import numpy as np

dadt=0.4
ADT=np.arange(-2.0,2+dadt,dadt)

dx=1
lons=np.arange(0,360+dx,dx)
lats=np.arange(-90,90+dx,dx)

cell_no=(lats.size-1)*(lons.size-1)
print (lons.size-1)*(lats.size-1)
print (lons.size-1)*(lats.size-1)*(ADT.size-1)
print 

def adtlonlat2i(adt,dadt,lon,lat,res):
        adt=adt + 2
	lat=lat+90
        ix=int(lon/res)
        iy=int(lat/res)*(np.amax(lons)/res)
        return (int(adt/dadt)*cell_no) + ix+iy

def i2adtlonlat(i,res):
        adt=(i/cell_no)
        i=i%cell_no
        lon = res*(i%(np.amax(lons)/res))
        lat = res*(i/(np.amax(lons)/res))
        return lon, lat-90, (adt*dadt)-2

#print adtlonlat2i(-1.9,dadt,0.5,-89.5,dx)
#print adtlonlat2i(-1.5,dadt,0.5,-89.5,dx)
#print adtlonlat2i(1.9,dadt,359.5,89.5,dx)

for i in range((lats.size-1)*(lons.size-1)+1):
	print i, i2adtlonlat(i,dx)
