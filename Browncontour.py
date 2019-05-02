import numpy as np
import scipy.interpolate as ip
import matplotlib.pyplot as plt

read = np.genfromtxt('./Brown.dat', delimiter=', ', skiprows = 3)

a,l,w,f = read[:,0], read[:,1], read[:,2], read[:,3]
nca, ncl, ncw = 22, 17, 32

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3) #, figsize=(10,3))

#plt.subplot(131)
ax1.set_title('FWHM of 0.8 Rj')
ax1.set_xlabel('Amplitude (- km/s)')
ax1.set_ylabel('L-shell (Rj)')
aw, lw, fw = a[nca+ncl:nca+ncl+ncw], l[nca+ncl:nca+ncl+ncw], f[nca+ncl:nca+ncl+ncw]
#print(lw)
#X1, Y1 = np.mgrid[min(aw):max(aw):100j, min(lw):max(lw):100j]
ax1.tricontour(aw, lw, fw) #, levels=10)
concol1 = ax1.tricontourf(aw, lw, fw)
#fig.colorbar(concol1, ax=ax1)
ax1.plot(aw, lw, ' ')
ax1.set_xlim(min(aw),max(aw))
ax1.set_ylim(min(lw),max(lw))

#plt.subplot(132)
ax2.set_title('L-shell of 7.2 Rj')
ax2.set_xlabel('Amplitude (- km/s)')
ax2.set_ylabel('FWHM (Rj)')   
al, wl, fl = a[nca:nca+ncl], w[nca:nca+ncl], f[nca:nca+ncl]
ax2.tricontour(al, wl, fl) #, levels=10)
concol2 = ax2.tricontourf(al, wl, fl)
#fig.colorbar(concol2, ax=ax2)
ax2.plot(al, wl, ' ') 
ax2.set_xlim(min(al),max(al))
ax2.set_ylim(min(wl),max(wl))

#plt.subplot(133)
ax3.set_title('Amplitude of 3.0 km/s')
ax3.set_xlabel('L-shell (Rj)')  
ax3.set_ylabel('FWHM (Rj)')   
la, wa, fa = l[:nca], w[:nca], f[:nca]
#print(la, wa, fa)
ax3.tricontour(la, wa, fa) #, levels=10)
concol3 = ax3.tricontourf(la, wa, fa)
#fig.colorbar(concol3, ax=ax3)
ax3.plot(la, wa, ' ') 
ax3.set_xlim(min(la),max(la))
ax3.set_ylim(min(wa),max(wa))

plt.tight_layout()

fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.75])
cbar = fig.colorbar(concol3, cax=cbar_ax)
cbar.set_label('Frequency (rad per day)')

plt.savefig('Browncontour.png')
plt.show()
