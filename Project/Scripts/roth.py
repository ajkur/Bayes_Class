from __future__ import division
import numpy as np

def flameSpread(sigma=2054., bulk=1.217, hoc=8000., moist=0.15, igFac=250, vel=393.7, height=5, mExt=0.3):
    # Calculate beta - packing ratio
    drybulk = bulk/(height*0.3048) # kg/m^3
    beta = drybulk/512.0

    # Calculate functions of sigma and beta
    A = 1 / (4.774*sigma**(0.1) - 7.27)
    B = 0.02526 * sigma**(0.54)
    C = 7.47 * np.exp(-0.133*sigma**(0.55))    
    E = 0.715 * np.exp(-0.000359*sigma)
    BetaOP = 3.348*sigma**(-0.8189)
    gamMax = sigma**(1.5) / (495 + 0.0595*sigma**(1.5))
    GAM = gamMax * (beta/BetaOP)**A * np.exp(A * (1 - beta/BetaOP))
    EP = np.exp((0.792 + 0.681*sigma**(0.5))*(beta + 0.1)) / (192 + 0.2595*sigma)
    ep = np.exp(-138/sigma)

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

    # Convert to m/s
    return spRate*0.00508

# Mixture of forest service guide and reasonable data for wind speed and grass height
# mps = flameSpread(sigma=2054, bulk=1.2, hoc=8000, igFac=250, moist=0.15, vel=393.7, height=5
# print mps
