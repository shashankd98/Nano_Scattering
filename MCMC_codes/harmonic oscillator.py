import numpy as np 
import random
from matplotlib import pyplot as plt

def initializeWalkers(N,x):
    for i in range(N):
        x[i]=random.random()-0.5
    return x

def prob(xTrail,x,alpha):
    return np.exp(-2*alpha*(xTrail**2-x**2))

def eLocal(x,alpha):
    return alpha+(0.5-2*alpha**2)*(x**2)

def harmonic():
    N=30
    x=np.zeros(N)
    delta=0.1
    alpha=alphaMin=0
    alphaMax=1.5
    alphaStep=0.1
    yaxis=np.zeros(int((alphaMax-alphaMin)/alphaStep))
    xaxis=np.arange(alphaMin,alphaMax, alphaStep)
    MCSteps=1000
    thermSteps=200
  
    for k in range(int((alphaMax-alphaMin)/alphaStep)):
        x=initializeWalkers(N,x)
        energySum=0
        energySqdSum=0
        for j in range(MCSteps+thermSteps):
            for i in range(N):
                n=int(random.random()*N)
                xTrail=np.random.normal(x[n],delta)
                if prob(xTrail,x[n],alpha)>random.random():
                    x[n]=xTrail
                if j>=thermSteps:
                    energySum+=eLocal(x[n],alpha)
                    energySqdSum+=eLocal(x[n],alpha)**2

        eAve=energySum/N/MCSteps
        eVar=energySqdSum/N/MCSteps-eAve**2
        err=np.sqrt(eVar)/np.sqrt(N*MCSteps)
        yaxis[k]=eAve
        alpha+=alphaStep

    plt.plot(xaxis,yaxis)
    plt.title("30 Walkers, 1000 Steps")
    plt.xlabel("Alpha")
    plt.ylabel("Energy")
    plt.show()


harmonic()



    

