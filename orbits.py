import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

df = pd.read_csv('planets.csv')

exodf = df.drop_duplicates('pl_hostname')
exodf = df.loc[(df['st_mass'] <=.6) & (df['st_teff'] <=6000) & (np.isfinite(df['pl_orbsmax']))]
star_names = exodf['pl_hostname']

for ii in star_names:
    
    plt.close()
    

    our_df = exodf.loc[star_names == ii]
    num_planet = our_df['pl_pnum']
    orb_radius = our_df['pl_orbsmax']
    orbradii = orb_radius.loc[np.isfinite(orb_radius)]
    orbradii = orbradii.values
    planet_total = len(orbradii)
    
    
    if len(orbradii) > 0:
        
        fig = plt.figure()
        ax = fig.add_subplot(111, xlim = (-max(orbradii)-.2,max(orbradii)+.2), ylim = (-max(orbradii)-.2,max(orbradii)+.2))
        lines = []
        
        for _ in range(planet_total):
            lines.append(ax.plot([], [], 'o'))
            
        def init():
            for ii in range(len(lines)):
                print(lines[ii])
                lines[ii][0].set_data([],[])
            return lines
        
        def animate(i):

            #angle = i/10. * np.pi
            angle_factor = np.arange(planet_total)
            angle_factor += 1
    
            for iii in range(planet_total):
                #angle = (i + angle_factor)/10. * np.pi
                angle = i/(10.*angle_factor[iii]) * np.pi
                moving_x = [0, orbradii[iii]*np.cos(angle)]
                moving_y = [0, orbradii[iii]*np.sin(angle)]
        
                #print(lines[ii])
                lines[iii][0].set_data(moving_x,moving_y)
        
            return lines
        our_animation = ani.FuncAnimation(fig, animate, np.arange(1, 1000), interval=75, init_func=init)  
        plt.show()