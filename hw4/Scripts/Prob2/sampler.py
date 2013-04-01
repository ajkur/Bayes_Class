from __future__ import division
import models
import pymc as mc
import numpy as np
import data

# y0, n0, y1, n1 = data.full()
# print y0/(n0 - y0)
vars = models.mod_1()

m = mc.MCMC(vars)
m.use_step_method(mc.AdaptiveMetropolis, [m.theta_j])
m.sample(iter=2000, burn=0, thin=1)
# m.sample(iter=40000, burn=25000, thin=1)

print m.theta_j.summary()
# print m.sigma.summary()
print 'DIC=%f' % m.dic
mc.Matplot.plot(m, format='pdf', path='../../Figures/Prob2', common_scale=False)

