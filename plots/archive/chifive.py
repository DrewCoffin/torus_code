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
  day=100
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
    if( day == 180 ): print data[1]
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

def output(s, dll, chis, filenames):
  for i in range(0, len(filenames)):
    out=open(filenames[i]+".dat", 'a')
    out.write(str(dll)+"e-7 ")
    out.write(str(s)+"e28 ")
    out.write(str(chis[i])+'\n')
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
for name in filenames: open(name+'.dat', 'w').close()
out=open("chi.dat", 'a')
with open("../../gatherData.py", 'r') as runfile:
  content = runfile.readlines() #first line is content[0]
s1 = content[36].strip('sourceArray=[').rstrip(']\n')
s = s1.split(',')
print(s)
sAl1 = content[38].strip('sourceAlphaArray=[').rstrip(']\n')
salph = sAl1.split(',')
dll1 = content[41].strip('dllArray=[').rstrip(']\n')
dll = dll1.split(',')
dllAl1 = content[43].strip('dllAlphaArray=[').rstrip(']\n')
dllalph = dll1.split(',')
fhe1 = content[45].strip('fheArray=[').rstrip(']\n')
fhe = fhe1.split(',')
fheAl1 = content[47].strip('fheAlphaArray=[').rstrip(']\n')
fhealph = fheAl1.split(',')
print(len(fhealph))
for i in range(0, len(s)) :
  for j in range(0, len(salph)) :
    for k in range(0,len(dll)):
      for l in range(0,len(dllalph)):
        for m in range(0,len(fhe)):
          for n in range(0,len(fhealph)):
            run='run-('+str(i)+', '+str(j)+', '+str(k)+', '+str(l)+', '+str(m)+', '+str(n)+')'
            #run="s="+str(s[j])+":dll="+str(dll[i])
            if(not os.path.exists("./"+run)): print "BAD", run
#            if(os.path.exists("./"+run+"/s3p/MIXR/MIXRs3p0200rad.dat")): print "GOOD RUN", run
            O=copy.deepcopy(E)
            outputs=[]
#            print O
            print len(O)
            print len(O[1])
            print len(E)
            if(getOutput(outputs, run) and os.path.exists("./"+run)):
              print len(outputs[0])
              O=modifyOutput(outputs, O) 
#              print len(O)
#              print len(E)
#              print len(sig)
              chis=calculateChi(O, E, sig)
              print chis
              print len(chis)
              chis.append((sum(chis)-chis[0])) #/83.0)
  #            print chis
              #print O, '\n', E, '\n', "+++++++++++++++++++++++++++++++++++++++++++++"
              output(s[j], dll[i], chis, filenames)
            outputSpace(filenames)
  #           out=open("chi.dat", 'a')
  #          out.write('\n')
  #          out.close()

os.popen("gnuplot plot.gnu")
#print x
#print y
#print z
#makePlot(x, y, z) #<-BROKEN
    #GetData(E, sig)
    #GetOutput(output)
    #ModifyOutput(output, O)
    #calculate chi squared(O, E, sig)
    #output chi squared, s, dll in proper order for plotting
#plot heatmap of chi squared
