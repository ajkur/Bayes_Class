from __future__ import division
import numpy as np
import matplotlib
matplotlib.use("Agg")
from pylab import *
import pymc as mc
import models

# Generate model and fit model
vars = models.uniform_priors()
m1 = mc.MCMC(vars)
m1.use_step_method(mc.AdaptiveMetropolis, [m1.modSig,m1.hoc,m1.mExt])
m1.sample(iter=50000, burn=25000, thin=50)
print m1.summary()

# Plot resulting distributions and convergence diagnostics
mc.Matplot.plot(m1, format='pdf', path='../Figures/diffuse', common_scale=False)

# plot sp vs mc here