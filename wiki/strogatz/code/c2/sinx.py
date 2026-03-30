import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange


def f(x):
    return np.sin(x)



def rk4logistic(init_cons,dt):
    '''
    simulate logistic equation dxdt=x(1-x)
    init_cons: vector of initial conditions (t_0,x_0) (integers)
    dt: timestep
    '''
    #timevec
    tvec=np.arange(0,10,dt)
    #vector for values
    xvec=np.zeros((np.shape(init_cons)[0],np.shape(tvec)[0])) 

    for con in range(np.shape(init_cons)[0]):
        #set initial condition
        t_0=int(np.round(init_cons[con][0]/dt))
        xvec[con,0:t_0]=np.nan
        xvec[con,t_0]=init_cons[con][1] 
        

        #rk4
        for t in range(len(tvec)-1-t_0):
            k_1=f(xvec[con,t_0+t])*dt
            k_2=f(xvec[con,t_0+t]+0.5*k_1)*dt
            k_3=f(xvec[con,t_0+t]+0.5*k_2)*dt
            k_4=f(xvec[con,t_0+t]+k_3)*dt
            xvec[con,t_0+t+1]=xvec[con,t_0+t]+(1/6)*(k_1+2*k_2+2*k_3+k_4)

    return tvec, xvec

 


#compute
t,x=rk4logistic([(1,-0.01),(0,0.01),(0,6),(1,6.28)],0.01)

#phase portrait
X=np.arange(-4,8,0.4)
T=np.arange(0,10,0.5)

traj_x=f(X)
traj_t=np.ones(np.shape(T))

#position
T,X=np.meshgrid(T,X)
#gradient at each position
traj_t,traj_x=np.meshgrid(traj_t,traj_x)



fig,ax=plt.subplots()

ax.quiver(T,X,traj_t,traj_x,pivot='tail',scale=35,headwidth=1)


for traj in range(np.shape(x)[0]):
    plt.plot(t,x[traj,:],linewidth=3)
plt.show()



