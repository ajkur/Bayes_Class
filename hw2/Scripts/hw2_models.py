# Model
from pymc import *
from numpy import array, empty
from numpy.random import randint

def hw1ex():

    theta = pymc.Beta('theta',alpha=10,beta=10)
    d = pymc.Binomial('d', n=np.array([20]), p=theta, value=np.array([3]),observed=True)

    return vars()

def prob_2():

    data_2 = np.array([3.7, 3.4, 5.5, 5.0, 5.4, 6.6, 4.8, 4.4, 5.1, 5.4])

    y_mean = pymc.Uninformative('y_mean', value=0.)
    sigma = pymc.Uniform('sigma', lower=0., upper=100., value=1.)

    y_obs = pymc.Normal('y_obs', value=data_2, mu=y_mean, tau=sigma**-2, observed=True)

    return vars()

def prob_6(w_prior):

    dillo_kills = np.array([2,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0])

    if w_prior == 1:
        theta = pymc.Gamma('theta', alpha=0.001, beta=0.001, value=5.0)
    elif w_prior == 2:
        theta = pymc.Gamma('theta', alpha=1.11, beta=1.61, value=5.0)
    elif w_prior == 3:
        theta = pymc.Uniform('theta', lower=0.0, upper=20.0, value=5.0)

    dillos = Poisson('dillos', mu=theta, value=dillo_kills, observed=True)

    return vars()

def prob_7(w_prior):

    low_data = np.array([91., 46., 95., 60., 33., 410., 105., 43., 189., 1097., 54., 178., 114., 137., 233., 101., 25., 70., 357.])
    nor_data = np.array([370., 267., 99., 157., 75., 1281., 48., 298., 268., 62., 804., 430., 171., 694., 404.])

    if w_prior == 1:
        mu_low = pymc.Uninformative('mu_low', value=1.)
        mu_nor = pymc.Uninformative('mu_nor', value=1.)
        tau_low = pymc.Uninformative('tau_low', value=10.)
        tau_nor = pymc.Uninformative('tau_nor', value=10.)
        
    elif w_prior == 2:
        mu_low = pymc.Normal('mu_low', mu=4.87, tau=0.003)
        mu_nor = pymc.Normal('mu_nor', mu=5.39, tau=0.003)
        tau_low = pymc.Gamma('tau_low', alpha=1.04, beta=0.001)
        tau_nor = pymc.Gamma('tau_nor', alpha=1.054, beta=0.001)
    
    y_low = Normal('y_low', value=low_data, mu=mu_low, tau=tau_low, observed=True)
    y_nor = Normal('y_nor', value=nor_data, mu=mu_nor, tau=tau_nor, observed=True)

    return vars()
