import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

import itertools

from panning import panning_fun
from zooming import zoom_fun
from on_pick import onpick


#defining our dataframes
df = pd.read_csv('planets.csv')

exodf = df.loc[(df['st_mass']<= 0.6) & (df['st_teff'] < 6000) & (df['pl_orbsmax'] > 0)]
stardf = df.loc[(df['st_mass']<= 0.6) & (df['st_teff'] < 6000) & (df.duplicated('pl_hostname')) & (df['pl_orbsmax'] > 0)]


#cleaning and defining our data
bitwise_mask = (np.isfinite(stardf['st_dist'])) & (np.isfinite(stardf['st_mass'])) & (np.isfinite(stardf['st_teff']))

ra = stardf['ra'].loc[bitwise_mask]
dec = stardf['dec'].loc[bitwise_mask]
distance = stardf['st_dist'].loc[bitwise_mask] 
stellar_mass = stardf['st_mass'].loc[bitwise_mask]
teff = stardf['st_teff'].loc[bitwise_mask]
star_name = stardf['pl_hostname'].loc[bitwise_mask]

x = distance * np.cos(dec) * np.cos(ra)
y = distance * np.cos(dec) * np.sin(ra)
z = distance * np.sin(dec)

#axes limits for on_key codes
a = -300
b = 300
c = a
d = b
e = a
f = b

labels_column = star_name
labels = labels_column.values

colors = itertools.cycle(['#42f4bf', 'green', 'blue']) 


#Define the figure and scatter plot the data
fig = plt.figure(figsize=[10, 8]) 

ax = fig.add_subplot(111, facecolor='Black', projection='3d', xlim = (a,b), ylim = (c,d), zlim = (e,f))
ax.scatter(x, y, z, c = teff, cmap= 'plasma', s = 2*((10*stellar_mass)**2), marker = 'o')  
ax.set_axis_off()

#Connect the matplotlib events
fig = ax.get_figure() # get the figure of interest

fig.canvas.mpl_connect('key_press_event', panning_fun)
fig.canvas.mpl_connect('scroll_event',zoom_fun)
fig.canvas.mpl_connect('pick_event', onpick)