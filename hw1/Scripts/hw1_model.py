# Model
from pymc import *
from numpy import array, empty
from numpy.random import randint

theta = pymc.Beta('theta',alpha=10,beta=10)
d = pymc.Binomial('d', n=np.array([20]), p=theta, value=np.array([3]),observed=True)
