#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


#open x,y
def load_data():
    x = np.loadtxt('x.txt')
    y = np.loadtxt('y.txt')
    
    return x,y

#moindre carré  avec X devenu phi(X), vecteur de fonctions ([1,x,x^2,x^3...x^m])
def calc_theta(x,y,m=50):
    line = np.zeros(x.shape)
    mat = np.ones((x.shape))
    theta = []
    for i in xrange(1,m+1):
        #remplir la ligne avec la bonne puissance
        line = np.power(x,i)
        #l'ajouter à la matrice existante
        mat = np.vstack((mat,line))
        #on calcule les moindres carrés
        
        #
        etape1 = np.asmatrix(np.dot(mat,mat.T))
        
        etape1 = etape1.I
        
        #

        etape2 = np.dot(mat,y)
        
        #
        theta_i = np.dot(etape1,etape2)
        
        theta.append(theta_i)
    return mat,theta



def mse():
    pass

#k-fold validation
# k c'est le nombre de fold
# n le nombre de donnée
def kfold_validation(k,n):
    '''
    on prend k = 10
    on a 100 pts a verifier
    on entraine theta sur les 900pts restants
    
    '''
    
    #j de 1 a k-1
    for j in xrange(1,k):
        #i de 1 a n/k
        for i in xrange(1,(n/k)+1):
            #f_n(k-1)/k(x_((j*k/n)+i),y_((j*(k/n)+i)))
            func
        



if __name__ == '__main__':
    x,y = load_data()
    theta = calc_theta(x,y,10)







