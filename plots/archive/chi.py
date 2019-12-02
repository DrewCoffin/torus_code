import pandas
import os
import copy
import matplotlib.pyplot as plt
import numpy

def transpose(array):
  return map(list, zip(*array)) 

def getData(E, sig):
  tmp=[]
  tmp=pandas.read_csv('Expected.dat', sep='\t', header=None)
  tmp=tmp.values
  tmp=transpose(tmp)
  E=tmp
  tmp=pandas.read_csv('Sigma.dat', sep='\t', header=None)
  tmp=tmp.values
  tmp=transpose(tmp)
  sig=tmp
#  print E, '\n'
#  print sig
  return [E, sig]

def getOutput(output,run):
  paths=[]
  day=150
  pathParams=[["elec", "DENS"], ["op", "MIXR"], ["o2p","MIXR"], ["sp","MIXR"], ["s2p","MIXR"], ["s3p","MIXR"], ["elec", "NL2_"], ["elec", "TEMP"]]
  for i in range(0,len(pathParams)):
    path="./"+run+"/"+pathParams[i][0]+"/"+pathParams[i][1]+"/"+pathParams[i][1]+pathParams[i][0]+"0"+str(day)+"rad.dat"
#    while(not os.path.isfile(path)):
#      day=day-1
#      path="./"+run+"/"+pathParams[i][0]+"/"+pathParams[i][1]+"/"+pathParams[i][1]+pathParams[i][0]+"0"+str(day)+"rad.dat"
#      if( day == 0 ): return 0
    if( not os.path.isfile(path) ): return 0
    paths.append(path)
#    print os.path.isfile(path)
#  print paths
  output.append([])
  for f in paths:
    data=pandas.read_csv(f, sep=' ', header=None)
    #print data
    data=data.values
    data=transpose(data) 
    output.append(data[1])
  output[0]=data[0]
  return 1    

def modifyOutput(output, O):
  for i in range(0, len(O)):
    for j in range(0, len(O[i])):
      k=j
      if i==len(O)-1: k=j+1
      O[i][len(O[i])-j-1]=output[i+1][k]    
  return O

def calculateChi(O, E, sig):
  chis=[]
  chi=0
  for i in range(0, len(O)):
    for j in range(0, len(O[i])-1):
      k=len(O[i])-1-j
      if not (i==len(O)-1 and j==0):
        chi=chi+(((O[i][k] - E[i][k])**2)/sig[i][k]**2)
    chis.append(chi)
  return chis

def output(s, salph, dll, dllalph, chis, filenames):
  for i in range(0, len(filenames)):
    out=open(filenames[i]+".dat", 'a')
    out.write(str(dll)+"e-7 ")
    out.write(str(dllalph)+" ")
    out.write(str(s)+"e28 ")
    out.write(str(salph)+" ")
    out.write(str(chis[i])) #+'\n')
    out.close()

def outputSpace(filenames):
  for i in range(0, len(filenames)):
    out=open(filenames[i]+".dat", 'a')
    out.write('\n')
    out.close()

E=[]
sig=[]
[E, sig]=getData(E, sig)
outputs=[]
filenames=["elecDens", "op", "o2p", "sp", "s2p", "s3p", "NL2", "elecTemp", "Tot"] 
#print(filenames)
for name in filenames: open(name+'.dat', 'w').close()
out=open("chi.dat", 'a')
with open("../../gatherData.py", 'r') as runfile:
  content = runfile.readlines()
s1 = content[35].strip('sourceArray=[').rstrip(']\n')
s = s1.split(',')
for i in range(len(s)):
  s[i] = float(s[i])
sAl1 = content[37].strip('sourceAlphaArray=[').rstrip(']\n')
salph = sAl1.split(',')
for i in range(len(salph)):
  salph[i] = float(salph[i])
dll1 = content[39].strip('dllArray=[').rstrip(']\n')
dll = dll1.split(',')
for i in range(len(dll)):
  dll[i] = float(dll[i])
dllAl1 = content[41].strip('dllAlphaArray=[').rstrip(']\n')
dllalph = dllAl1.split(',')
for i in range(len(dllalph)):
  dllalph[i] = float(dllalph[i])
#print(dllalph)
fhe1 = content[43].strip('fheArray=[').rstrip(']\n')
fhe = fhe1.split(',')
#print(fhe)
for i in range(len(fhe)):
  fhe[i] = float(fhe[i])
fheAl1 = content[45].strip('fheAlphaArray=[').rstrip(']\n')
fhealph = fheAl1.split(',')
fhealph = [3.5]
for i in range(len(fhealph)):
  fhealph[i] = float(fhealph[i])
#print(s)
#print(dll)
for i in range(0, len(s)) :
  for j in range(0, len(salph)) :
    for k in range(0,len(dll)):
      for l in range(0,len(dllalph)):
        for m in range(0,len(fhe)):
          for n in range(0,len(fhealph)):
            run='run-('+str(i)+', '+str(j)+', '+str(k)+', '+str(l)+', '+str(m)+', '+str(n)+')'
            if(not os.path.exists("./"+run)): print "BAD", run
#            print(E)
            O=copy.deepcopy(E)
            outputs=[]
#            print('deepcopy successful')
#    print(filenames)
            if(not getOutput(outputs, run)): print "BAD Location", run
            if(getOutput(outputs, run) and os.path.exists("./"+run)):
#      print(filenames)
#              print('output is ')
#              print(outputs)
#              print(O)
              O=modifyOutput(outputs, O) 
#              print(len(O[0]))
              chis=calculateChi(O, E, sig)
              chis.append((sum(chis)-chis[0])) #/83.0)
#      print(filenames)
#      print(chis)
#      print O, '\n', E, '\n', "+++++++++++++++++++++++++++++++++++++++++++++"
   #           print(s)
  #            print(dll)
#              print(chis)
 #             print(len(chis))
   #           print(filenames)
    #          print(len(filenames))
              output(s[i], salph[j], dll[k], dllalph[l], chis, filenames)
            outputSpace(filenames)
  #out=open("chi.dat", 'a')
  #out.write('\n')
  #out.close()

#os.popen("gnuplot plot.gnu")
