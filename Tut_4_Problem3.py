import numpy as np
import matplotlib.pyplot as plt

n=100
rho=np.zeros(n)
rho[n/3:2*n/3]=1
v=-1.0
dx=1.0
x=np.arange(n)*dx

plt.clf()
plt.axis([0,n,0,1.1])
plt.plot(x,rho)
plt.draw()
plt.show()

dt=1.0
for step in range(0,250):
    drho=rho[1:]-rho[0:-1]
    rho[1:]=rho[1:]-v*dt/dx*drho
    rho[0]=rho[-1]
    plt.clf()
    plt.plot(x,rho)
    plt.draw()
    plt.show()

#Mass moves from right to left as time increases. Once the mass is out of frame, a new mass enters, this is expected since it is periodic. Amplitudes increase as time increases as well.
