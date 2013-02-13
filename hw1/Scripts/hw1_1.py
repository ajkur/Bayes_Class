import numpy as np
import scipy.stats
import matplotlib as plt
from pylab import *

def plot_hist(a,b):
    v = np.random.beta(a, b, 10000)
    s = np.zeros(v.shape[0])

    for i in range(v.shape[0]):
        s[i] = np.random.binomial(20,v[i])

    figure()

    center = scipy.stats.itemfreq(s)[:,0]
    hist = scipy.stats.itemfreq(s)[:,1]
    plt.bar(center, hist, align = 'center', width = 0.7)
    plt.savefig('../Figures/a'+str(a)+'_b'+str(int(b))+'.pdf')

# Consider various choices of (a, b) including {(1, 1), (10, 10), and(10, 1)}
plot_hist(1,1)
plot_hist(10,10)
plot_hist(10,1)
alp = 2
bet = (17*alp - 14)/3.0
plot_hist(alp,bet)
