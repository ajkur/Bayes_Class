# Model
from pymc import *
import numpy as np
import hw3_data

def prob_3():

    data_x, data_y = hw3_data.evap()

    sigma = pymc.Uniform('sigma', lower=0., upper=500., value=1.)

    # Covariates:
    #   max gr temp, min gr temp, ave gr temp index, max air temp, min air temp, ave air temp index 
    beta = pymc.MvNormalCov('beta', mu = np.zeros(7), C = 100*np.identity(7))  

    @deterministic
    def y_mean(beta=beta, data=data_x):
        return np.dot(data_x,beta) 

    y_obs = pymc.Normal('y_obs', value=data_y, mu=y_mean, tau=sigma**-2, observed=True)
    evap_sim = pymc.Normal('evap_sim', mu=y_mean, tau=sigma**-2)

    return vars()

def prob_3_red1():

    data_x, data_y = hw3_data.evap_red1()

    sigma = pymc.Uniform('sigma', lower=0., upper=500., value=1.)

    # Covariates:
    #   max gr temp, min gr temp, ave gr temp index, max air temp, min air temp, ave air temp index 
    beta = pymc.MvNormalCov('beta', mu = np.zeros(3), C = 100*np.identity(3))  

    @deterministic
    def y_mean(beta=beta, data=data_x):
        return np.dot(data_x,beta) 

    y_obs = pymc.Normal('y_obs', value=data_y, mu=y_mean, tau=sigma**-2, observed=True)
    # evap_sim = pymc.Normal('evap_sim', mu=y_mean, tau=sigma**-2)

    return vars()

def prob_3_red2():

    data_x, data_y = hw3_data.evap_red2()

    sigma = pymc.Uniform('sigma', lower=0., upper=500., value=1.)

    # Covariates:
    #   max gr temp, min gr temp, ave gr temp index, max air temp, min air temp, ave air temp index 
    beta = pymc.MvNormalCov('beta', mu = np.zeros(4), C = 100*np.identity(4))  

    @deterministic
    def y_mean(beta=beta, data=data_x):
        return np.dot(data_x,beta) 

    y_obs = pymc.Normal('y_obs', value=data_y, mu=y_mean, tau=sigma**-2, observed=True)
    # evap_sim = pymc.Normal('evap_sim', mu=y_mean, tau=sigma**-2)

    return vars()

def prob_3_red3():

    data_x, data_y = hw3_data.evap_red3()

    sigma = pymc.Uniform('sigma', lower=0., upper=500., value=1.)

    # Covariates:
    #   max gr temp, min gr temp, ave gr temp index, max air temp, min air temp, ave air temp index 
    beta = pymc.MvNormalCov('beta', mu = np.zeros(4), C = 100*np.identity(4))  

    @deterministic
    def y_mean(beta=beta, data=data_x):
        return np.dot(data_x,beta) 

    y_obs = pymc.Normal('y_obs', value=data_y, mu=y_mean, tau=sigma**-2, observed=True)
    # evap_sim = pymc.Normal('evap_sim', mu=y_mean, tau=sigma**-2)

    return vars()

def prob_3_red4():

    data_x, data_y = hw3_data.evap_red4()

    sigma = pymc.Uniform('sigma', lower=0., upper=500., value=1.)

    # Covariates:
    #   max gr temp, min gr temp, ave gr temp index, max air temp, min air temp, ave air temp index 
    beta = pymc.MvNormalCov('beta', mu = np.zeros(3), C = 100*np.identity(3))  

    @deterministic
    def y_mean(beta=beta, data=data_x):
        return np.dot(data_x,beta) 

    y_obs = pymc.Normal('y_obs', value=data_y, mu=y_mean, tau=sigma**-2, observed=True)
    # evap_sim = pymc.Normal('evap_sim', mu=y_mean, tau=sigma**-2)

    return vars()

def prob_3_air():

    data_x, data_y = hw3_data.evap_air()

    sigma = pymc.Uniform('sigma', lower=0., upper=500., value=1.)

    # Covariates:
    #   max gr temp, min gr temp, ave gr temp index, max air temp, min air temp, ave air temp index 
    beta = pymc.MvNormalCov('beta', mu = np.zeros(2), C = 100*np.identity(2))
    # CC = np.zeros([2,2])
    # CC[0,0] = 55.0
    # CC[1,1] = 495.0
    # beta = pymc.MvNormalCov('beta', mu = np.array([5,45]), C = CC)  

    @deterministic
    def y_mean(beta=beta, data=data_x):
        return np.dot(data_x,beta) 

    y_obs = pymc.Normal('y_obs', value=data_y, mu=y_mean, tau=sigma**-2, observed=True)
    # evap_sim = pymc.Normal('evap_sim', mu=y_mean, tau=sigma**-2)

    return vars()
