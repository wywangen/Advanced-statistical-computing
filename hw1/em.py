import numpy as np
import scipy

m1=600
m2=400
m3=1000

def f(x, mu, sigma=0.5):
    return scipy.stats.norm.pdf(x, loc=mu, scale=sigma)

def em(x, p1, pi_list, mu_list, sigma):
    K = pi_list.shape[1]
    a = np.zeros([m1, K])
    for i in range(m1):
        sum = np.sum(pi_list[0][k]*f(x[i], mu_list[k]) for k in range(K))
        for k in range(K):
            a[i][k] = pi_list[0][k]*f(x[i], mu_list[k])/sum

    b = np.zeros([m2, K])
    for i in range(m2):
        sum = np.sum(pi_list[1][k]*f(x[m1+i], mu_list[k]) for k in range(K))
        for k in range(K):
            b[i][k] = pi_list[1][k]*f(x[m1+i], mu_list[k])/sum
    
    c = np.zeros([2, m3, K])
    for i in range(m3):
        sum1 = np.sum(pi_list[0][k]*f(x[m1+m2+i], mu_list[k]) for k in range(K))
        sum2 = np.sum(pi_list[1][k]*f(x[m1+m2+i], mu_list[k]) for k in range(K))
        sum = p1*sum1+(1-p1)*sum2
        for k in range(K):
            c[0][i][k] = p1*pi_list[0][k]*f(x[m1+m2+i], mu_list[k])/sum
        for k in range(K):
            c[1][i][k] = (1-p1)*pi_list[1][k]*f(x[m1+m2+i], mu_list[k])/sum

    p_new=(m1+np.sum(c[0]))/(m1+m2+np.sum(c))
    pi_list_new = np.zeros([2, K])

    for k in range(K):
        pi_list_new[0][k]=(np.sum(a[:, k])+np.sum(c[0, :, k]))/(np.sum(a)+ np.sum(c[0]))
        pi_list_new[1][k]=(np.sum(b[:, k])+np.sum(c[1, :, k]))/(np.sum(b)+ np.sum(c[1]))
        
    return p_new, pi_list_new
    

if __name__=="__main__":
    a=np.arange(24).reshape([2,3,4])
    print(np.sum(a))
