#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Classification
'''

import numpy as np


def open_data():
    '''
    Retrieve the points from the files given to us
    '''
    f = np.loadtxt('tp4_files/taillepoids_f.txt')
    h = np.loadtxt('tp4_files/taillepoids_h.txt')
    
    return f,h


def separate_data(data):
    '''
    find coordinate and store them separately
    '''
    datax = data[:,0]
    datay = data[:,1]
    
    return datax,datay



#WARNING
#je crois que le theta on le prend arbitrairement....
def calc_theta_1d(taille,poids):
    '''

    '''
    tmp = np.ones((1,taille.shape[0]))
    taille = np.vstack((taille,tmp))
    
    #
    etape1 = np.asmatrix(np.dot(taille,taille.T))
    etape1 = etape1.I
    #
    etape2 = np.dot(taille,poids)
    #
    theta = np.dot(etape1,etape2) 
    return theta





if __name__ == "__main__":
    f,h = open_data()
    taille_f,poids_f = separate_data(f)
    theta = calc_theta_1d(taille_f,poids_f)
    print theta
