# Sampler
import hw1_model
from pymc import MCMC
from pylab import hist, show
from pymc.Matplot import plot

M = MCMC(hw1_model)
M.sample(iter=10000, burn=1000, thin=10)
plot(M)