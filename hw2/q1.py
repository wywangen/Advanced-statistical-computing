import numpy as np
import scipy
from functools import cache
from pynverse import inversefunc
import matplotlib.pyplot as plt


mu=1
c=3
sigma=np.sqrt(5)

@cache
def cdf(x):
    return scipy.stats.norm.cdf(x, loc=mu, scale=sigma)

def cdf_truc(x):
    # if x<c:
    #     return 0
    # else:
    return (cdf(x)-cdf(c))/(1-cdf(c))

def transform(u):
    return inversefunc(cdf_truc, u)


sample_size=3
x = np.arange(sample_size)

y =  scipy.stats.uniform.rvs(size=sample_size)  
y = transform(y)        
plt.plot(x,y, label='girl height')





