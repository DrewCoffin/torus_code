set terminal jpeg
set output 'Browninterp.jpeg'
set multiplot layout 2,2 rowsfirst 
#set pm3d interpolate 2,2
set key off
set title "Brown profile effect on frequency"
# Graph 1
set xlabel "Amplitude"
set ylabel "L-shell"
set cblabel "Frequency (rad/day)"
plot 'Brown.dat' u 1:2:4 lc palette
# Graph 2
set xlabel "Amplitude"
set ylabel "FWHM"   
set cblabel "Frequency (rad/day)"
plot 'Brown.dat' u 1:3:4 lc palette
# Graph 3
set xlabel "L-shell"  
set ylabel "FWHM"   
set cblabel "Frequency (rad/day)"
plot 'Brown.dat' u 2:3:4 lc palette
unset multiplot
