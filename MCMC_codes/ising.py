import numpy as np
import random
from matplotlib import pyplot as plt

def initialize(rows, columns):
    return np.ones((rows,columns))

def neighbours(spin_array, lattice_size, x,y):
    left=(x,y-1)
    right=(x,(y+1)%lattice_size)
    bottom=((x+1)%lattice_size,y)
    top=(x-1,y)
    return [spin_array[left[0], left[1]],
            spin_array[right[0], right[1]],
            spin_array[top[0], top[1]],
            spin_array[bottom[0], bottom[1]]]

def energy(spin_array, lattice_size, x,y):
    return 2*spin_array[x,y]*sum(neighbours(spin_array, lattice_size, x,y))

def ising():
    lattice_size=40
    sweeps=1000
    thermSteps=int(sweeps/5)
    temps=np.arange(0.1,5.0,0.1)
    avg_mag=np.ones(np.size(temps))
    avg_en=np.ones(np.size(temps))
    avg_spc_heat=np.ones(np.size(temps))
    c=0
    for temp in temps:
        spin_array=initialize(lattice_size, lattice_size)
        mag = np.zeros(sweeps)
        en=np.zeros(sweeps)
        e2=0
        e1=0
        for sweep in range(sweeps+thermSteps):
            for i in range(lattice_size):
                for j in range(lattice_size):
                    e = energy(spin_array, lattice_size, i, j)
                    if e <= 0:
                        spin_array[i, j] *= -1
                    elif np.exp((-1.0 * e)/temp) > random.random():
                        spin_array[i, j] *= -1
            if sweep>=thermSteps:
                mag[sweep-thermSteps] = abs(sum(sum(spin_array))) / (lattice_size ** 2)
                en[sweep-thermSteps] = energy(spin_array,lattice_size,i,j)/ (lattice_size ** 2)
                e1 = e1 + energy(spin_array,lattice_size,i,j)               
                e2 = e2 + energy(spin_array,lattice_size,i,j)**2


        avg_mag[c]=sum(mag)/sweeps
        avg_en[c]=sum(en)/sweeps
        e1=e1/sweeps
        e2=e2/sweeps
        avg_spc_heat[c]=(e2-e1**2)/(temp**2)
        c=c+1

    plt.plot(temps,avg_mag)
    plt.title("40 by 40 Lattice")
    plt.xlabel("Temperature")
    plt.ylabel("Magnetization")
    plt.show()


ising()



