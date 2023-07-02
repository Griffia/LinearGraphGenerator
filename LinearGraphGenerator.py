import matplotlib.pyplot as plt
import random
import numpy as np

def y_mx_c_graph():

    x = np.linspace(-5, 5, 11)
    # Generates an array from -5, to 5.

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



    plt.xlim(-5, 5)
    plt.ylim(-10, 10)
    # Stating the limits of the axis

    left_boarder_x = [-5, -5]
    left_boarder_y = [-10, 10]
    # Creates a boarder around the graph

    bottom_boarder_x = [-5, 5]
    bottom_boarder_y = [-10, -10]

    plt.plot(left_boarder_x, left_boarder_y,c='black', linewidth=1)
    plt.plot(bottom_boarder_x, bottom_boarder_y,c='black', linewidth=1.5)

    plt.plot(x,y, marker = 'x', c='red', linewidth=1)
    # Plot the linear equation

    ax = plt.gca()
    ax.spines[['left', 'bottom']].set_position('center')
    # Centers the axes of the plt, allowing for four quadrants
    

    plt.xticks(np.arange(-5,6,1))
    # Changes the scale of x axis
    plt.yticks(np.arange(-10,11,1))
    # Changes the scale of y axis

    plt.xlabel('x', loc='right')
    plt.ylabel('y', loc='top', rotation = 0)
    # Adds labels for both x and y axis


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
        



    plt.grid(True)
    
    plt.savefig('generatedGraph.png')
    # Saves randomly generated graph to a png file.
    # string can be changed to change the image name
    

y_mx_c_graph()
# Calls the user defined function
