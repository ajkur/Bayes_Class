from __future__ import division
import models
import pymc as mc
import numpy as np
import data

# data_x, data_y = data.full()
# data_x = data_x[:,1:3]
# data_x[:,0] = 1
# print data_x

# mod = 1
# dics = np.zeros(5)

# for mod in range(1,6):
#     if mod == 1:
#         # Model 1
#         vars = models.mod_1()
#         m = mc.MCMC(vars)
#         m.use_step_method(mc.AdaptiveMetropolis, [m.beta])
#         m.sample(iter=20000, burn=10000, thin=25)
#     if mod == 2:
#         # Model 2
#         vars = models.mod_2()
#         m = mc.MCMC(vars)
#         m.use_step_method(mc.AdaptiveMetropolis, [m.beta])
#         m.sample(iter=20000, burn=10000, thin=25)
#     if mod == 3:
#         # Model 3
#         vars = models.mod_3()
#         m = mc.MCMC(vars)
#         m.use_step_method(mc.AdaptiveMetropolis, [m.beta])
#         m.sample(iter=20000, burn=10000, thin=25)
#     if mod == 4:
#         # Model 4
#         vars = models.mod_4()
#         m = mc.MCMC(vars)
#         m.use_step_method(mc.AdaptiveMetropolis, [m.beta])
#         m.sample(iter=20000, burn=10000, thin=25)
#     if mod == 5:
#         # Model 5
#         vars = models.mod_5()
#         m = mc.MCMC(vars)
#         m.use_step_method(mc.AdaptiveMetropolis, [m.beta])
#         m.sample(iter=20000, burn=10000, thin=25)
#     dics[mod-1] = m.dic
# print dics

# Model 1
vars = models.mod_1()
m = mc.MCMC(vars)
m.use_step_method(mc.AdaptiveMetropolis, [m.beta])
m.sample(iter=20000, burn=10000, thin=25)
print m.beta.summary()
# print 'DIC=%f' % m.dic
# mc.Matplot.plot(m, format='pdf', path='../../Figures/Prob1', common_scale=False)

