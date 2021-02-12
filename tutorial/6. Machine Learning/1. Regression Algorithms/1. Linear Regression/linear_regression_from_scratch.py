#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 21:22:25 2021

@author: rjn
"""

import numpy as np

class LinearRegression:
    '''
    alpha : Learning rate
            float
    iteration : No of training cycle
                int            
    '''
    
    def __init__(self, alpha = 0.05, iteration = 1000,norm = False):
        
        self.alpha = alpha
        self.iteration = iteration
        self.norm = norm 
        self.w_ = np.zeros((2, 1))
        
    def forward(self, x):
        
        try:
            yhat = np.dot(x,self.w_)
            return yhat    

            
        except (RuntimeError, TypeError, NameError):
            print("(RuntimeError or TypeError or  NameError)")
                        
    
    def loss(self,m,yhat, ytrue):
        '''
        calculates loss values between yhat and ytrue
        '''
        loss = np.sum((yhat - ytrue) ** 2) / (2 * m)
        return loss 
    
    def opitimizes(self,m, yhat,y,x):
        '''
        optimizing theta (w_) using GD 
        '''
        grad = (1/m) * np.dot(x.T ,(yhat - y)) 
        self.w_ -= self.alpha * grad
        
    def concat(self,x,y):
        x = x.reshape(-1,1)
        y = y.reshape(-1,1)
        a = np.ones(len(x)).reshape(-1,1)
        x = np.concatenate((a,x),axis =1)
        return x,y
    
    def fit(self,x,y):
        
        """ Predicts the value after the model has been trained.
        Parameters
        ----------
        x : array-like, shape = [n_samples, n_features]
        y : array-like, shape = [n_samples, n_features]
        """
        self.loss_ = []
        m = x.shape[0]
        
        if self.norm:
            x = (x - min(x)) / (max(x) - min(x))
            y = (y - min(y)) / (max(y) - min(y))
            
        x,y = self.concat(x,y)
                
        for i in range(self.iteration):
            yhat = self.forward(x)
            lss = self.loss(m, yhat , y)
            if i % 10000 == 0:
                print(lss)
                
            self.loss_.append(lss)
            
            self.opitimizes(m,yhat, y,x)
            
        return self
    
    def predict(self, x):
        """ Predicts the value after the model has been trained.
        Parameters
        ----------
        x : array-like, shape = [n_samples, n_features]
        Returns
        -------
        Predicted value
        """
        return np.dot(x, self.w_)
    
    def score(self,x,y):
        
        """ Predicts the value after the model has been trained.
        Parameters
        ----------
        x : array-like, shape = [n_samples, n_features]
        y : array-like, shape = [n_samples, n_features]
        Returns
        -------
        r2_score value
        """
        x,y = self.concat(x,y)
        yhat = self.forward(x)
        ssr = np.sum((yhat - y)**2)

        #  total sum of squares
        sst = np.sum((y - np.mean(y))**2)

        # R2 score
        r2_score = 1 - (ssr/sst)
        
        return r2_score