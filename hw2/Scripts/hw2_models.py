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
