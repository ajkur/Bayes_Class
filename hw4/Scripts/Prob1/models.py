# Model
from __future__ import division
from pymc import *
import numpy as np
import data

def mod_1():

    data_x, data_y = data.full()

    # Covariates:
    #   Intercept, Age, Weight, Race, Visit
    beta = pymc.Normal('beta', mu = [0]*5, tau=[10**-6]*5 , value=[0]*5)  

    @deterministic
    def y_mean(beta=beta, data=data_x):
        return 1.0/(1.0 + np.exp(-np.dot(data_x,beta)))

    y_obs = pymc.Bernoulli('y_obs', value=data_y, p=y_mean, observed=True)

    return vars()

def mod_2():

    data_x, data_y = data.full()
    data_x = data_x[:,0:4]

    # Covariates:
    #   Intercept, Age, Weight, Race
    beta = pymc.Normal('beta', mu = [0]*4, tau=[10**-6]*4 , value=[0]*4)  

    @deterministic
    def y_mean(beta=beta, data=data_x):
        return 1.0/(1.0 + np.exp(-np.dot(data_x,beta)))

    y_obs = pymc.Bernoulli('y_obs', value=data_y, p=y_mean, observed=True)

    return vars()

def mod_3():

    data_x, data_y = data.full()
    data_x = data_x[:,1:4]
    data_x[:,0] = 1

    # Covariates:
    #   Intercept, Weight, Race
    beta = pymc.Normal('beta', mu = [0]*3, tau=[10**-6]*3 , value=[0]*3)  

    @deterministic
    def y_mean(beta=beta, data=data_x):
        return 1.0/(1.0 + np.exp(-np.dot(data_x,beta)))

    y_obs = pymc.Bernoulli('y_obs', value=data_y, p=y_mean, observed=True)

    return vars()

def mod_4():

    data_x, data_y = data.full()
    data_x = data_x[:,1:3]
    data_x[:,0] = 1

    # Covariates:
    #   Intercept, Weight
    beta = pymc.Normal('beta', mu = [0]*2, tau=[10**-6]*2 , value=[0]*2)  

    @deterministic
    def y_mean(beta=beta, data=data_x):
        return 1.0/(1.0 + np.exp(-np.dot(data_x,beta)))

    y_obs = pymc.Bernoulli('y_obs', value=data_y, p=y_mean, observed=True)

    return vars()

def mod_5():

    data_x, data_y = data.full()
    data_x = data_x[:,0:3]

    # Covariates:
    #   Intercept, Age, Weight
    beta = pymc.Normal('beta', mu = [0]*3, tau=[10**-6]*3 , value=[0]*3)  

    @deterministic
    def y_mean(beta=beta, data=data_x):
        return 1.0/(1.0 + np.exp(-np.dot(data_x,beta)))

    y_obs = pymc.Bernoulli('y_obs', value=data_y, p=y_mean, observed=True)

    return vars()
