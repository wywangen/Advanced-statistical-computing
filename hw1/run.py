import numpy as np

a = np.loadtxt('hw1_dataset.txt')
mu = np.arange(146, 191.5, 0.5)
K = mu.shape[0]
sigma = 0.5
pi = np.zeros([2, K])
print(pi[0][2])
pi[0][0] = 1
pi[1][0] = 1
p1=0.5
m1=600
m2=400
n=2000
p1_new = 0
for i in range(100):
    p1_new = (m1 + (n - m1 - m2) * p1) / n
    for k in range(K):
        pi[0][k] = (m1*pi[0][k]+p1*pi[0][k]*(n-m1-m2))/(m1+(n-m1-m2)*p1)
        pi[1][k] = (m2 * pi[1][k] + (1-p1) * pi[1][k] * (n - m1 - m2))/(m2+(n-m1-m2)*(1-p1))
    p1 = p1_new
    if i>90:
        print(pi)

