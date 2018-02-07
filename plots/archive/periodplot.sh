#!/bin/bash

OBSDIR='home/dcoffin/2D_Model-master/plots/data/'
SPEC='sp'
PARA='DENS'
END='_1D.dat'
days = {50..200}

#Find maximum of each time step
for i in $( days ); do
     if i < 100;
         
 
#Read maximum to .dat file
sed 

#Plot
gnuplot periodplot.gnu
eog periodplot.jpeg
