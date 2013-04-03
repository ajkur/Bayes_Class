from __future__ import division
import models
import pymc as mc
import numpy as np
import data

# y0, n0, y1, n1 = data.full()
# y_j = np.log(y0/(n0 - y0)) - np.log(y1/(n1 - y1))
# V_j = 1.0/y1 + 1.0/(n1 - y1) + 1.0/y0 + 1.0/(n0 - y1)
# print y_j


mod = 1

if mod == 1:
    vars = models.mod_1()
    m = mc.MCMC(vars)
    # m.use_step_method(mc.AdaptiveMetropolis, [m.theta,m.theta_j,m.tau_sq])
    m.sample(iter=100000, burn=50000, thin=70)
    # m.sample(iter=10000, burn=0, thin=1)
    
if mod == 2:
    vars = models.mod_2()
    m = mc.MCMC(vars)
    m.use_step_method(mc.AdaptiveMetropolis, [m.tau,m.theta])
    m.sample(iter=10000, burn=0, thin=1)

print m.summary()
print 'DIC=%f' % m.dic
mc.Matplot.plot(m, format='pdf', path='../../Figures/Prob2', common_scale=False)

