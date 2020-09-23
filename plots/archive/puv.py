import os

lineNum=34

def getPuv(folder):
  runlog=open("./"+run+"/runlog", 'r')
  lNum=0
  junk=""
  Puv=''
  for line in runlog:
    lNum=lNum+1
    if(lNum == lineNum):
      s=line.rsplit('\n', 1)
#      print s
      while(Puv==''):
       s=s[0].rsplit(' ', 1)
       Puv=s[1]
#       print s
  if(lNum < lineNum):
#    print "ERROR:", run, " only has ", lNum, " lines."
    return 0
  return str(float(Puv))

open("Puv.dat", 'w').close()
out=open("Puv.dat", 'a')
with open("../../gatherData.py", 'r') as runfile:
  content = runfile.readlines()
s1=content[35].strip('sourceArray=[').rstrip(']\n')
s=s1.split(', ')
for i in range(len(s)):
  s[i] = float(s[i])
dll1=content[40].strip('dllArray=[').rstrip(']\n')
dll=dll1.split(', ')
for i in range(len(dll)):
  dll[i] = float(dll[i])
for i in range(0, len(dll)) :
  for j in range(0, len(s)) : #take from gatherData.py that generated the data
    run="s="+str(s[j])+":dll="+str(dll[i])
    if(not os.path.exists("./"+run)): print "BAD", run
    if(os.path.exists("./"+run)):
      Puv=getPuv(run)
      if( Puv > 0.0 ): out.write(str(dll[i])+"e-7 " + str(s[j])+"e28 " + Puv+'\n')
#      print dll[i], s[j], Puv
  out.write('\n')
out.close()

os.popen("gnuplot plotPuv.gnu")
