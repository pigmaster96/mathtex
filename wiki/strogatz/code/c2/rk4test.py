import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange


def f(x):
    '''
    logistic model dxdt=x(1-x)
    '''
    return x*(1-x)




def rk4logistic(init_x,dt):
    '''
    simulate logistic equation dxdt=x(1-x)
    init_cons: vector of initial conditions (t_0,x_0) (for now assume t_0=0)
    dt: timestep
    '''
    #timevec
    tvec=np.arange(0,30,dt)
    #vector for values
    xvec=np.zeros(np.shape(tvec)[0]) 
    #set init
    xvec[0]=init_x
 
    #rk4
    for t in range(len(tvec)-1):
        k_1=f(xvec[t])*dt
        k_2=f(xvec[t]+0.5*k_1)*dt
        k_3=f(xvec[t]+0.5*k_2)*dt
        k_4=f(xvec[t]+k_3)*dt
        xvec[t+1]=xvec[t]+(1/6)*(k_1+2*k_2+2*k_3+k_4)


    return xvec, tvec

 



x,t=rk4logistic(0.5,0.2)


X=np.arange(0,30,3)
Y=np.arange(0,5,0.5)


fig,ax=plt.subplots()
U,V=np.meshgrid(X,Y)
plt.plot(U,V, marker='o',color='k',linestyle='none')
plt.plot(t,x)
plt.show()



