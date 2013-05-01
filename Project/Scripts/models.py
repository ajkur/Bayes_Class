from __future__ import division
import numpy as np
import roth
import data
import pymc as mc

def uniform_priors():
    # Priors
    # modSig, hoc, igFac
    modSig = mc.Uniform('modSig', lower=500., upper=50000., value=2000.)
    hoc = mc.Uniform('hoc', lower=1., upper=50000., value=6000.)
    # igFac = mc.Uniform('igFac', lower=1., upper=1000., value=200.)

    sigma = mc.Uniform('sigma', lower=0., upper=100., value=1.)

    # Model
    @mc.deterministic
    def y_mean(modSig=modSig, hoc=hoc, igFac=250., D_one=data.metricBulk, D_two=data.mcs):
        return roth.flameSpread(sigma=modSig, bulk=D_one, hoc=hoc, igFac=igFac, moist=D_two)

    # Likelihood
    # The likelihood is N(y_mean, sigma^2), where sigma
    # is pulled from a uniform distribution.
    y_obs = mc.Normal('y_obs',
                      value=data.rates,
                      mu=y_mean,
                      tau=sigma**-2,
                      observed=True)

    return vars()
