from math import log
import sys
sys.path.append('assignment_7')
from monte_carlo_coin_flips import *


def kl_divergence(p, q):
    assert len(p) == len(q)
    result = 0
    for i in range(len(p)):
        p_term = p[i]
        q_term = q[i]
        if p_term == 0 or q_term == 0:
            continue
        result += p_term * log(p_term/q_term)
    return round(result, 6)

p = [0.2, 0.5, 0, 0.3]
q = [0.1, 0.8, 0.1, 0]
print("Asserting that 'kl_divergence' works...")
assert kl_divergence(p, q) == -0.096372
print("PASSED")
print("\n")

print("Computing KL divergence for MC solutions...")
q = []
for i in range(9):
    q.append(probability(i, 8))

print("100 samples:")
p = []
for i in range(9):
    p.append(monte_carlo_probability(i, 8, 100))
print("KL Divergence = " + str(kl_divergence(p, q)))
print("1,000 samples:")
p = []
for i in range(9):
    p.append(monte_carlo_probability(i, 8, 1000))
print("KL Divergence = " + str(kl_divergence(p, q)))
print("10,000 samples:")
p = []
for i in range(9):
    p.append(monte_carlo_probability(i, 8, 10000))
print("KL Divergence = " + str(kl_divergence(p, q)))

'''
As the number of samples increases, the KL divergence approaches 0
because the error is lowered.
'''
