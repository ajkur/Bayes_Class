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

# MC = arange(0.05, 0.5, .01)
# y_trace = []
# sigList = []
# hocList = []
# mExtList = []
# for modSig in m1.modSig.trace():
#     sigList.append(modSig)
# for hoc in m1.hoc.trace():
#     hocList.append(hoc)
# for mExt in m1.mExt.trace():
#     mExtList.append(mExt)

# for i in range(len(sigList)):
#     y = roth.flameSpread(sigma=sigList[i], bulk=data.meanBulk, hoc=hocList[i], moist=MC, mExt=mExtList[i])
#     pl.plot(R, y, color='gray', alpha=.75, zorder=-1)
#     y_trace.append(y)

# print y_trace