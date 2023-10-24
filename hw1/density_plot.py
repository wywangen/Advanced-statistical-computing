import numpy as np
import matplotlib.pyplot as plt
import em

p1=np.load("estimated_p1.npy")
pi=np.load("estimated_pi.npy")
mu_list = np.arange(146, 191.5, 0.5)
K = mu_list.shape[0]
x = np.arange(145, 195, 0.1)
length=x.shape[0]
y = np.zeros(length)
for i in range(length):
    y[i] = sum(pi[0][k]*em.f(x[i], mu_list[k]) for k in range(K))
plt.plot(x,y, label='girl height')


for i in range(length):
    y[i] = sum(pi[1][k]*em.f(x[i], mu_list[k]) for k in range(K))
plt.plot(x,y, label='boy height')
plt.legend()
plt.savefig('height density.png')
