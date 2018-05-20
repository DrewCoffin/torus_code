#Read data files
import os
import sys
import csv
import math as m

def getdim():
     with open("do", 'r') as runfile:
          content = runfile.readlines()
     lng = int(content[2].strip('lng=').rstrip('\n'))
     rad = int(content[3].strip('rad=').rstrip('\n'))
     return lng, rad

def numzeros(i):
    base =  m.log(i)/m.log(10)
    return 3 - int(base)

def getdens(output, spec, runloc, dim): 
     maxday = 20
     denvals = []
     for i in range(1, maxday):
          dayden = []
          path = './' + runloc + '/' + spec + '/DENS/DENS' + spec + numzeros(i)*'0' + str(i) + '_3D.dat'
          if( not os.path.isfile(path) ): return 0
          with open(path) as datafile:
               data = [next(datafile) for x in xrange(dim)]  
               datalines = [data[i].split() for i in range(len(data))]
               for j in range(len(datalines)):
                    dayden.append(float(datalines[j][1])) 
          denvals.append(max(dayden))
     return denvals  

lng, rad = getdim()
#print lng, rad
output = []
specs = ['sp', 's2p', 's3p', 'op', 'o2p', 'elec']
output = [getdens(output, specs[i], 'plots/data', lng) for i in range(len(specs))]
print output

#Plot max density array
