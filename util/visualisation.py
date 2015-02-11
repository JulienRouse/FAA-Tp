'''
A small lib that will hopefully help me plot some of my tp
and help me visualize whats going on in here.

'''

import pylab
import numpy as np

    

def plot_points_cloud(x,y):
    '''
    Plot points cloud.
    
    :param x: a vector containing the x-coordinates for the points to plot
    :param y: a vector containing the y-coordinates for the points to plot
    :type x: list of float
    :type y: list of float
    :return: nothing
    :rtype: void
    :side-effect: Create a png resulting from the plotting, and a popup
                  showing the plot.
    '''
    pylab.plot(x,y,'b.')



def plot_tp3(theta,n=20):
    '''
    Plot a line
    '''
    size = theta[n].shape[1]
    x = np.arange(-2.5,2.6,0.1)
    y = np.zeros(x.shape)
    for i in xrange(0,size):
        tmp = theta[n][0,i]*x**i
        y = y + tmp
    pylab.plot(x,y,'g-')

def plot_tp4(theta):
    '''
    plot a line
    '''
    x = np.arange(-20,20,0.2)
    
    

def plot_tp2(theta):
    '''
    '''
    plot_tp3(theta,0)
    show()

if __name__ == '__main__':
    pass
