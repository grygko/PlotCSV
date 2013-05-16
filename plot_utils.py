#!/usr/bin/env python

"""Module contains utility functions for plotting data using the Matplotlib
library
"""
# TODO: plot from multiple files (on dictionary read?)

import numpy as np
import matplotlib.pyplot as plt

def plot_fig_from_dict(data_dict, xkey, ykeys,
        xlab='x-label', ylab='y-label', leg_loc='best',
        xlim=(None, None), ylim=(None, None),
        xtick_fmt='plain', ytick_fmt='plain',
        xscale='linear', yscale='linear', 
        grid=False,
        labels=None,
        outfile='', ):
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
            ax.plot(data_dict[xkey][0], data_dict[k][0], 'ko')
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    if labels:  # if labels are supplied
        handles = ax.get_legend_handles_labels()[0]
        ax.legend(handles, labels, loc=leg_loc)
    ax.set_xlim(xlim,)
    ax.set_ylim(ylim,)
    ax.ticklabel_format(style=xtick_fmt, scilimits=(0,0), axis='x')
    ax.ticklabel_format(style=ytick_fmt, scilimits=(0,0), axis='y')
    ax.set_xscale(xscale)
    ax.set_yscale(yscale)
    if grid:
        ax.grid()
    if outfile:
        print("Saving to {0}".format(outfile))
        plt.savefig(outfile)
    plt.show()

def plot_image(filename, width=0):
    """Plot image in IPython Notebook 

    where the image may be located at an arbitrary path

    Example:
        picture('/path/to/image.png', width=6.1)

    Author: Jakob Gager
    Date: 2013-02-07
    TODO: multiple plots
    """
    from PIL import Image as PILImage
    import matplotlib.pyplot as plt

    img = PILImage.open(filename)
    dpi = 96 #plt.rcParams['figure.dpi']*2
    figsize = (img.size[0]/dpi, img.size[1]/dpi)
    if width > 0:
        height=width*img.size[1]/img.size[0]
        figsize = (width, height)
    picfig = plt.figure(figsize=figsize)
    ax = picfig.add_axes([0,0,1,1], frameon=False)
    ax.set_axis_off()
    plt.imshow(img);
    ax.invert_yaxis()

def plot_images(filenames, width=0, comp=(0, 0), dpi=96, 
                figsize=(10, 5), hspace=0.02, wspace=0.02):
    """Plot image in IPython Notebook 

    where the image may be located at an arbitrary path

    Examples:
    plot_images([file1, file2], comp=(2, 1), figsize=(20, 10))
    plot_images('path/to/image.png')

    Author: Jakob Gager
    Date: 2013-02-07
    TODO: multiple plots
    """
    from PIL import Image as PILImage

    if comp != (0, 0):
        rows, cols = comp # e.g., (2, 2)
    elif type(filenames) == str:
        rows, cols = 1, 1
        filenames = [filenames]
    elif len(filenames) == 2:
        rows, cols = 1, 2
    elif len(filenames) == 3:
        rows, cols = 1, 3
    elif len(filenames) == 4:
        rows, cols = 2, 2
    else:
        print 'Number of files either exceeds 4 or unknown... exiting'
        return None

    fig, axes = plt.subplots(nrows=rows, ncols=cols, 
        frameon=False, figsize=figsize, dpi=dpi,
        subplot_kw={'xticks': [], 'yticks': []})
    
    for ax, f in zip(np.ravel(axes), filenames):
        img = PILImage.open(f)
        figsize = (img.size[0]/dpi, img.size[1]/dpi)
        if width > 0:
            height=width*img.size[1]/img.size[0]
            figsize = (width, height)
        ax.imshow(img)
        ax.invert_yaxis()
    fig.subplots_adjust(hspace=hspace, wspace=wspace)

    plt.show()

if __name__ == "__main__":
    import csv_utils
    with open('p26_static_n1_e1.dat', 'rb') as f:
        data_dict = csv_utils.dict_from_csv(f)
    plot_fig_from_dict(
            data_dict, 'EPPLEQV', ('SX', 'SY'), 
            xlab='Pl.strain', ylab='Stress, MPa')
