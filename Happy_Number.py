"""
https://leetcode.com/problems/happy-number/
"""


class Solution:

    def __init__(self):
        self.seen = set()

    def isHappy(self, n: int) -> bool:

        if int(n) == 1:
            return True
        elif n in self.seen:  # endless cycle
            return False

        self.seen.add(n)
        n = self.isHappy(n=sum(int(digit)**2 for digit in str(n)))

        return n
