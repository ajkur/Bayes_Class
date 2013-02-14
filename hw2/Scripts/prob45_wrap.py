from __future__ import division
import numpy as np
import scipy.stats
import matplotlib as plt
from pylab import *
import slice_sampler
import mh_sampler

def plot_hist(x_l, file_path):
    figure()
    n, bins, patches = hist(x_l, 20, histtype='bar')
    plt.savefig(file_path)

def plot_trace(x_l, n_l, file_path):
    figure()
    plot(n_l,x_l)
    plt.savefig(file_path)


data = np.array([3.7, 3.4, 5.5, 5.0, 5.4, 6.6, 4.8, 4.4, 5.1, 5.4])

# MH Sampling
x_chain, n_chain, acc = mh_sampler.mh_sample(5000,data,10.0,2.0)

plot_hist(x_chain[:acc+1], '../Figures/Prob4/mu_hist.pdf')
plot_trace(x_chain[:acc+1], n_chain[:acc+1], '../Figures/Prob4/mu_trace.pdf')

# Slice Sampling
n = 1000
x_chain = slice_sampler.slice_sample(n,data,10.0)
n_chain = np.arange(1,n+2,1)
plot_hist(x_chain, '../Figures/Prob5/mu_hist.pdf')
plot_trace(x_chain, n_chain, '../Figures/Prob5/mu_trace.pdf')