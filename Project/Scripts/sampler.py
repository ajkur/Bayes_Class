from __future__ import division
import numpy as np
import matplotlib
matplotlib.use("Agg")
import pylab as pl
import pymc as mc
import graphics
import models
import roth
import data

# Generate model and fit model
vars = models.uniform_priors()
m1 = mc.MCMC(vars)
# m1.use_step_method(mc.AdaptiveMetropolis, [m1.modSig,m1.hoc,m1.mExt])
m1.sample(iter=50000, burn=25000, thin=50)
# m1.sample(iter=300, burn=50, thin=2) # Test run
print m1.summary()

# Plot resulting distributions and convergence diagnostics
mc.Matplot.plot(m1, format='pdf', path='../Figures/diffuse', common_scale=False)

# plot sp vs mc here
pl.figure(figsize=(12,9))
graphics.plot_spread_mc(m1)
pl.savefig('../Figures/spread_rate.pdf')
pl.figure(figsize=(12,9))
graphics.plot_data()
pl.savefig('../Figures/data_rates.pdf')

# # Generate model and fit model
# vars = models.no_moist_data()
# m2 = mc.MCMC(vars)
# # m2.use_step_method(mc.AdaptiveMetropolis, [m2.modSig,m2.hoc,m2.mExt])
# m2.sample(iter=50000, burn=25000, thin=50)
# # m2.sample(iter=300, burn=50, thin=2) # Test run
# print m2.summary()

# # Plot resulting distributions and convergence diagnostics
# mc.Matplot.plot(m2, format='pdf', path='../Figures/no_moist', common_scale=False)

# # plot sp vs mc here
# pl.figure(figsize=(12,9))
# graphics.plot_spread_mc_nomext(m2)
# pl.savefig('../Figures/spread_rate_nm.pdf')

