import math
import numpy as np


N = 10000
delta = 0.1
p = 0.5
num_experiments = 10000

def calculate_phat():
    outcomes = np.random.binomial(n=1,p=1/2,size=N)
    denoms = [i for i in range(1,N+1)]
    phats = np.divide(np.cumsum(outcomes),denoms) # Calculate phat for each n
    return phats

def compute_interval(phat,n):
    interval = np.sqrt(np.divide(np.log(np.divide(2,delta)),np.multiply(2,n)))
    return interval

def compute_valid_interval(phat,n):
    interval = np.sqrt(np.divide(np.add(np.log(np.multiply(n,np.add(n,1),dtype=float)),np.log(np.divide(2,delta))),np.multiply(2,n)))
    return interval

def compute_iterated_interval(phat,n):
    interval = np.sqrt(np.divide(np.add(np.log(np.log(n)),np.log(np.divide(2,delta,dtype=float))),np.multiply(2.0,n)))
    return interval

def check_range(phat,intervals):
    return np.where( abs(phat-p) > intervals)


def part_a():
    in_range = 0
    for experiment in range(num_experiments):
        phats = calculate_phat()
        n = [i for i in range(2,N)]
        intervals = compute_interval(phats[2:],n)
        not_in_interval = check_range(phats[2:],intervals)[0].shape[0]
        if not_in_interval == 0:
            in_range += 1
    proportion = in_range/num_experiments
    print('Proportion : {}'.format(proportion))

def part_b():
    in_range = 0
    for experiment in range(num_experiments):
        phats = calculate_phat()
        n = [i for i in range(2,N)]
        intervals = compute_valid_interval(phats[2:],n)
        not_in_interval = check_range(phats[2:],intervals)[0].shape[0]
        if not_in_interval == 0:
            in_range += 1
    proportion = in_range/num_experiments
    print('Proportion : {}'.format(proportion))


def part_c():
    in_range = 0
    for experiment in range(num_experiments):
        phats = calculate_phat()
        n = [i for i in range(2,N)]
        intervals = compute_iterated_interval(phats[2:],n)
        not_in_interval = check_range(phats[2:],intervals)[0].shape[0]
        if not_in_interval == 0:
            in_range += 1
    proportion = in_range/num_experiments
    print('Proportion : {}'.format(proportion))

if __name__ == '__main__':
    part_a()
    part_b()
    part_c()





