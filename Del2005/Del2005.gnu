set terminal png 
set output '3.6exp/s3pMIXR.png'    
set key off
set title 'S3+ Mixing ratio' 
set ylabel 'Mixing Ratio'
set xlabel 'Radial Distance (RJ)'
set grid ytics
set xrange [6:9]
set grid xtics
plot '3.6exp/s3pMIXR.dat' using 3:2 with lines
