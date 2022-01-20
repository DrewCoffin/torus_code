import os 
import sys
import math
import matplotlib.pyplot as plt


#def Transport(path, dll0, s):
dayint=int(sys.argv[1])

zeroes=int(3 - math.floor(math.log10(dayint)))

for i in range(0, zeroes):
  day="0"+str(dayint)

target="NL2_elec"+str(day)+"rad.dat"
#  if( not os.path.isfile(target)): return 0
while( not os.path.isfile(target)):
  dayint=dayint-1
  for i in range(0, zeroes):
    day="0"+str(dayint)
  target="NL2_elec"+str(day)+"rad.dat"

infile = open(target, "r")

inputs=open("./inputs.dat", "r")

rarray=[]
narray=[]
for line in infile:
  [rdist, nl2]=line.split()
  rarray.append(float(rdist))
  narray.append(float(nl2))

infile.close()

dll0 = 3.5e-7
dlla = 4.5
dll=[]
for r in rarray:
  dll.append(dll0*(r/6.0)**dlla)

dr=rarray[2]-rarray[1]
#print rarray
#print narray
#print dr

values=[0]
for i in range(1,len(rarray)):
  values.append(dll[i]*((narray[i]-narray[i-1])/dr)/(rarray[i]**2))

values[0]=values[1]

#print values

transport=[]

ntot=[]
for i in range(0, len(narray)):
  tot=0.0
  for j in range(i):
    tot=tot+(narray[j]/rarray[j]**2)*dr
  ntot.append(tot)

#print narray
#print ntot

for i in range(0,len(rarray)):
  transport.append(-dr*narray[i]/(rarray[i]**2)/86400.0/values[i])
  
ttot=[0.0]
tauarr=[0.0]
for i in range(1, len(narray)):
  tot=0.0
  for j in range(i):
    tot=tot+transport[j]*(rarray[j+1]-rarray[j])
    tau=transport[j]*(rarray[j+1]-rarray[j])
  ttot.append(tot)
  tauarr.append(tau)

print ttot
  
plt.plot(rarray, tauarr)
plt.xlabel('Radial distance (Rj)')
plt.ylabel('Time for transport (days)')
plt.show()
