set terminal png 
set output 'Copp2016/Copp2016.png'
set key outside
set title 'Mixing ratio comparisons' 
set ylabel 'Mixing Ratio'
set xlabel 'Radial Distance (RJ)'
set grid ytics
set logscale y
set xrange [6:9]
set yrange [0.01:1]
set grid xtics

plot 'Copp2016/opMIXR.dat' using 3:2 lt rgb "blue"  title 'O+ theory', \
     'opCass.dat' using 1:2:3 with errorbars lt rgb "blue" title 'O+ Cassini', \
     'Copp2016/o2pMIXR.dat' using 3:2 lt rgb "green" title 'O2+ theory', \
     'o2pCass.dat' using 1:2:3 with errorbars lt rgb "green" title 'O2+ Cassini', \
     'Copp2016/spMIXR.dat' using 3:2 lt rgb "black" title 'S+ theory', \
     'spCass.dat' using 1:2:3 with errorbars lt rgb "black" title 'S+ Cassini', \
     'Copp2016/s2pMIXR.dat' using 3:2 lt rgb "red" title 'S2+ theory', \
     's2pCass.dat' using 1:2:3 with errorbars lt rgb "red" title 'S2+ Cassini', \
     'Copp2016/s3pMIXR.dat' using 3:2 lt rgb "cyan" title 'S3+ theory', \
     's3pCass.dat' using 1:2:3 with errorbars lt rgb "cyan" title 'S3+ Cassini'

