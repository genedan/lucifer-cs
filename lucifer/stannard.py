from math import sqrt
from scipy.stats import (
    expon,
    norm,
    randint
)

# for each accident year

# A random number of losses, N, was drawn from a normal distribution with mean 40, variance 60.
# Restricted to be > 0
max(0 ,norm.rvs(loc=40, scale=sqrt(60)))

# Month of loss is uniform
randint.rvs(low=1, high=12)

# Report lag is exponential with mean 18 months

expon.rvs(scale=18)

# Payment lag exponential with mean 12 months
expon.rvs(scale=12)

# Payment amount lognormal with mean 10,400 and variance 34800


# Reserve error V_i, lognormal with mean 1 and variance 2