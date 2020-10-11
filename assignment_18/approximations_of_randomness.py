from math import log
import sys
sys.path.append('assignment_11')
from kl_divergence_for_monte_carlo_simulations import *

flips = {
    'Justin S': 'HTTH HHTT TTHH TTTH HHTH TTHT HHHH THHT THTT HTHH TTTT HTHT TTHH THTH HTTH HHTH HHHT TTTH HTTH HTHT',
    'Nathan R': 'HTTH HHTH HTTT HTHH HTTH HHHH TTHH TTHT THTT HTHT HHTH TTTT THHT HTTH HTHH THHH HTTH THTT HHHT HTHH',
    'Justin H': 'HHHT HHTH HHTT THHT HTTT HTTT HHHT HTTT TTTT HTHT THHH TTHT TTHH HTHT TTTT HHHH THHH THTH HHHH THHT',
    'Nathan A': 'HTTH HHHH THHH TTTH HTTT THTT HTHT THHT HTTH TTTT HHHH TTHH HHTH TTTH HHHH THTT HTHT TTTT HHTT HHTT',
    'Cayden': 'HTHT HHTT HTTH THTH THHT TTHH HHHH TTTH HHHT HTTT TTHT HHTH HTHH THTT HHHH THTT HTTT HTHH TTTT HTTH',
    'Maia': 'HTHH THTH HTTH TTTT TTHT HHHH HHTT THHH TTHH HHTH THHT HHHH THTT HHTH HTHT TTHH TTHH HHHH TTTT HHHT',
    'Spencer': 'HHHT HTTH HTTT HTHH THTT TTHT TTTT HTTH HHTH TTHT TTHH HTHT THHT TTHT THTT THTH HTTH THHT TTTH HHHH',
    'Charlie': 'HHHH HHHT HHTT HTTT TTTT TTTH TTHH THHH THTH HTHT HHTH HTHH TTHT THTT THTH TTHT HTHT THHT HTTH THTH',
    'Anton': 'HHTH THTH TTTT HTTH THTT TTTH THHH TTHH THHT HHHH TTHT HTTT THTH HHHT HHTH HHHH TTTH HTHT TTTT HHTT',
    'William': 'THTT HHHT HTTH THHT THTH HHHT TTTH HHTH THTH HTHT HHHT TTHT HHHT THTT HHTT TTHH HHTH TTTT THTH TTHT'
}

true_distribution = []
for i in range(5):
    true_distribution.append(probability(i, 4))

for key in flips:
    head_count_list = [0, 0, 0, 0, 0]
    values = flips[key]
    values = list(values.split(" "))
    for trial in values:
        head_counter = 0
        for flip in trial:
            if flip == "H":
                head_counter += 1
        head_count_list[head_counter] += 1
    for i in range(len(head_count_list)):
        head_count_list[i] /= 20
    flips[key] = head_count_list

ordered_list = []
while True:
    for key in flips:
        least_value = kl_divergence(flips[key], true_distribution)
        least_key = key
    for key in flips:
        if kl_divergence(flips[key], true_distribution) < least_value:
            least_value = kl_divergence(flips[key], true_distribution)
            least_key = key
    ordered_list.append(least_key + ": " + str(least_value))
    del flips[least_key]
    if len(flips) == 0:
        print("Most accurate to least accurate:")
        print(ordered_list)
        break

'''Charlie's coin flips were the best approximation for random coin flips
then Cayden's, then mine, then Anton's, etc.'''