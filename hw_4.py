import numpy as np
import math

delta = 0.1
c = 9

def calculate_epsilon(n):
    """
    VC bound for uncountable function class

    """
    epsilon = 32*math.sqrt((math.log(n+1) + math.log(8) + math.log(1/delta))/n)
    return epsilon


def part_b():
    for n in range(1,100000):
        epsilon = calculate_epsilon(n)
        if epsilon < 1:
            print(n)
            break

def calculate_epsilon_quantized(n):
    """
    VC bound for quantized function class (countable)

    """
    epsilon = 2*math.sqrt((math.log(2+n) + math.log(1/delta))/(2*n)) + c/n
    return epsilon

def part_d():
    for n in range(1,100000):
        epsilon = calculate_epsilon_quantized(n)
        if epsilon < 1:
            print(n)
            break

def generate_samples(n):
    """
    Generate samples (x,y)

    """
    x_s = np.random.uniform(size=n)
    sample_pairs = []
    for x in x_s:
        sample = []
        sample.append(x)
        if x >= 1/3:
            y = 1
        else:
            y = 0
        sample.append(y)
        sample_pairs.append(sample)
    return sample_pairs

def calculate_emp_risk(samples,t):
    """
    Calculate empirical risk for a given (samples,t) combination
    """
    loss = 0
    for sample in samples:
        x = sample[0]
        y = sample[1]
        y_pred = int(x>t)
        loss += int(y_pred != y)
    emp_risk = loss/len(samples)
    return emp_risk

def calculate_minimum_emp_risk(samples):
    """
    Given samples, calculate the empirical risk minimizer (t_min)

    """
    emp_risk = {}
    for sample in samples:
        t = sample[0] # t = xi
        emp_risk[t] = calculate_emp_risk(samples,t)
    t_min = min(emp_risk,key=emp_risk.get) #Find t_min
    return t_min

def calculate_minimum_emp_risk_quantized(samples):
    q = len(samples) # q = n
    emp_risk = {}
    for step in range(q+1):
        t = step/q # t = {0,1/q,...,1}
        emp_risk[t] = calculate_emp_risk(samples,t)
    t_min = min(emp_risk,key=emp_risk.get)
    return t_min

def calculate_excess_risk(t):
    """
    Calculate excess risk for a given t

    """
    excess_risk = ((t-1/3)**2)/2
    return excess_risk

def part_g(n):
    samples = generate_samples(n)

    # Uncountable Class
    t_min = calculate_minimum_emp_risk(samples)
    excess_risk = calculate_excess_risk(t_min)
    bound = calculate_epsilon(n)

    #Quantized Version
    t_min_q = calculate_minimum_emp_risk_quantized(samples)
    excess_risk_q = calculate_excess_risk(t_min_q)
    bound_q = calculate_epsilon_quantized(n)

    print('Class F :: #samples : {} t_min: {} excess_risk :{} VC bound : {}'.format(n,t_min,excess_risk,bound))
    print('Class F_q :: #samples : {} t_min: {} excess_risk :{} Quantized bound : {}'.format(n,t_min_q,excess_risk_q,bound_q))


if __name__ == '__main__':
    part_b()
    part_d()
    part_g(n=10)
    part_g(n=100)
    part_g(n=1000)

