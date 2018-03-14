import numpy as np
import scipy.interpolate as ip
import matplotlib.pyplot as plt

read = np.genfromtxt('./Brown.dat', delimiter=', ', skiprows = 3)

a,l,w,f = read[:,0], read[:,1], read[:,2], read[:,3]

nca, ncl, ncw = 16, 10, 25

fig, axarr = plt.subplots(3,1, figsize=(14,3))

plt.subplot(131)
#plt.title('L-shell vs. amplitude')
plt.xlabel('Amplitude')
plt.ylabel('L-shell')
aw, lw, fw = a[nca+ncl:nca+ncl+ncw-1], l[nca+ncl:nca+ncl+ncw-1], f[nca+ncl:nca+ncl+ncw-1]
X1, Y1 = np.mgrid[min(aw)-0.2:max(aw)+0.2:100j, min(lw)-0.2:max(lw)+0.2:100j]
interp1 = ip.griddata((aw, lw), fw, (X1, Y1), method='cubic')
plt.imshow(interp1.T, extent=(min(aw)-1,max(aw)+1,min(lw)-1,max(lw)+1), origin='lower')

plt.subplot(132)
#plt.title('FWHM vs. amplitude')
plt.xlabel('Amplitude')
plt.ylabel('FWHM')   
al, wl, fl = a[nca:nca+ncl-1], w[nca:nca+ncl-1], f[nca:nca+ncl-1]
X2, Y2 = np.mgrid[min(al)-0.2:max(al)+0.2:100j, min(wl)-0.2:max(wl)+0.2:100j]
interp2 = ip.griddata((al, wl), fl, (X2, Y2), method='cubic')
plt.imshow(interp2.T, extent=(min(al)-1,max(al)+1,min(wl)-1,max(wl)+1), origin='lower')

plt.subplot(133)
#plt.title('FWHM vs. L-shell')
plt.xlabel('L-shell')  
plt.ylabel('FWHM')   
la, wa, fa = l[:nca-1], w[:nca-1], f[:nca-1]
X3, Y3 = np.mgrid[min(la)-0.2:max(la)+0.2:100j, min(wa)-0.2:max(wa)+0.2:100j]
interp3 = ip.griddata((la, wa), fa, (X3, Y3), method='cubic')
plt.imshow(interp3.T, extent=(min(la)-1,max(la)+1,min(wa)-1,max(wa)+1), origin='lower')

plt.tight_layout()

fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.88, 0.15, 0.03, 0.7])
cbar = plt.colorbar(cax=cbar_ax)
cbar.set_label('Frequency (rad per day)')

plt.savefig('Brown.png')
plt.show()
