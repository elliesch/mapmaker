import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation


#importing our data
df = pd.read_csv('../planets.csv')
exodf = df.loc[(df['st_mass']<=0.6) & (df['st_teff']<=6000)]


#defining our variables
bitwise_mask = (np.isfinite(exodf['st_dist'])) & (np.isfinite(exodf['st_mass'])) & (np.isfinite(exodf['st_teff']))
ra = exodf['ra'].loc[bitwise_mask]
dec = exodf['dec'].loc[bitwise_mask]
distance = exodf['st_dist'].loc[bitwise_mask] 
stellar_mass = exodf['st_mass'].loc[bitwise_mask]
teff = exodf['st_teff'].loc[bitwise_mask]


#converting coordinates
x = distance * np.cos(dec) * np.cos(ra)
y = distance * np.cos(dec) * np.sin(ra)
z = distance * np.sin(dec)

a = -300
b = 300


#creating animation
fig = plt.figure(figsize=[10, 8]) 

ax = fig.add_subplot(111, facecolor='Black', projection='3d', xlim = (a,b), ylim = (a,b), zlim = (a,b))
ax.scatter(x, y, z, c = teff, cmap= 'plasma', s = 2*((10*stellar_mass)**2), marker = 'o')  
ax.set_axis_off()

description_font = {'fontname':'Courier New'}

def func(i):
    '''
    This code was written by Luna Simone-Gonzalez and Ellie Cooper for the #TeamExoplanets 
    internship at the American Museum of Natural History
    '''
    
    ax.annotate('Distance from the Sun = {} parsec'.format(i), 
                xy=(0.25, 0.05), xycoords='axes fraction', color ='White', 
                fontsize=12, backgroundcolor='k', **description_font)
    
    if i > 1:
        ax.set_xlim(-i, i)
        ax.set_ylim(-i, i)
        ax.set_zlim(-i, i)

        
ani = animation.FuncAnimation(fig, func, frames=350, interval=10, blit=False)
ani.save('zoom_out.mpeg', writer='ffmpeg')