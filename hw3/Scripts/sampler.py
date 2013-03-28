import hw3_models
import pymc as mc
import numpy as np
import hw3_data

vars = hw3_models.prob_3()

m = mc.MCMC(vars)
m.use_step_method(mc.AdaptiveMetropolis, [m.beta])
m.sample(iter=150000, burn=50000, thin=200)
# m.sample(iter=1500, burn=5, thin=1)

print m.beta.summary()
# print m.evap_sim.stats()
print 'DIC=%f' % m.dic
mc.Matplot.plot(m, format='pdf', path='../Figures', common_scale=False)


# Chi squared 
# T_sim = 0.0
# T_data = 0.0
# evap_samp = m.trace('evap_sim')[-1]
# evap_exp = np.mean(evap_samp)
# evap_var = np.std(evap_samp)**2
# data_x, data_y = hw3_data.evap()
# data_exp = np.mean(data_y)
# data_var = np.std(data_y)**2
# for i in range(25):
# 	T_sim = (evap_samp[i]-evap_exp)**2/evap_exp + T_sim
# 	T_data = (data_y[i]-data_exp)**2/data_exp + T_data

# print T_sim
# print T_data

# samp_means = m.evap_sim.stats()['mean']
# samp_mean = np.mean(samp_means)
# samp_devs = m.evap_sim.stats()['standard deviation']
# samp_dev = np.mean(samp_devs)
# print samp_mean
# print samp_dev
# print samp_mean - 2.576*samp_dev
# print samp_mean + 2.576*samp_dev
