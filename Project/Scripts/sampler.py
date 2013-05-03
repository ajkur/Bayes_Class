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

dicList = []
for modNum in range(4,5):

    if modNum == 1:
        # Generate model and fit model
        vars = models.uniform_priors()
        m1 = mc.MCMC(vars)
        # m1.use_step_method(mc.AdaptiveMetropolis, [m1.modSig,m1.hoc,m1.mExt])
        m1.sample(iter=83000, burn=8000, thin=75)
        # m1.sample(iter=10000, burn=0, thin=1) # Test run    
        # print m1.summary()
        # print 'DIC=%f' % m1.dic
        dicList.append(m1.dic)

        # Plot resulting distributions and convergence diagnostics
        mc.Matplot.plot(m1, format='pdf', path='../Figures/mod_one', common_scale=False)

        # plot sp vs mc here
        pl.figure(figsize=(12,9))
        graphics.plot_spread_mc(m1)
        pl.savefig('../Figures/mod_one/spread_rate.pdf')

        # Write posterior output
        m1.write_csv("../Figures/mod_one/reg_out.csv")

        D = mc.discrepancy(1/(1+np.exp(-data.rates)), 1/(1+np.exp(-m1.y_sim.trace())), 1/(1+np.exp(-m1.y_mean.trace())))
        mc.Matplot.discrepancy_plot(D, name='D', format='pdf', path='../Figures/mod_one', report_p=True)


    if modNum == 2:
        # Generate model and fit model
        vars = models.model_two()
        m2 = mc.MCMC(vars)
        # m2.use_step_method(mc.AdaptiveMetropolis, [m2.modSig,m2.hoc,m2.mExt])
        m2.sample(iter=56000, burn=6000, thin=50)
        # m2.sample(iter=10000, burn=0, thin=1) # Test run
        # print m2.summary()
        print 'DIC=%f' % m2.dic
        dicList.append(m2.dic)

        # Plot resulting distributions and convergence diagnostics
        mc.Matplot.plot(m2, format='pdf', path='../Figures/mod_two', common_scale=False)

        # plot sp vs mc here
        pl.figure(figsize=(12,9))
        graphics.plot_spread_mc(m2)
        pl.savefig('../Figures/mod_two/spread_rate.pdf')

        # Write posterior output
        m2.write_csv("../Figures/mod_two/reg_out.csv")

        D = mc.discrepancy(1/(1+np.exp(-data.rates)), 1/(1+np.exp(-m2.y_sim.trace())), 1/(1+np.exp(-m2.y_mean.trace())))
        mc.Matplot.discrepancy_plot(D, name='D', format='pdf', path='../Figures/mod_two', report_p=True)

        # Check for outliers
        # simList = []
        # for y_sim in m2.y_sim.trace():
        #     simList.append(y_sim)
        # meanList = []
        # for y_mean in m2.y_mean.trace():
        #     meanList.append(y_mean)
        # sigmaList = []
        # for sigma in m2.sigma.trace():
        #     sigmaList.append(sigma)
        # outArr = np.zeros(len(simList))
        # for i in range(len(simList)):
        #     outliers = 0
        #     for j in range(len(simList[i])):
        #         if abs(simList[i][j] - meanList[i][j])/sigmaList[i] > 1.6:
        #             outliers = outliers + 1
        #     outArr[i] = outliers
        # print np.mean(outArr)
        # print data.sOutliers

    if modNum == 3:
        # Generate model and fit model
        vars = models.model_three()
        m3 = mc.MCMC(vars)
        # m3.use_step_method(mc.AdaptiveMetropolis, [m3.modSig,m3.hoc,m3.mExt])
        m3.sample(iter=27000, burn=2000, thin=25)
        # m3.sample(iter=10000, burn=0, thin=1) # Test run
        # print m3.summary()
        # print 'DIC=%f' % m3.dic
        dicList.append(m3.dic)

        # Plot resulting distributions and convergence diagnostics
        mc.Matplot.plot(m3, format='pdf', path='../Figures/mod_three', common_scale=False)

        # plot sp vs mc here
        pl.figure(figsize=(12,9))
        graphics.plot_spread_mc_shift(m3)
        pl.savefig('../Figures/mod_three/spread_rate.pdf')

        # Write posterior output
        m3.write_csv("../Figures/mod_three/reg_out.csv")

        D = mc.discrepancy(1/(1+np.exp(-data.rates)), 1/(1+np.exp(-m3.y_sim.trace())), 1/(1+np.exp(-m3.y_mean.trace())))
        mc.Matplot.discrepancy_plot(D, name='D', format='pdf', path='../Figures/mod_three', report_p=True)

    if modNum == 4:
        # Generate model and fit model
        vars = models.model_four()
        m4 = mc.MCMC(vars)
        # m4.use_step_method(mc.AdaptiveMetropolis, [m4.modSig,m4.hoc,m4.mExt])
        m4.sample(iter=56000, burn=6000, thin=50)
        # m4.sample(iter=10000, burn=0, thin=1) # Test run
        # print m4.summary()
        # print 'DIC=%f' % m4.dic
        dicList.append(m4.dic)

        # Plot resulting distributions and convergence diagnostics
        mc.Matplot.plot(m4, format='pdf', path='../Figures/mod_four', common_scale=False)

        # plot sp vs mc here
        pl.figure(figsize=(12,9))
        graphics.plot_spread_mc_nes(m4)
        pl.savefig('../Figures/mod_four/spread_rate.pdf')

        # Write posterior output
        m4.write_csv("../Figures/mod_four/reg_out.csv")

        D = mc.discrepancy(1/(1+np.exp(-data.nes_rates)), 1/(1+np.exp(-m4.y_sim.trace())), 1/(1+np.exp(-m4.y_mean.trace())))
        mc.Matplot.discrepancy_plot(D, name='D', format='pdf', path='../Figures/mod_four', report_p=True)

print dicList
# Plot only scenario data and spread rates
pl.figure(figsize=(12,9))
graphics.plot_data()
pl.savefig('../Figures/data_rates.pdf')
