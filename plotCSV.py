#!/usr/bin/env python

import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size': 16})
#rc({'font.size': 18})

infile = sys.argv[1]
fname = sys.argv[1].split('.')[0]
fext = sys.argv[1].split('.')[1]

time,temp,sx,sy,sz,sxy,syz,sxz,epelx,epelz,epelxz = \
        np.loadtxt(infile, usecols=(0,1,2,3,4,5,6,7,8,10,13),
                   skiprows=1, unpack=True)

itmax = temp.argmax() # index at max TEMP

fig = plt.figure()
ax = fig.add_subplot(111)
l1 = ax.plot(temp, sx, 'o-', label='$\sigma_{xx}$')
l12 = ax.plot(temp[itmax], sx[itmax], 'ro')
l2 = ax.plot(temp, sy, 'o-', label='$\sigma_{yy}$')
l22 = ax.plot(temp[itmax], sy[itmax], 'ro')
l3 = ax.plot(temp, sz, 'mo-', label='$\sigma_{zz}$')
l32 = ax.plot(temp[itmax], sz[itmax], 'ro')

handles, labels = ax.get_legend_handles_labels()
leg = ax.legend(handles, labels, fancybox=False)
leg.get_frame().set_alpha(0.0)

ax.set_ylabel(r'Stress, Pa')
ax.set_xlabel(r'Temperature, K')
ax.grid()
plt.savefig(fname+'TEMP_SX'+'.png', dpi=300, transparent=True)

fig = plt.figure()
ax = fig.add_subplot(111)
l1 = ax.plot(sx, sy, 'o-')
l2 = ax.plot(sx[itmax], sy[itmax], 'ro')
#ax.set_aspect('equal')
ax.set_xlabel(r'Stress $\sigma_{xx}$ Pa')
ax.set_ylabel(r'Stress $\sigma_{yy}$ Pa')
ax.grid()
plt.savefig(fname+'SX_SY'+'.png', dpi=300, transparent=True)

fig = plt.figure()
ax = fig.add_subplot(111)
l1 = ax.plot(sx, sz, 'o-')
l2 = ax.plot(sx[itmax], sz[itmax], 'ro')
#ax.set_aspect('equal')
ax.set_xlabel(r'Stress $\sigma_{xx}$ Pa')
ax.set_ylabel(r'Stress $\sigma_{zz}$ Pa')
ax.grid()
plt.savefig(fname+'SX_SZ'+'.png', dpi=300, transparent=True)

fig = plt.figure()
ax = fig.add_subplot(111)
l1 = ax.plot(sxy, sxz, 'o-')
l2 = ax.plot(sxy[itmax], sxz[itmax], 'ro')
#temp=0.5*max(sxz)
#ax.set_aspect('equal')
#ax.set_xlim(-temp, temp)
ax.set_xlabel(r'Stress $\sigma_{xy}$ Pa')
ax.set_ylabel(r'Stress $\sigma_{xz}$ Pa')
ax.grid()
plt.savefig(fname+'SXY_SXZ'+'.png', dpi=300, transparent=True)

fig = plt.figure()
ax = fig.add_subplot(111)
l1 = ax.plot(syz, sxz, 'o-')
l2 = ax.plot(syz[itmax], sxz[itmax], 'ro')
#ax.set_aspect('equal')
#ax.set_xlim(-temp, temp)
ax.set_xlabel(r'Stress $\sigma_{yz}$ Pa')
ax.set_ylabel(r'Stress $\sigma_{xz}$ Pa')
ax.grid()
plt.savefig(fname+'SYZ_SXZ'+'.png', dpi=300, transparent=True)

theta_s = -0.5*np.arctan2(epelz-epelx, epelxz)  # max shear strain direction angle
#factor = max(eint)/max(exz) # scale factor
fig = plt.figure()
ax = fig.add_subplot(111)
l1 = ax.plot(time, theta_s*180/np.pi, lw=2)
l2 = ax.plot(time[itmax], theta_s[itmax]*180/np.pi, 'ro')
ax.set_xlabel('Time, s')
ax.set_ylabel(r'Max shear strain angle $\theta_s$')
ax.set_xscale('log')
ax.set_ylim(-90, 0)
ax.grid()
plt.savefig(fname+'MSSA'+'.png', dpi=300, transparent=True)
