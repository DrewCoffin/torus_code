set terminal png 
set output 'snuexp/o2pMIXR.png'    
set key outside
set title 'O2+ Mixing ratio' 
set ylabel 'Mixing Ratio'
set xlabel 'Radial Distance (RJ)'
set grid ytics
set logscale y
set xrange [6:9]
set yrange [0.01:1]
set grid xtics
plot 'snuexp/4.0exp/o2pMIXR.dat' using 3:2 title '4.0 S_n exp', \
     'snuexp/12.0exp/o2pMIXR.dat' using 3:2 title '12.0 S_n exp', \
     'snuexp/20.0exp/o2pMIXR.dat' using 3:2 title '20.0 S_n exp', \
     'o2pmix.dat' using 1:2:3 with errorbars title 'Cassini'

