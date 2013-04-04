# Model
from __future__ import division
from pymc import *
import numpy as np
import data

def mod_1():
    # Data
    y0, n0, y1, n1 = data.full()
    y_j = np.log(y0/(n0 - y0)) - np.log(y1/(n1 - y1))
    V_j = 1.0/y1 + 1.0/(n1 - y1) + 1.0/y0 + 1.0/(n0 - y1)
    sig2_c = sum(V_j)

    # Priors
    # tau_sq = pymc.Uniform('tau_sq', lower=0., upper=1., value=0.5)
    tau_sq = pymc.Beta('tau_sq', alpha=1, beta=6, value=0.01)
    theta = pymc.Normal('theta', mu = 0, tau=10**-6, value=0)

    # Second Level
    theta_j = pymc.Normal('theta_j', mu = [theta]*22, tau=[1/tau_sq]*22, value=[0]*22)

    # Likelihood function
    y_j_obs = pymc.Normal('y_j_obs', value=y_j, mu=theta_j, tau=1/V_j, observed=True)

    return vars()

def mod_2():
    # Data
    y0, n0, y1, n1 = data.full()
    # y_j = np.log(y0/(n0 - y0)) - np.log(y1/(n1 - y1))
    # V_j = 1.0/y1 + 1.0/(n1 - y1) + 1.0/y0 + 1.0/(n0 - y1)

    # Priors
    # tau_sq = pymc.Uniform('tau_sq', lower=0., upper=1., value=0.5)
    tau_sq = pymc.Beta('tau_sq', alpha=1, beta=6, value=0.01)
    theta = pymc.Normal('theta', mu = 0, tau=10**-6, value=0)
    p1p = pymc.Uniform('p1p', lower=0., upper=1., value=0.5)
    p0p = pymc.Uniform('p0p', lower=0., upper=1., value=0.5)

    # Second Level
    theta_j = pymc.Normal('theta_j', mu = [theta]*22, tau=[1/tau_sq]*22, value=[0]*22)

    @deterministic
    def p0(th=theta_j,p1=p1p):
        c1 = np.exp(-th) + p1/(1+p1)
        return c1/(1+c1)
    @deterministic
    def p1(th=theta_j,p0=p0p):
        c0 = np.exp(-th) + p0/(1+p0)
        return c0/(1+c0)

    # Likelihood function
    y_j_obs_1 = pymc.Binomial('y_j_obs_1', value=y1, p=p1, n=n1, observed=True)
    y_j_obs_0 = pymc.Binomial('y_j_obs_0', value=y0, p=p0, n=n0, observed=True)

    return vars()



