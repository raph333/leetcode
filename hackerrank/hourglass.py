"""
https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""

import math
from itertools import product


def hourglassSum(arr):
    max_sum = -math.inf

    for i, j in product(range(len(arr) - 2), range(len(arr[0]) - 2)):
        sum_ = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
        max_sum = max(max_sum, sum_)

    return max_sum
