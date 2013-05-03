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

modNum = 1

if modNum == 1:
    # Generate model and fit model
    vars = models.uniform_priors()
    m1 = mc.MCMC(vars)
    # m1.use_step_method(mc.AdaptiveMetropolis, [m1.modSig,m1.hoc,m1.mExt])
    m1.sample(iter=50000, burn=25000, thin=50)
    # m1.sample(iter=300, burn=50, thin=2) # Test run
    print m1.summary()
    print 'DIC=%f' % m1.dic

    # Plot resulting distributions and convergence diagnostics
    mc.Matplot.plot(m1, format='pdf', path='../Figures/mod_one', common_scale=False)

    # plot sp vs mc here
    pl.figure(figsize=(12,9))
    graphics.plot_spread_mc(m1)
    pl.savefig('../Figures/mod_one/spread_rate.pdf')


if modNum == 2:
    # Generate model and fit model
    vars = models.model_two()
    m2 = mc.MCMC(vars)
    # m2.use_step_method(mc.AdaptiveMetropolis, [m2.modSig,m2.hoc,m2.mExt])
    m2.sample(iter=50000, burn=25000, thin=50)
    # m2.sample(iter=300, burn=50, thin=2) # Test run
    print m2.summary()
    print 'DIC=%f' % m2.dic

    # Plot resulting distributions and convergence diagnostics
    mc.Matplot.plot(m2, format='pdf', path='../Figures/mod_two', common_scale=False)

    # plot sp vs mc here
    pl.figure(figsize=(12,9))
    graphics.plot_spread_mc(m2)
    pl.savefig('../Figures/mod_two/spread_rate.pdf')

if modNum == 3:
    # Generate model and fit model
    vars = models.model_three()
    m3 = mc.MCMC(vars)
    # m3.use_step_method(mc.AdaptiveMetropolis, [m3.modSig,m3.hoc,m3.mExt])
    m3.sample(iter=50000, burn=25000, thin=50)
    # m3.sample(iter=300, burn=50, thin=2) # Test run
    print m3.summary()
    print 'DIC=%f' % m3.dic

    # Plot resulting distributions and convergence diagnostics
    mc.Matplot.plot(m3, format='pdf', path='../Figures/mod_three', common_scale=False)

    # plot sp vs mc here
    pl.figure(figsize=(12,9))
    graphics.plot_spread_mc_shift(m3)
    pl.savefig('../Figures/mod_three/spread_rate.pdf')

if modNum == 4:
    # Generate model and fit model
    vars = models.model_four()
    m4 = mc.MCMC(vars)
    # m4.use_step_method(mc.AdaptiveMetropolis, [m4.modSig,m4.hoc,m4.mExt])
    m4.sample(iter=50000, burn=25000, thin=50)
    # m4.sample(iter=300, burn=50, thin=2) # Test run
    print m4.summary()
    print 'DIC=%f' % m4.dic

    # Plot resulting distributions and convergence diagnostics
    mc.Matplot.plot(m4, format='pdf', path='../Figures/mod_four', common_scale=False)

    # plot sp vs mc here
    pl.figure(figsize=(12,9))
    graphics.plot_spread_mc(m4)
    pl.savefig('../Figures/mod_four/spread_rate.pdf')

# Plot only scenario data and spread rates
pl.figure(figsize=(12,9))
graphics.plot_data()
pl.savefig('../Figures/data_rates.pdf')
