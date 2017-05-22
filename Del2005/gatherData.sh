#!/bin/bash

spec=( sp s2p s3p op o2p )

cd ../plots/data/elec/MIXR

a="MIXR"
b="0250_3D.dat"
c="MIXR.dat"

for i in "${spec[@]}"
do
     cd ../../$i/MIXR
     awk "NR % ($1 +2) == 1" $a$i$b > $HOME/2D_Model-master/Del2005/$i$c
done

cd $HOME/2D_Model-master/Del2005/
