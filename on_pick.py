import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

import itertools


def onpick(event): #this first line defines our function, and takes in an `event`

    '''
    This code was written by the entire #TeamExoplanets team, with specific pieces
    contributed directly by Prachurjya Barua and Maxine Sowah.
    '''
    
    ind = event.ind #here we select an `attribute` of our event, this one is the indices
    star_label= labels[ind]

        
    our_df = exodf.loc[star_name == star_label[0]]
    num_of_planets= our_df['pl_pnum'] #the number of planets per star
    orb_radius= our_df['pl_orbsmax'] #the semi-major axis radius of the planet


    orbradii= orb_radius.loc[np.isfinite(orb_radius)].sort_values()
    orbradii= orbradii.values #this turns a column into numbers

    
    if len(orbradii) > 0:
        planet_total = len(orbradii)
        fig2= plt.figure()
        ax2= fig2.add_subplot(111,xlim=(-max(orbradii)-1, max(orbradii)+1), ylim=(-max(orbradii)-1, max(orbradii)+1))   
        

        for radius in orbradii:
            
            x = np.linspace(-1.0, 1.0, 100) #this adds enough points to complete the circle
            y = np.linspace(-1.0, 1.0, 100)
            X, Y = np.meshgrid(x,y)
            F = X**2 + Y**2 - radius #the rest of this equation draws the circle, 0.2 adds the radius
            ax2.contour(X,Y,F,[0], colors=next(colors))

        
        ax2.scatter(0,0, marker='*', s=20, c=our_df['st_teff'].iloc[0], cmap='hot')
        text = 'Name = {}\nDistance from Sun = {} parsec\nTotal Planets = {}\nEffective Temp = {} K\nMass = {} M_Sun'.format(
            star_name.values[0],our_df['st_dist'].iloc[0],num_of_planets.iloc[0],our_df['st_teff'].iloc[0],our_df['st_mass'].iloc[0])
        ax2.annotate(text, xy=(0.6, 0.8), xycoords='axes fraction', **description_font)
            
        ax2.spines['right'].set_visible(False)
        ax2.spines['top'].set_visible(False)
            
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()