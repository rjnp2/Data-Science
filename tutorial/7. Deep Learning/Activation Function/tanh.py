import numpy as cp

class Tanh():
    '''
    The tanh function is just another possible functions that can be used as a nonlinear activation function between layers of a neural network. 
    Tanh will map values to be between -1 and 1.
    the tanh function is that the derivative can be expressed in terms of the function itself. 
    The logistic Tanh function is defined as follows:
        
        T(x) =   _exp(x)-exp(-x)_ where exp is exponential
                  exp(x)+exp(-x)
    '''
    def __call__(self, x: cp.array) -> cp.array:
        
        return cp.exp(x)-cp.exp(-x))/(cp.exp(x)+cp.exp(-x))

    def gradient(self, x: cp.array) -> cp.array:
        '''
        
        Parameters
        ----------
        x : cp.array
             Array of ouputs of deeplearning layer..

        Returns
        -------
        cp.array
            Array after derivatives of sigmoid applied .

        '''        
        return (1 - self.__call__(x) ** 2)
