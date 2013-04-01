# Model
from pymc import *
import numpy as np
import data

def mod_1():

    data_x, data_y = data.full()

    # sigma = pymc.Uniform('sigma', lower=0., upper=500., value=1.)
    one = np.ones(data_x.shape[0])

    # Covariates:
    #   Intercept, Age, Weight, Race, Visit
    beta = pymc.Normal('beta', mu = [0]*5, tau=[10**-6]*5 , value=[0]*5)  

    @deterministic
    def y_mean(beta=beta, data=data_x):
        return 1.0/(1.0 + np.exp(-np.dot(data_x,beta)))

    y_obs = pymc.Bernoulli('y_obs', value=data_y, p=y_mean, observed=True)

    return vars()

