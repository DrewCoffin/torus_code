#Syntax:

#Three system arguments. First two specify the day range.
#Third sysarg is whether the run is completed (1) or in process (0).
#Example call is: python mixplot.py 50 250 0 (plot days 50 to 250 of the currently running data).

#Read data files
import os
import sys
import numpy as np
import math as m
import matplotlib.pyplot as plt

def getdim():
     with open("do", 'r') as runfile:
          content = runfile.readlines()
     lng = int(content[2].strip('lng=').rstrip('\n'))
     rad = int(content[3].strip('rad=').rstrip('\n'))
     return lng, rad

def numzeros(i):
     if i < 1000:
          base =  m.log(i)/m.log(10)
          return 3 - int(base)
     else: 
          return 0

def getval(output, days, spec, runloc, dim, runstat): #finds the max mixing ratio per day
     longval = []
     for i in days:
          dayarr = []
          if( runstat ):
               path = './' + runloc + '/' + spec + '/MIXR/MIXR' + spec + numzeros(i)*'0' + str(i) + '_3D.dat'
          else:
               path = './MIXR' + spec + numzeros(i)*'0' + str(i) + '_3D.dat'
          if( not os.path.isfile(path) ): return 0
          with open(path) as datafile:
               data = [next(datafile) for x in xrange(dim)] #reads first dim-th lines
               datalines = [data[i].split() for i in range(len(data))]
               for j in range(len(datalines)):
                    dayarr.append(float(datalines[j][1])) #List of all ratios per day
          indval = dayarr.index(max(dayarr)) #azimuthal bin of peak ratio
          longval.append(360./dim*indval) #converts bin to degrees
     return longval

lng, rad = getdim()
days = range(int(sys.argv[1]), int(sys.argv[2]))
output = []
specs = ['sp', 's3p'] #'s2p', 's3p', 'op', 'o2p', 'elec']
output = [getval(output, days, specs[i], 'plots/data', lng, int(sys.argv[3])) for i in range(len(specs))]
#print output

#Plot peak angle

#plt.subplot(231)
plt.title('Peak Mixing ratio location')      
plt.xlabel('Days')
plt.ylabel('System III Angle')
plt.scatter(days, output[0], marker='^', c = 'red', label = specs[0])
plt.scatter(days, output[1], marker='o', c = 'blue', label = specs[1])
plt.legend()
plt.show()
