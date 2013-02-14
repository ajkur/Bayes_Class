from __future__ import division
import numpy as np
import scipy.stats
import matplotlib as plt
from pylab import *

def mh_sample(n, data, mu, walk_sig):
    # n is the number of iterations
    # data is what we are conditioning on
    # mu is an initial value for the chain of samples
    # walk_sig is the variance of the random walk

    # Initialize arrays
    x_list = np.zeros(n)
    n_list = np.zeros(n)
    x_list[0] = mu
    n_list[0] = 1

    # Variance is 1 for now
    sigma = 1.0

    # Pointer for last accepted value
    acc = 0

    for i in range(n):
        # Random Walk to generate next value of x
        z = x_list[acc] + np.random.normal(0.0,walk_sig**2,1)

        # Compute Denominator of MH alogrithm
        den = 1
        for j in range(0,data.shape[0]):
        	den = den * np.exp((-(data[j]-x_list[acc])**2)/(2.0*sigma**2))
        
        # Compute Numerator of MH alogrithm
        num = 1
        for j in range(0,data.shape[0]):
            num = num * np.exp((-(data[j]-z)**2)/2.0)

        # Compute the probability of a move, alpha
        alpha = min(1, num/den)

        # Accept / Reject
        if alpha == 1:
            x_list[acc+1] = z
            n_list[acc+1] = i+1
            acc = acc + 1
        elif alpha < 1:
            p_a = np.random.binomial(1, alpha, 1)
            if p_a == 1:
                x_list[acc+1] = z
                n_list[acc+1] = i+1
                acc = acc + 1

    return x_list, n_list, acc



