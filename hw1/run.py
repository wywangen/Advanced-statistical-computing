import numpy as np
import em

sample = np.loadtxt('hw1_dataset.txt')[:,0]
mu_list = np.arange(146, 191.5, 0.5)
K = mu_list.shape[0]
sigma = 0.5
pi = np.ones([2, K])/K

p1=0.5
print(sample)

while 1:
    p1_new, pi_new = em.em(sample, p1, pi, mu_list, sigma)
    eps = max(np.linalg.norm(p1-p1_new), np.linalg.norm(pi-pi_new, ord=1))
    print(eps, p1_new)
    pi=pi_new
    p1=p1_new
    if eps<10**(-3):
        break

print(p1, pi_new)
np.save("estimated_p1.npy", p1)
np.save("estimated_pi.npy", pi)
