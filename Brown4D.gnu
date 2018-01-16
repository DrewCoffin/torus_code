set terminal jpeg
set output 'Browncontour.jpeg'
set key off
set title "Brown subcorotation profile on System IV frequency"
# set autoscale cbfix
set dgrid3d
set contour
set xlabel "Amplitude"
set ylabel "L-shell"
set zlabel "FWHM"
set cblabel "Frequency"
splot 'Brown.dat' u 1:2:3:4 lc palette
