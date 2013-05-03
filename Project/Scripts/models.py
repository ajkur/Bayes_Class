from __future__ import division
import numpy as np
import roth
import data
import pymc as mc

def uniform_priors():
    # Priors
    # modSig, hoc, mExt
    modSig = mc.Uniform('modSig', lower=500., upper=50000., value=2000.)
    hoc = mc.Uniform('hoc', lower=1., upper=50000., value=6000.)
    mExt = mc.Uniform('mExt', lower=0., upper=1., value=0.3)

    sigma = mc.Uniform('sigma', lower=0., upper=100., value=1.)

    # Model - switch mc and hoc
    @mc.deterministic
    def y_mean(modSig=modSig, mBulk=data.meanBulk, hoc=hoc, moistC=data.mcs, moistE=mExt):
        return roth.flameSpread(sigma=modSig, bulk=mBulk, hoc=hoc, moist=moistC, mExt=moistE)

    # Likelihood
    # The likelihood is N(y_mean, sigma^2), where sigma
    # is pulled from a uniform distribution.
    y_obs = mc.Normal('y_obs',
                      value=data.rates,
                      mu=y_mean,
                      tau=sigma**-2,
                      observed=True)

    return vars()

def model_two():
    # Priors
    # modSig, hoc, mExt
    modSig = mc.Uniform('modSig', lower=500., upper=50000., value=2000.)
    hoc = mc.Uniform('hoc', lower=1., upper=50000., value=6000.)
    mExt = mc.Gamma('mExt', alpha=5.6, beta=20.87, value=0.2)

    sigma = mc.Uniform('sigma', lower=0., upper=100., value=1.)

    # Model - switch mc and hoc
    @mc.deterministic
    def y_mean(modSig=modSig, mBulk=data.meanBulk, hoc=hoc, moistC=data.mcs, moistE=mExt):
        return roth.flameSpread(sigma=modSig, bulk=mBulk, hoc=hoc, moist=moistC, mExt=moistE)

    # Likelihood
    # The likelihood is N(y_mean, sigma^2), where sigma
    # is pulled from a uniform distribution.
    y_obs = mc.Normal('y_obs',
                      value=data.rates,
                      mu=y_mean,
                      tau=sigma**-2,
                      observed=True)

    return vars()

def no_moist_data():
    # Priors
    # modSig, hoc, mExt
    modSig = mc.Uniform('modSig', lower=500., upper=50000., value=2000.)
    hoc = mc.Uniform('hoc', lower=1., upper=50000., value=6000.)
    # mExt = mc.Beta('mExt', alpha=2., beta=5., value=0.2)
    moistC = mc.Uniform('moistC', lower=0., upper=1., value=0.3)

    sigma = mc.Uniform('sigma', lower=0., upper=100., value=1.)

    # Model - switch mc and hoc
    @mc.deterministic
    def y_mean(modSig=modSig, mBulk=data.meanBulk, hoc=hoc, moistC=moistC, moistE=0.3):
        return roth.flameSpread(sigma=modSig, bulk=mBulk, hoc=hoc, moist=moistC, mExt=moistE)

    # Likelihood
    # The likelihood is N(y_mean, sigma^2), where sigma
    # is pulled from a uniform distribution.
    y_obs = mc.Normal('y_obs',
                      value=data.rates,
                      mu=y_mean,
                      tau=sigma**-2,
                      observed=True)

    return vars()

def one_beta():
    # Priors
    # modSig, hoc, mExt
    modSig = mc.Uniform('modSig', lower=500., upper=50000., value=2000.)
    hoc = mc.Uniform('hoc', lower=1., upper=50000., value=6000.)
    mExt = mc.Beta('mExt', alpha=2., beta=5., value=0.2)
    # mExt = mc.Uniform('mExt', lower=0., upper=1., value=0.3)

    sigma = mc.Uniform('sigma', lower=0., upper=100., value=1.)

    # Model - switch mc and hoc
    @mc.deterministic
    def y_mean(modSig=modSig, mBulk=data.meanBulk, hoc=hoc, moistC=data.mcs, moistE=mExt):
        return roth.flameSpread(sigma=modSig, bulk=mBulk, hoc=hoc, moist=moistC, mExt=moistE)

    # Likelihood
    # The likelihood is N(y_mean, sigma^2), where sigma
    # is pulled from a uniform distribution.
    y_obs = mc.Normal('y_obs',
                      value=data.rates,
                      mu=y_mean,
                      tau=sigma**-2,
                      observed=True)

    return vars()
