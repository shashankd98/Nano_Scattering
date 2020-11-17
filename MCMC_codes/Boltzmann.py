import numpy as np  
from matplotlib import pyplot as plt  
import random

vx=0
vy=0
vz=0
m=4.64*10**(-26)
kb=1.38*10**(-23)
T=30
step=200
num=10000
vArray=np.zeros(num)
for i in range(num):
    v=np.sqrt(vx**2+vy**2+vz**2)
    vArray[i]=v
    KE=0.5*m*v**2
    dv=step*(2*random.random()-1)
    vxtrail=vx+dv
    vytrail=vy+dv
    vztrail=vz+dv
    vtrail=np.sqrt(vxtrail**2+vytrail**2+vztrail**2)
    KEtrail=0.5*m*vtrail**2
    if np.exp((KE-KEtrail)/kb/T)>=random.random():
        vx=vxtrail
        vy=vytrail
        vz=vztrail

bins=int(1500/25)
hist=np.zeros(bins)
for i in range(num):
    for j in range(bins):
        if 25*j>vArray[i] and 25*(j-1)<vArray[i]:
            hist[j]+=1
            break

xaxis=np.linspace(0,1500,bins)
plt.plot(xaxis,hist)
plt.show()

