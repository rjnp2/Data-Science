import numpy as cp

class Softmax():
    
    '''
    The softmax function is a generalization of the logistic function to multiple dimensions.
    It is used in multinomial logistic regression and is often used as the last activation
    function of a neural network to normalize the output of a network to a probability 
    distribution over predicted output classes.
    
    The softmax function takes as input a vector z of K real numbers, and normalizes it into 
    a probability distribution consisting of K probabilities proportional to the exponentials
    of the input numbers.
    
    The Softmax function is defined as follows:
        
        softmax(x) =  ___exp(xi)____ where exp is exponential function
                           ∑ exp(x)
                          
    Parameters
    ----------
    x : cp.array
        Array of ouputs of deeplearning layer.

    Returns
    -------
    cp.array
        Array after Softmax function applied .
    
    '''
    
    def __call__(self, x: cp.array) -> cp.array:
        
        e_x = cp.exp(x)
        return e_x / cp.sum(e_x, axis=-1, keepdims=True)

    def gradient(self, x: cp.array) -> cp.array:
        '''
        
        Parameters
        ----------
        x : cp.array
             Array of ouputs of deeplearning layer..

        Returns
        -------
        cp.array
            Array after derivatives of Softmax applied .

        '''
        
        p = self.__call__(x)
        return p * (1 - p)
