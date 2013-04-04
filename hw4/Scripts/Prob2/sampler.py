from __future__ import division
import models
import pymc as mc
import numpy as np
import data

# y0, n0, y1, n1 = data.full()
# y_j = np.log(y0/(n0 - y0)) - np.log(y1/(n1 - y1))
# V_j = 1.0/y1 + 1.0/(n1 - y1) + 1.0/y0 + 1.0/(n0 - y1)
# # print sum(V_j)
# # print np.mean(y_j)
# for i in range(y_j.shape[0]):
#     # print y_j[i]
#     print y1[i]/n1[i]
# p0=np.array([0.081, 0.089, 0.093, 0.075, 0.08 , 0.092, 0.132, 0.097, 0.109, 0.085, 0.08 , 0.168, 0.049, 0.06 , 0.179, 0.162, 0.107, 0.057, 0.042, 0.16 , 0.093, 0.048])
# p1=np.array([0.081, 0.089, 0.093, 0.075, 0.08 , 0.092, 0.132, 0.097, 0.109, 0.085, 0.08 , 0.168, 0.049, 0.06 , 0.179, 0.162, 0.107, 0.057, 0.042, 0.16 , 0.093, 0.048])

# for i in range(p0.shape[0]):
#     print np.log(p0[i]/(1 - p0[i])) #- np.log(p1[i]/(1 - p1[i]))




mod = 2

if mod == 1:
    vars = models.mod_1()
    m = mc.MCMC(vars)
    m.sample(iter=100000, burn=70000, thin=70)
    
if mod == 2:
    vars = models.mod_2()
    m = mc.MCMC(vars)
    m.use_step_method(mc.AdaptiveMetropolis, [m.theta])
    m.sample(iter=20000, burn=10000, thin=10)

print m.summary()
print 'DIC=%f' % m.dic
mc.Matplot.plot(m, format='pdf', path='../../Figures/Prob2', common_scale=False)

