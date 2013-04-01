import models
import pymc as mc
import numpy as np
import data

# data_x, data_y = data.full()
# print data_x
vars = models.mod_1()

m = mc.MCMC(vars)
m.use_step_method(mc.AdaptiveMetropolis, [m.beta])
m.sample(iter=20000, burn=10000, thin=25)
# m.sample(iter=40000, burn=25000, thin=1)

print m.beta.summary()
# print m.sigma.summary()
print 'DIC=%f' % m.dic
mc.Matplot.plot(m, format='pdf', path='../../Figures/Prob1', common_scale=False)

