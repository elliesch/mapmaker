def panning_fun(event): 

    '''
    This code was written by Debjani Das and Laura Valdez for the #TeamExoplanets 
    internship at the American Museum of Natural History
    '''

    if event.key == 'left': #if the key pressed is the left arrow
        global a #tells our function that we defined 'a' outside of the function
        global b #^
        a = a-50 #subtracts 50 from the value of a each time the key is pressed
        b = b-50 #^
        ax.set_xlim([a,b]) #resets the x-axis limits to new 'a' and 'b'
        plt.show() #re-shows the plot so we can see the change in axis

    if event.key == 'right': #if the key pressed is the right arrow
        a = a+50 #adds 50 from the value of a each time the key is pressed
        b = b+50 #^
        ax.set_xlim([a,b]) #resets the x-axis limits to new 'a' and 'b'
        plt.show() #re-shows the plot so we can see the change in axis

    if event.key == 'down': #if the key pressed is the down arrow
        global c #tells our function that we defined 'c' outside of the function
        global d #^
        c = c-50 #subtracts 50 from the value of a each time the key is pressed
        d = d-50 #^
        ax.set_ylim([c,d]) #resets the y-axis limits to new 'c' and 'd'
        plt.show() #re-shows the plot so we can see the change in axis

    if event.key == 'up': #if the key pressed is the up arrow
        c = c+50 #adds 50 from the value of a each time the key is pressed
        d = d+50 #^
        ax.set_ylim([c,d]) #resets the y-axis limits to new 'c' and 'd'
        plt.show() #re-shows the plot so we can see the change in axis

    if event.key == 'r': #if the key pressed is the r key
        global e #tells our function that we defined 'e' outside of the function
        global f #^
        e = e-50 #subtracts 50 from the value of a each time the key is pressed
        f = f-50 #^
        ax.set_zlim([e,f]) #resets the y-axis limits to new 'c' and 'd'
        plt.show() #re-shows the plot so we can see the change in axis

    if event.key == 't': #if the key pressed is the t key
        e = e+50 #adds 50 from the value of a each time the key is pressed
        f = f+50 #^
        ax.set_zlim([e,f]) #resets the y-axis limits to new 'c' and 'd'
        plt.show() #re-shows the plot so we can see the change in axis

    if event.key == 'b': #if the key pressed is the b key
        ax.set_xlim([-300,300]) #resets the x-axis limits 
        ax.set_ylim([-300,300]) #resets the y-axis limits 
        ax.set_zlim([-300,300]) #resets the z-axis limits 
        plt.show() #re-shows the plot so we can see the change in axis