from __future__ import division
import numpy as np
import math as m

def flameSpread(sigma, beta, moist, hoc, igFac, vel, height, mExt=0.3):
    # Calculate functions of sigma and beta
    A = 1 / (4.774*sigma**(0.1) - 7.27)
    B = 0.02526 * sigma**(0.54)
    C = 7.47 * m.exp(-0.133*sigma**(0.55))    
    E = 0.715 * m.exp(-0.000359*sigma)
    BetaOP = 3.348*sigma**(-0.8189)
    gamMax = sigma**(1.5) / (495 + 0.0595*sigma**(1.5))
    GAM = gamMax * (beta/BetaOP)**A * m.exp(A * (1 - beta/BetaOP))
    EP = m.exp((0.792 + 0.681*sigma**(0.5))*(beta + 0.1)) / (192 + 0.2595*sigma)
    ep = m.exp(-138/sigma)

    # Wind factor
    phiW = C * vel**B * (beta/BetaOP)**(-E)

    # Moisture damping
    MM = moist/mExt
    etaMoist = 1 - 2.59*MM + 5.11*MM**2 - 3.52*MM**3

    # Heat of preignition
    Qig = igFac + moist*1116.0

    # Mineral Coefficient
    minCoef = 0.395

    # Spread rate
    spRate = (1 + phiW) * EP * GAM * minCoef * hoc * height * etaMoist / (ep * Qig)
    return spRate

# Mixture of forest service guide and reasonable data for wind speed and grass height
fpm = flameSpread(sigma=2054, beta=0.00143, moist=0.15, hoc=8000, igFac=250, vel=880, height=3)
mps = fpm*0.00508
print mps
