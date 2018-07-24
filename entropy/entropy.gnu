set terminal png
set output 'entropy.png'
set ylabel 'Entropy'         
set xlabel 'Radial distance'
set autoscale
set title "Entropy radial profiles"        
set key outside
plot 'sp.dat' using 3:2 title 'S+', \
     's2p.dat' using 3:2 title 'S2+', \
     's3p.dat' using 3:2 title 'S3+', \
     'op.dat' using 3:2 title 'O+', \
     'o2p.dat' using 3:2 title 'O2+', \
     'elec.dat' using 3:2 title 'e-' #, \
     #'tot.dat' using 3:2 title 'Total'
