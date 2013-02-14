from __future__ import division
import numpy as np
import scipy.stats
import matplotlib as plt
from pylab import *

def slice_sample(n, data, mu):
	# n is the number of iterations
    # data is what we are conditioning on
    # mu is an initial value for the chain of samples

    # Initialize arrays
    x_list = np.zeros(n+1)
    x_list[0] = mu
    sigma = 1.0

    width = 1.0

    for i in range(n):
        # Calculate h(x) at data
        h_x = 1
        for j in range(0,data.shape[0]):
            h_x = h_x * np.exp((-(data[j]-x_list[i])**2)/(2.0*sigma**2))

        # Sample from 0 to h(x) to get U
        U = np.random.uniform(0, h_x, 1)

        # Find bounds x_L and x_R
        x_L = x_list[i] - width
        x_R = x_list[i] + width
        left_bound = False
        right_bound = False
        while left_bound == False:
            h_x_L = 1.0
            for j in range(0,data.shape[0]):
                h_x_L = h_x_L * np.exp((-(data[j]-x_L)**2)/(2.0*sigma**2))
            if h_x_L < U:
                left_bound = True
            elif h_x_L > U:
                x_L = x_L - width

        while right_bound == False:
            h_x_R = 1.0
            for j in range(0,data.shape[0]):
                h_x_R = h_x_R * np.exp((-(data[j]-x_R)**2)/(2.0*sigma**2))
            if h_x_R < U:
                right_bound = True
            elif h_x_R > U:
                x_R = x_R + width

        # Sample from uniform on interval x_L to x_R
        x_list[i+1] = np.random.uniform(x_L, x_R, 1)

    return x_list