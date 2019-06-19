import os
import sys
import numpy as np
import math as m

Mdot = input("Mass loading (kg/s): ")
SigP = input("Pedersen conductivity (mho): ")

L0 = 6 #initial L-shell
delL = 1 #change in L-shell
vtan = 57000 #differential velocity between Io and magnetic field (m/s)
Bj = 7.77*10**-4 #equatorial magnetic field of Jupiter (T)
Rp = 71492000 #equatorial radius of Jupiter (m)

denom = 4*m.pi*SigP*Rp**3*Bj**2*(1-1/L0)**(1./2)*delL

delom = (vtan*Mdot*L0**4)/denom

orbcirc = 2*m.pi*6*Rp/1000

print(orbcirc*delom)
