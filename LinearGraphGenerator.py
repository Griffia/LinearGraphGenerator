import matplotlib.pyplot as plt
import numpy as np
import random

def y_mx_c_graph():

    ax = plt.subplot()


    ax.spines[['left', 'bottom']].set_position(('data', 0))
    # Move the left and bottom spines to the center of the graph
    ax.spines[['top', 'right']].set_visible(False)
    # Hides the right and top spines

    # ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    # ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(-1, 0, "<k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, -1, "vk", transform=ax.get_xaxis_transform(), clip_on=False)


    x = np.linspace(-100, 100,201)
    # Generates an array from -100, to 100.

    m = 0

    while m == 0:
        m = random.randint(-5,5)
    # Picks a random number from -5 to 5 for the gradient.
    # As we want graphs with a gradient, m != 0.

    c = random.randint(-5,5)
    #  Picks a random number from -5 to 5 for the y-intercept

    y = []
    # Empty list to store the values of y for the linear equation

    for value in x:
        y_coord = m * value + c
        y.append(y_coord) 
    # Simple for loop that calculates the y value using each
    # value for x

    # Handling all the correct formats for the equation of the line
    if c == 0 and m == -1:
        plt.title(f'y = -x', loc='right', c = 'red')
        
    elif c < 0 and m == -1:
        plt.title(f'y = -x {c}' , loc='right', c = 'red')
        
    elif c > 0 and m == -1:
        plt.title(f'y = -x + {c}' , loc='right', c = 'red')
        
    elif c == 0 and m == 1:
        plt.title(f'y = x' , loc='right', c = 'red')
        
    elif c < 0 and m == 1:
        plt.title(f'y = x {c}' , loc='right', c = 'red')
        
    elif c > 0 and m == 1:
        plt.title(f'y = x + {c}' , loc='right', c = 'red')
        
    elif c == 0 and m !=1:
        plt.title(f'y = {m}x', loc='right', c = 'red')
        
    elif c < 0 and m !=1:
        plt.title(f'y = {m}x {c}', loc='right', c = 'red')
        
    elif c > 0 and m!=1:
        plt.title(f'y = {m}x + {c}', loc='right', c = 'red')

    plt.xticks(np.arange(-100,100,1))
    # Changes the tick scale of x axis, to increment by 1 from -100 to 100
    plt.yticks(np.arange(-100,100,1))
    # Changes the tick scale of y axis, to increment by 1 from -100 to 100

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    # Stating the limits of the visible area of the graph

    plt.plot(x,y, marker = 'x', c='red', linewidth=1)
    # Plot the linear equation

    plt.grid(which='both')
    plt.savefig('generatedGraph.png')
    plt.show()

y_mx_c_graph()
