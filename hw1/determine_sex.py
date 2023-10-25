import numpy as np
from em import f

m1=400
m2=600
m3=1000
p1=np.load("estimated_p1.npy")
pi_list=np.load("estimated_pi.npy")
x = np.loadtxt('hw1_dataset.txt')[:, 0]
mu_list = np.arange(146, 191.5, 0.5)
K=pi_list.shape[1]

c = np.zeros([2, m3, K])
for i in range(m3):
    sum1 = np.sum(np.fromiter((pi_list[0][k]*f(x[m1+m2+i], mu_list[k]) for k in range(K)), float))
    sum2 = np.sum(np.fromiter((pi_list[1][k]*f(x[m1+m2+i], mu_list[k]) for k in range(K)), float))
    sum = p1*sum1+(1-p1)*sum2
    for k in range(K):
        c[0][i][k] = p1*pi_list[0][k]*f(x[m1+m2+i], mu_list[k])/sum
    for k in range(K):
        c[1][i][k] = (1-p1)*pi_list[1][k]*f(x[m1+m2+i], mu_list[k])/sum

determine_sex=np.zeros([2,m3])
for i in range(m3):
    determine_sex[0, i] = x[m1+m2+i]
    if np.sum(c[0, i, :])>np.sum(c[1, i, :]):
        determine_sex[1, i] = 1
    else:
        determine_sex[1, i] = 2
print(determine_sex)
np.save("column of gender.npy", determine_sex)
