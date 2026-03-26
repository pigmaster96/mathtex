import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange


def f(x):
    '''
    logistic model dxdt=x(1-x)
    '''
    return x*(1-x)




def rk4logistic(init_cons,dt):
    '''
    simulate logistic equation dxdt=x(1-x)
    init_cons: vector of initial conditions (t_0,x_0)
    dt: timestep
    '''
    #timevec
    tvec=np.arange(0,30,dt)
    #vector for values
    xvec=np.zeros((np.shape(init_cons)[0],np.shape(tvec)[0])) 

    
    #rk4
    for cond in trange(len(init_cons)):
        
        for t in range(len(tvec)):
        





rk4logistic([[0,1]],0.1)
