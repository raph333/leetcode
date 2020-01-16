"""
https://leetcode.com/problems/contains-duplicate-ii/
"""
from typing import List


class Solution:

    @staticmethod
    def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        """
        O(n)
        """
        number2index = dict()

        for i, number in enumerate(nums):
            if number in number2index and abs(i - number2index[number]) <= k:
                return True
            number2index[number] = i

        return False
