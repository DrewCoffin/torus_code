import numpy as np
import scipy.interpolate as itp
import matplotlib.pyplot as plt
import matplotlib as mpl

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
#print(a)

fig, axarr = plt.subplots(1,3, figsize=(10,3))

plt.subplot(131)
plt.title('Amplitude vs. L-shell')
plt.scatter(a, l, c=f)
#plt.colorbar()

plt.subplot(132)
plt.title('Amplitude vs. FWHM')
plt.scatter(a, w, c=f)
#plt.colorbar()

plt.subplot(133)
plt.title('L-shell vs. FWHM')
plt.scatter(l, w, c=f)

fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.88, 0.15, 0.03, 0.7])
cbar = plt.colorbar(cax=cbar_ax)
cbar.set_label('Frequency (rad per day)')

plt.show()
