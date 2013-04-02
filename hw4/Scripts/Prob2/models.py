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

    # Priors
    tau_sq = pymc.Uniform('tau_sq', lower=0., upper=1., value=0.5)
    theta = pymc.Normal('theta', mu = 0, tau=10**-6, value=0)

    # Second Level
    theta_j = pymc.Normal('theta_j', mu = theta, tau=tau_sq**0.5, value=0)

    # Likelihood function
    y_j_obs = pymc.Normal('y_j_obs', value=y_j, mu=theta_j, tau=1/V_j, observed=True)

    return vars()




