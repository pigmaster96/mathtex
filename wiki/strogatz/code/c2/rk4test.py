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
    init_cons: vector of initial conditions (t_0,x_0) (for now assume t_0=0)
    dt: timestep
    '''
    #timevec
    tvec=np.arange(0,30,dt)
    #vector for values
    xvec=np.zeros((np.shape(init_cons)[0],np.shape(tvec)[0])) 



    
    #rk4
    #for t in range(len(tvec)):
        




X=np.arange(0,30,2)
Y=np.arange(0,30,2)


fig,ax=plt.subplots()
U,V=np.meshgrid(X,Y)
plt.plot(U,V, marker='o',color='k',linestyle='none')
plt.show()



