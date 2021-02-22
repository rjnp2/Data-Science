import numpy as cp

class Sigmoid():
    
    '''
    
    A Sigmoid function is a mathematical function which has a characteristic S-shaped curve.
    Normally used to refer specifically to the logistic function, also called the logistic
    sigmoid function.sigmoid functions have the property that they map the entire number line 
    into a small range such as between 0 and 1,so one use of a sigmoid function is to convert 
    a real value into one that can be interpreted as a probability.
    
    The logistic sigmoid function is defined as follows:
        
        S(x) =   _____1_______ where exp is exponential
                ( 1 + exp(-x))
                
     With the help of Sigmoid activation function, we are able to reduce the loss during
     the time of training because it eliminates the gradient problem in machine learning 
     model while training.   
     
    Parameters
    ----------
    x : cp.array
        Array of ouputs of deeplearning layer.

    Returns
    -------
    cp.array
        Array after sigmoid function applied .
            
    '''
	
    def __call__(self, x: cp.array) -> cp.array:
        
        return 1 / (1 + cp.exp(-x))

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
        return self.__call__(x) * (1 - self.__call__(x))

