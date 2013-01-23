#!/usr/bin/env python

"""Module contains utility functions for plotting data using the Matplotlib
library
"""

import matplotlib.pyplot as plt

def plot_fig_from_dict(data_dict, xkey, ykeys,
        xlab='x-label', ylab='y-label', leg_loc='best',
        xlim=(None, None), ylim=(None, None),
        xtick_fmt='sci', ytick_fmt='plain'):
    """Plot a figure from dictionary data

    Args:
        xkey: dictionary key for x-values
        ykeys (tuple): dictionary keys for y-values
    """
    # TODO: sanity checks whether x,y values are of the same length

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for k in ykeys:
        if data_dict.has_key(k):
            ax.plot(data_dict[xkey], data_dict[k], label=k)
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    ax.legend(loc=leg_loc)
    ax.set_xlim(xlim,)
    ax.set_ylim(ylim,)
    ax.ticklabel_format(style=xtick_fmt, scilimits=(0,0), axis='x')
    ax.ticklabel_format(style=ytick_fmt, scilimits=(0,0), axis='y')
    plt.show()

if __name__ == "__main__":
    import csv_utils
    with open('p26_static_n1_e1.dat', 'rb') as f:
        data_dict = csv_utils.dict_from_csv(f)
    plot_fig_from_dict(
            data_dict, 'EPPLEQV', ('SX', 'SY'), 
            xlab='Pl.strain', ylab='Stress, MPa')
