class Solution:

    def __init__(self):

        self.map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s: str) -> int:

        ints = [self.map[c] for c in s]
        sum_ = 0
        i = 0

        while i < len(ints):

            # just add next integer: e.g. 'X': + 10
            if i == len(ints) - 1 or ints[i] >= ints[i + 1]:
                sum_ += ints[i]
                i += 1

            # combine two integers: e.g. 'IX' = 10 - 1 = 9
            else:
                sum_ += ints[i + 1] - ints[i]
                i += 2

        return sum_
