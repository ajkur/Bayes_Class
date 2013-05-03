from __future__ import division
import numpy as np

# Estimated point value for bulk density
metricBulk = np.array([1.087, 1.169, 1.318, 1.174, 1.279, 1.429, 1.358, 1.339, 1.322, 0.939, 0.973]) # kg/m^2
meanBulk = np.mean(metricBulk)

# Data with estimates
rates = np.array([1.89, 0.40, 0.27, 1.89, 0.74, 1.01, 0.90, 1.10, 1.92, 1.18, 0.70])

mcsper = np.array([13.26, 15.28, 16.24, 15.26, 17.87, 16.56, 14.54, 15.33, 18.26, 16.37, 13.07])
mcs = mcsper/100.0

# Data without estimates
nes_rates = np.array([1.89, 0.40, 0.27, 1.89, 0.74, 1.01, 0.90, 1.10, 1.18])

nes_mcsper = np.array([13.26, 15.28, 16.24, 15.26, 17.87, 16.56, 14.54, 15.33, 16.37])
nes_mcs = nes_mcsper/100.0

# Outliers
sSigma = np.var(mcs)**0.5
sMean = np.mean(mcs)
sOutliers = 0
for i in range(mcs.shape[0]):
    if abs(mcs[i] - sMean)/sSigma > 1.6:
        # print i
        sOutliers = sOutliers + 1
# print sOutliers


