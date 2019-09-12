import operator
from functools import reduce
import math

def ncr(n, r):
    assert n >= r
    r = min(r, n-r)
    numerator = reduce(operator.mul, range(n, n-r, -1), 1)
    denominator = reduce(operator.mul, range(1, r+1), 1)
    return  numerator / denominator

def prob_worse_split(k, alpha):
    assert alpha < 0.5
    result = 0
    for i in range(math.ceil(k/2), k+1):
        result += alpha**i * (1 - alpha)**(k-i) * ncr(k, i)
    return 2 * result