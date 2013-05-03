from __future__ import division
import numpy as np

mcs = np.array([15, 15, 30, 15, 40, 40, 15, 30, 40, 15, 15, 40, 40, 
    15, 15, 40, 30, 15, 30, 15, 40, 40])/100.0

mu = np.mean(mcs)
var = np.var(mcs)

print 'Moisture Content:'
print 'alpha', (mu**2/var)
print 'beta', (mu/var)

sav = np.array([2200, 2000, 1500, 2000, 1800, 2200, 2000, 1500, 1800, 
    2000, 2000, 1800, 1800, 2000, 2000, 1600, 2000, 750, 750, 750, 750, 750])

mu = np.mean(sav)
var = np.var(sav)

z95 = 1.644854
z99 = 2.575829
mu = 2286.0
var = ((3658-mu)/z99)**2

print 'SAV:'
print 'alpha', (mu**2/var)
print 'beta', (mu/var)
print 'scale', (var/mu)
