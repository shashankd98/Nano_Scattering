import numpy as np 
import random
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def initializeWalkers(N,r):
    for i in range(N):
        for j in range(3):
            r[i][j]=random.random()-0.5
    return r

def norm(R):
    return np.sqrt(R[0]**2+R[1]**2+R[2]**2)

def dist(r_1,r_2):
    return np.sqrt((r_1[0]-r_2[0])**2+(r_1[1]-r_2[1])**2+(r_1[2]-r_2[2])**2)

def prob(r_1,r_2,r_1_trail,r_2_trail,alpha):
    return np.exp(-2*alpha*(norm(r_1_trail)+norm(r_2_trail)-norm(r_1)-norm(r_2)))

def eLocal(r_1,r_2,alpha):
    return -alpha**2+alpha/norm(r_1)+alpha/norm(r_2)-2/norm(r_1)-2/norm(r_2)+1/dist(r_1,r_2)


def helium():
    N=50
    r_1=np.zeros((N,3))
    r_2=np.zeros((N,3))
    delta=0.1
    alpha=alphaMin=1
    alphaMax=2.7
    alphaStep=0.1
    yaxis=np.zeros(int((alphaMax-alphaMin)/alphaStep))
    xaxis=np.arange(alphaMin,alphaMax, alphaStep)
    MCSteps=1000
    thermSteps=200
  
    for k in range(int((alphaMax-alphaMin)/alphaStep)):
        r_1=initializeWalkers(N,r_1)
        r_2=initializeWalkers(N,r_2)
        energySum=0
        energySqdSum=0
        for j in range(MCSteps+thermSteps):
            for i in range(N):
                n=int(random.random()*N)
                r_1_trail=np.random.normal(r_1[n],delta)
                r_2_trail=np.random.normal(r_2[n],delta)
                if prob(r_1[n],r_2[n],r_1_trail,r_2_trail,alpha)>random.random():
                    r_1[n]=r_1_trail
                    r_2[n]=r_2_trail
                if j>=thermSteps:
                    energySum+=eLocal(r_1[n],r_2[n],alpha)
                    energySqdSum+=eLocal(r_1[n],r_2[n],alpha)**2

        eAve=energySum/N/MCSteps
        eVar=energySqdSum/N/MCSteps-eAve**2
        err=np.sqrt(eVar)/np.sqrt(N*MCSteps)
        yaxis[k]=eAve
        alpha+=alphaStep

    plt.plot(xaxis,yaxis)
    plt.title("50 Walkers, 1000 Steps")
    plt.xlabel("Alpha")
    plt.ylabel("Energy")
    plt.show()
    plt.show()


helium()




        
