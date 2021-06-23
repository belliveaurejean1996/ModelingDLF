
import numpy as np
import matplotlib.pyplot as plt

angle = []
for i in range(1000):
    mu, sigma = 90, 50 # mean and standard deviation
    s = np.random.normal(mu, sigma, 1)

    if s > 90:
        s = s - 180

    angle.append(s) 


mu, sigma = 90, 50 # mean and standard deviation
s2 = np.random.normal(mu, sigma, 1000)




#count, bins, ignored = plt.hist(angle, 30, density=True)
#plt.show()