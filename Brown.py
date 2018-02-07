import numpy as np
import scipy.interpolate as ip
import matplotlib.pyplot as plt

read = np.loadtxt('./Brown.dat', delimiter=', ', skiprows = 1)
a = []
l = []
w = []
f = []
for i in range(len(read)):
	a.append(read[i][0])
        l.append(read[i][1])
        w.append(read[i][2])
        f.append(read[i][3])

a = np.array(a)
l = np.array(l)
w = np.array(w)
f = np.array(f)

fig, axarr = plt.subplots(1,3, figsize=(10,3))

plt.subplot(131)
plt.title('L-shell vs. amplitude')
X1, Y1 = np.mgrid[min(a)-1:max(a)+1:100j, min(l)-1:max(l)+1:100j]
interp1 = ip.griddata((a, l), f, (X1, Y1), method='cubic')
plt.imshow(interp1.T, extent=(min(a)-1,max(a)+1,min(l)-1,max(l)+1), origin='lower')

plt.subplot(132)
plt.title('FWHM vs. amplitude')
X2, Y2 = np.mgrid[min(a)-1:max(a)+1:100j, min(w)-1:max(w)+1:100j]
interp2 = ip.griddata((a, w), f, (X2, Y2), method='cubic')
plt.imshow(interp2.T, extent=(min(a)-1,max(a)+1,min(w)-1,max(w)+1), origin='lower')

plt.subplot(133)
plt.title('FWHM vs. L-shell')
X3, Y3 = np.mgrid[min(l)-1:max(l)+1:100j, min(w)-1:max(w)+1:100j]
interp3 = ip.griddata((l, w), f, (X3, Y3), method='cubic')
plt.imshow(interp3.T, extent=(min(l)-1,max(l)+1,min(w)-1,max(w)+1), origin='lower')

fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.88, 0.15, 0.03, 0.7])
cbar = plt.colorbar(cax=cbar_ax)
cbar.set_label('Frequency (rad per day)')

plt.savefig('Brown.svg')
plt.show()
