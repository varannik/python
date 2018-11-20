# mean and standard deviation

import numpy as np
from scipy.stats import moment
import matplotlib.pyplot as plt
import math
import seaborn as sns


# generate random sample by known parameters
mu = 1
sigma = 0.1
KnewData = np.random.normal(mu, sigma, 1000)

knowData_array = np.array(KnewData)

# find density parameters
mu_bar = sum(KnewData) / len(KnewData)
sigma_bar = sum((knowData_array - mu_bar) ** 2) / len(KnewData)

# use scipy library to find methods
FirstMoment = moment(KnewData, moment=1)
SecondMoment = moment(KnewData, moment=2)

# generate random sample by estimated parameters
UnKnewData = np.random.normal(mu_bar, math.sqrt(sigma_bar), 1000)


sns.distplot(KnewData, hist=False)
sns.distplot(UnKnewData, hist=False)
plt.show()

print('FirstMoment:', FirstMoment)
print('SecondMoment:', math.sqrt(SecondMoment))
print('manual first moment:', mu_bar)
print('manual second metod:', math.sqrt(sigma_bar))
