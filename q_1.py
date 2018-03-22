#!/usr/bin/env python3

import math
import numpy as np

# n : number of tosses per coin
# m : number of coins
# N : number of simulations
# eps : bias in fake coin
# p = 1/2 : True proportion of fair coins

eps = 0.1
N = 10000
p = 1/2

def get_proportions(m,n):
    """
    Get proportion of heads for all m coins, with each coin being tossed n times
    """
    p_hats = []
    # The first coin is 'fake'
    p_hat = np.divide(np.random.binomial(n,p+eps),n) # np.random.binomial returns #wins i.e sum of Xi's, divide by n to get p_hat
    p_hats.append(p_hat)
    for coin in range(m-1):
        p_hat = np.divide(np.random.binomial(n,p),n)
        p_hats.append(p_hat)

    return p_hats

def error_check(m,n):
    """
    Compare proportion of heads of the fake coin with the rest of the (fair) coins.
    Return true if any one coin is found to proportion of heads greater than the fake coin
    """
    p_hats = get_proportions(m,n)
    flag = False
    for idx in range(1,m):
        if p_hats[0]<p_hats[idx]:
            flag = True
            break

    return flag

def bound_compare(m,n):
    """
    For N simulations, compares proportion of errors to the derived bound
    """
    bound = np.multiply((m-1),math.exp(-n*(eps**2)))
    error_count = 0
    for step in range(N):
        if error_check(m,n) is True:
            error_count += 1
    error_proportion = np.divide(error_count,N)
    print('Number of coins = {} Number of tosses = {} Error probablity bound = {} Error Count : {} Error Proportion : {}'.format(m,n,bound,error_count,error_proportion))



if __name__ == '__main__':
    # Experiment with 2 coins
    bound_compare(m=2,n=10)
    bound_compare(m=2,n=100)
    bound_compare(m=2,n=500)
    bound_compare(m=2,n=1000)

    # Experiment with 100 coins
    bound_compare(m=100,n=10)
    bound_compare(m=100,n=100)
    bound_compare(m=100,n=500)
    bound_compare(m=100,n=1000)
