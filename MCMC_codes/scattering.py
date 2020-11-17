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

def prob(r,alpha,beta,k):
    return np.exp(-2*alpha*norm(r))+np.exp(2*beta*norm(r))+2*np.exp((beta-alpha)*norm(r))+2*np.exp(-alpha*norm(r))*np.cos(k*norm(r))+2*np.exp(beta*norm(r))*np.cos(k*norm(r))+1

def eLocal(r,alpha,beta,k):
    return 1/norm(r)-1/(norm(r))**2-alpha**2-beta**2+k**2


def scattering():
    N=50
    r=np.zeros((N,3))
    delta=0.1
    alpha=alphaMin=0
    alphaMax=20
    alphaStep=1
    beta=betaMin=0
    betaMax=20
    betaStep=1
    k=1000
    eAveMin=123123
    alphaTrue=0
    betaTrue=0
    zaxis=np.zeros((int((alphaMax-alphaMin)/alphaStep),int((betaMax-betaMin)/betaStep)))
    xaxis=np.zeros((int((alphaMax-alphaMin)/alphaStep),int((betaMax-betaMin)/betaStep)))
    yaxis=np.zeros((int((alphaMax-alphaMin)/alphaStep),int((betaMax-betaMin)/betaStep)))
    for i in range(int((alphaMax-alphaMin)/alphaStep)):
        for j in range(int((betaMax-betaMin)/betaStep)):
            xaxis[i][j]=alphaMin+i*alphaStep
            yaxis[i][j]=betaMin+j*betaStep
    MCSteps=1000
    thermSteps=200
  
    for k in range(int((alphaMax-alphaMin)/alphaStep)):
        beta=betaMin
        for l in range(int((betaMax-betaMin)/betaStep)):
            r=initializeWalkers(N,r)
            energySum=0
            energySqdSum=0
            for j in range(MCSteps+thermSteps):
                for i in range(N):
                    n=int(random.random()*N)
                    r_trail=np.random.normal(r[n],delta)
                    if norm(r_trail)!=0:
                        if prob(r_trail,alpha,beta,k)/prob(r[n],alpha,beta,k)>random.random():
                            r[n]=r_trail
                        if j>=thermSteps:
                            energySum+=eLocal(r[n],alpha,beta,k)
                            energySqdSum+=eLocal(r[n],alpha,beta,k)**2

            eAve=energySum/N/MCSteps
            eVar=energySqdSum/N/MCSteps-eAve**2
            err=np.sqrt(eVar)/np.sqrt(N*MCSteps)
            zaxis[k][l]=eAve
            if eAve<eAveMin:
                eAveMin=eAve
                alphaTrue=alpha
                betaTrue=beta

            beta+=betaStep
        alpha+=alphaStep

    errmin=zaxis.min()
    print(errmin)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('Alpha')
    ax.set_ylabel('Beta')
    ax.set_zlabel('Energy')
    ax.plot_wireframe(xaxis,yaxis,zaxis)
    plt.show()

scattering()