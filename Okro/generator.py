############################################################################
#"""
#    Authors: Ismail Dawud Ibrahim
#             Prince Alfred Gyan
#             Francis Billa
#             Franklin Wae Luther
#    Date Created:16th Jul,2018
#     Date Modified: 17th Jul,2018
#     
#     project: Okro -> This python project allows us to check whether a
#             given set of numerical data obeys the "Benford Law" or not
#             and also generate data based on the "Benford Law".
#
#             ReadMore: https://en.wikipedia.org/wiki/Benford%27s_law
#     
#     Deccription: This module makes up for the implementation of the benford's law 
#                 algorithm,thus fuctions for the leading values , lead frequency counts
#                 and ther corresponding percentages, to check for benford compliance.
# """
###########################################################################


import random, math
import benford as bf
from collections import Counter

#Generate maximun and minimum values
def generate(max_value, min_value,target_pop_size):
    probs = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    population = sum([[n] * int(p * 10) for n, p in zip(nums, probs)], [])

    max_value = max_value
    min_value = min_value
    result_pop = []
    target_pop_size = target_pop_size
    while len(result_pop) < target_pop_size:
        s = str(random.choice(population))
        while True:
            r = random.randint(min_value, max_value)
            if str(r).startswith(s):
                break
        result_pop.append(r)
    return result_pop
