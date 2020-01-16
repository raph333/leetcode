"""
https://leetcode.com/problems/contains-duplicate
"""

from typing import List


class Solution:

    @staticmethod
    def containsDuplicate1(nums: List[int]) -> bool:
        """
        trivial and slow
        """
        return len(set(nums)) != len(nums)

    @staticmethod
    def containsDuplicate2(nums: List[int]) -> bool:
        """
        sorting: O(n * log n)
        """
        nums_sorted = sorted(nums)  # O(n * log n)
        for i in range(len(nums_sorted) - 1):  # O(n)
            if nums_sorted[i] == nums_sorted[i + 1]:
                return True

    @staticmethod
    def containsDuplicate(nums: List[int]) -> bool:
        """
        early stopping: best asymptotically (maybe slower than sorting for small input data)
        O(n)
        """
        number_set = set()
        for number in nums:
            if number in number_set:
                return True
            number_set.add(number)

