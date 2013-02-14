# Sampler
import hw2_models
import pymc as mc

probnum = 4

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
    # Test Run
    # m.sample(iter=1000, burn=100, thin=1)
    # Full Run
    m.sample(iter=10000, burn=100, thin=15)

    #print m.beta.stats()
    print m.y_mean.summary()
    print m.sigma.summary()
    print 'DIC=%f' % m.dic
    mc.Matplot.plot(m, format='pdf', path='../Figures/Prob2', common_scale=False)

elif probnum == 3:
    # Part A - diffuse gamma
    vars = hw2_models.prob_6(1)

    m = mc.MCMC(vars)
    m.sample(iter=50000, burn=10000, thin=20)

    print m.theta.summary()
    print 'DIC=%f' % m.dic
    mc.Matplot.plot(m, format='pdf', path='../Figures/Prob6/A', common_scale=False)

    # # Part B - informed gamma
    # vars = hw2_models.prob_6(2)

    # m = mc.MCMC(vars)
    # m.sample(iter=30000, burn=10000, thin=20)

    # print m.theta.summary()
    # print 'DIC=%f' % m.dic
    # mc.Matplot.plot(m, format='pdf', path='../Figures/Prob6/B', common_scale=False)

    # Part C - Uniform
    # vars = hw2_models.prob_6(3)

    # m = mc.MCMC(vars)
    # m.sample(iter=30000, burn=4000, thin=15)

    # print m.theta.summary()
    # print 'DIC=%f' % m.dic
    # mc.Matplot.plot(m, format='pdf', path='../Figures/Prob6/C', common_scale=False)

elif probnum == 4:
    # Uninformed Priors
    vars = hw2_models.prob_7(2)

    m = mc.MCMC(vars)
    m.sample(iter=50000, burn=20000, thin=25)

    print 'DIC=%f' % m.dic
    mc.Matplot.plot(m, format='pdf', path='../Figures/Prob7/Uninformed', common_scale=False)  

    # Informed Priors
    vars = hw2_models.prob_7(2)

    m = mc.MCMC(vars)
    m.sample(iter=50000, burn=20000, thin=15)

    print 'DIC=%f' % m.dic
    mc.Matplot.plot(m, format='pdf', path='../Figures/Prob7/Informed', common_scale=False)   
