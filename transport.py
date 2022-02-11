import os 
import sys
import math
import matplotlib.pyplot as plt


#def Transport(path, dll0, s):
dayint=int(sys.argv[1])

zeroes=int(3 - math.floor(math.log10(dayint))) #file naming

for i in range(0, zeroes):
  day="0"+str(dayint)

target="plots/data/elec/NL2_/NL2_elec"+str(day)+"rad.dat"
#  if( not os.path.isfile(target)): return 0
while( not os.path.isfile(target)): #In case dayint is past the end of the run
  dayint=dayint-1
  for i in range(0, zeroes):
    day="0"+str(dayint)
  target="plots/data/elec/NL2_/NL2_elec"+str(day)+"rad.dat"
  #target="NL2_elec"+str(day)+"rad.dat"

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

#print dll

dr=rarray[2]-rarray[1]
#print rarray
#print narray
#print dr

values=[0]
for i in range(1,len(rarray)):
  values.append(dll[i]*((narray[i]-narray[i-1])/dr)/(rarray[i]**2))
#This is the term in brackets in the Copper formula
values[0]=values[1]

#print values

transport=[]

#ntot=[] #This function is redundant
#for i in range(0, len(narray)):
#  tot=0.0
#  for j in range(i):
#    tot=tot+(narray[j]/rarray[j]**2)#*dr
#  ntot.append(tot)

#print narray
#print ntot

for i in range(0,len(rarray)):
  #outer "derivative" - actually discrete sum
  transport.append(-dr*(narray[i]/(rarray[i]**2))/(values[i]))
  transport[i] /= 86400.0 #normalize to days
  
ttot=[0.0]
tauarr=[0.0]
for i in range(1, len(narray)):
  tot=0.0
  for j in range(i):
    tot=tot+transport[j]#*(rarray[j+1]-rarray[j]) #Extraneous dr factor
    tau=transport[j]#*(rarray[j+1]-rarray[j])
  ttot.append(tot)
  tauarr.append(tau)

print ttot
  
plt.plot(rarray, ttot)
plt.xlabel('Radial distance (Rj)')
plt.ylabel('Time for transport (days)')
plt.show()
