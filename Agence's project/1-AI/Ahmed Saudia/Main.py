import numpy as np
import astropy.io.fits as fits
import matplotlib.pyplot as plt
# Set up some default matplotlib options
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['image.origin'] = 'lower'
plt.rcParams['image.cmap'] = 'viridis'


from astropy.io import fits
sp = fits.open("iris_l2_20190723_042506_3882010194_raster_t000_r00000.fits")

hd = sp[0].header
hd['OBS_DESC']

print(len(sp))
print(hd['NWIN'])

print('Window. Name      : wave start - wave end\n')
for i in range(hd['NWIN']):
    win = str(i + 1)
    print('{0}. {1:15}: {2:.2f} - {3:.2f} Å'
          ''.format(win, hd['TDESC' + win], hd['TWMIN' + win], hd['TWMAX' + win]))

sp[3].data.shape

from astropy.wcs import WCS
wcs = WCS(sp[3].header)
m_to_nm = 1e9  # convert wavelength to nm
nwave = sp[3].data.shape[2]
wavelength = wcs.all_pix2world(np.arange(nwave), [0.], [0.], 0)[0] * m_to_nm



newarray=np.average(sp[3].data,0)
newarray2=np.average(newarray,0)
print(np.shape(newarray))
print(np.shape(newarray2))

local_min = (np.diff((np.sign(np.diff(newarray2))))>0).nonzero()[0]+1
local_max = (np.diff((np.sign(np.diff(newarray2))))<0).nonzero()[0]+1
plt.plot(wavelength, newarray2)

plt.axis([279, 281, 0, 260])
plt.xlabel("Wavelength (nm)")
plt.ylabel("Intensity (DN)")
#y = newarray2[local_max]
#x=wavelength[local_max]
#final_x=[]
#final_y=[]

#for i in range(len(y)):
 #   if y[i] > 10 :
  #      final_x.append(x[i])
   #     final_y.append(y[i])
#final_x=np.array(final_x)
#final_y=np.array(final_y)
#plt.plot(final_x,final_y,'o',label="Local max")
plt.plot(wavelength[local_max],newarray2[local_max],'o',label="Local max")

plt.plot(wavelength[local_min],newarray2[local_min],'o',label="Local min")

plt.legend()
plt.show()
