import numpy as cp

class ReLU():
    
    '''
    ReLU is Rectified Linear Activation Function which is mostly used activation function 
    in almost all the convolutional neural networks or deep learning. Despite its name and
    appearance, it’s not linear and provides the same benefits as Sigmoid but with better
    performance.

    The ReLU function is defined as follows:
        
            R(x )= {  z  z>0  }
                   {  0  z<=0 }  
    
    Parameters
    ----------
    x : cp.array
        Array of ouputs of deeplearning layer.

    Returns
    -------
    cp.array
        Array after ReLU function applied .

    '''
    
    def __call__(self, x: cp.array) -> cp.array:
        
        return cp.where(x >= 0, x, 0)

    def gradient(self, x: cp.array) -> cp.array:
        '''
        
        Parameters
        ----------
        x : cp.array
             Array of ouputs of deeplearning layer..

        Returns
        -------
        cp.array
            Array after derivatives of ReLU applied .

        '''
        
        return cp.where(x >= 0, 1, 0)
    
