#!/bin/bash

mv DENS*.dat plots/.
mv MIXR*.dat plots/.
mv TEMP*.dat plots/.
#mv INTS*.dat plots/.  
mv NL2_*.dat plots/.
mv LOAD*.dat plots/.
mv MOUT*.dat plots/.
mv TMSS*.dat plots/.
mv VSUB*.dat plots/.
#mv intensity*.dat plots/.  
mv PUV*.dat plots/.
mv FEH*.dat plots/.
mv ENTR*.dat plots/.
#mv ERAT*.dat plots/.

cd plots

  python radData.py $1 $2

  mv DENS*.dat data/.
  mv MIXR*.dat data/.
  mv TEMP*.dat data/.
#  mv INTS*.dat data/.
  mv NL2_*.dat data/.
  mv LOAD*.dat data/.
  mv MOUT*.dat data/.
  mv TMSS*.dat data/.
  mv PUV*.dat data/.
  mv VSUB*.dat data/.
  mv FEH*.dat data/.
  mv ENTR*.dat data/.
 # mv ERAT*.dat data/.
#  rm intensity*.dat

  ./organize.sh

cd ..
