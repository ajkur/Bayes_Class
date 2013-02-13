# Sampler
import hw2_models
import pymc as mc

probnum = 2

if probnum == 1:
    vars = hw2_models.hw1ex()

    m = mc.MCMC(vars)
    m.sample(iter=10000, burn=1000, thin=10)

    #print m.beta.stats()
    print m.theta.summary()
    print 'DIC=%f' % m.dic
    mc.Matplot.plot(m, format='pdf', path='../Figures/ex1', common_scale=False)

elif probnum == 2:
    vars = hw2_models.prob_2()

    m = mc.MCMC(vars)
    m.sample(iter=10000, burn=100, thin=15)

    #print m.beta.stats()
    print m.y_mean.summary()
    print m.sigma.summary()
    print 'DIC=%f' % m.dic
    mc.Matplot.plot(m, format='pdf', path='../Figures/Prob2', common_scale=False)    