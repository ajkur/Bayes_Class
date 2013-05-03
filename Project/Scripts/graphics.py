import pylab as pl
import numpy as np
import roth
import data


def plot_spread_mc(m, color='green', label='Spread Rate'):
    """Tool for plotting spread rate vs MC for each realization."""
    MC = pl.arange(0., 0.51, .01)
    y_trace = []
    sigList = []
    hocList = []
    mExtList = []
    for modSig in m.modSig.trace():
        sigList.append(modSig)
    for hoc in m.hoc.trace():
        hocList.append(hoc)
    for mExt in m.mExt.trace():
        mExtList.append(mExt)

    for i in range(len(sigList)):
        y = roth.flameSpread(sigma=sigList[i], bulk=data.meanBulk, hoc=hocList[i], moist=MC, mExt=mExtList[i])
        pl.plot(MC, y, color='gray', alpha=.75, zorder=-1)
        y_trace.append(y)
    pl.plot(data.mcs, data.rates, 'bo', label='Experiment')
    pl.plot(MC, pl.mean(y_trace, axis=0), color=color, linewidth=5, label=label)
    decorate_plot()

def plot_spread_mc_nes(m, color='green', label='Spread Rate'):
    """Tool for plotting spread rate vs MC for each realization."""
    MC = pl.arange(0., 0.51, .01)
    y_trace = []
    sigList = []
    hocList = []
    mExtList = []
    for modSig in m.modSig.trace():
        sigList.append(modSig)
    for hoc in m.hoc.trace():
        hocList.append(hoc)
    for mExt in m.mExt.trace():
        mExtList.append(mExt)

    for i in range(len(sigList)):
        y = roth.flameSpread(sigma=sigList[i], bulk=data.meanBulk, hoc=hocList[i], moist=MC, mExt=mExtList[i])
        pl.plot(MC, y, color='gray', alpha=.75, zorder=-1)
        y_trace.append(y)
    pl.plot(data.nes_mcs, data.nes_rates, 'bo', label='Experiment')
    pl.plot(MC, pl.mean(y_trace, axis=0), color=color, linewidth=5, label=label)
    decorate_plot()

def plot_spread_mc_shift(m, color='green', label='Spread Rate'):
    """Tool for plotting spread rate vs MC for each realization."""
    MC = pl.arange(0., 0.51, .01)
    y_trace = []
    sigList = []
    hocList = []
    mExtList = []
    for modSig in m.modSig.trace():
        sigList.append(modSig)
    for hoc in m.hoc.trace():
        hocList.append(hoc)
    for mExt in m.mExt.trace():
        mExtList.append(mExt)

    for i in range(len(sigList)):
        y = roth.flameSpread(sigma=(sigList[i]+100.), bulk=data.meanBulk, hoc=hocList[i], moist=MC, mExt=mExtList[i])
        pl.plot(MC, y, color='gray', alpha=.75, zorder=-1)
        y_trace.append(y)
    pl.plot(data.mcs, data.rates, 'bo', label='Experiment')
    pl.plot(MC, pl.mean(y_trace, axis=0), color=color, linewidth=5, label=label)
    decorate_plot()

def plot_spread_mc_nomext(m, color='green', label='Spread Rate'):
    """Tool for plotting spread rate vs MC for each realization."""
    MC = pl.arange(0., 0.51, .01)
    y_trace = []
    sigList = []
    hocList = []
    mExtList = []
    for modSig in m.modSig.trace():
        sigList.append(modSig)
    for hoc in m.hoc.trace():
        hocList.append(hoc)

    for i in range(len(sigList)):
        y = roth.flameSpread(sigma=sigList[i], bulk=data.meanBulk, hoc=hocList[i], moist=MC, mExt=0.3)
        pl.plot(MC, y, color='gray', alpha=.75, zorder=-1)
        y_trace.append(y)
    pl.plot(data.mcs, data.rates, 'bo', label='Experiment')
    pl.plot(MC, pl.mean(y_trace, axis=0), color=color, linewidth=5, label=label)
    decorate_plot()


def plot_data(label='Spread Rate'):
    pl.plot(data.mcs, data.rates, 'bo', label=label)
    decorate_plot()


def decorate_plot():
    """Decorate the plot with labels."""
    pl.axis([0, 0.5, 0., 7.])
    pl.legend(numpoints=1, prop=dict(size=20), fancybox=True)
    pl.xticks(fontsize=20)
    pl.xlabel('Moisture Content', fontsize=24)
    pl.yticks(fontsize=20)
    pl.ylabel('Spread Rate (m/s)', fontsize=24)