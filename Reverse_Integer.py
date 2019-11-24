
class Solution:

    def reverse1(self, x: int) -> int:
        """
        Trivial approach: convert to string
        """
        s = str(abs(x))
        rev = int(s[::-1])

        if rev >= 2 ** 31:
            return 0
        else:
            sign = -1 if x < 0 else 1
            return rev * sign

    def reverse(self, x: int) -> int:
        """
        Integer-only version
        """
        sign = -1 if x < 0 else 1
        num = abs(x)
        rev = 0

        while num > 0:
            trailing_digit = num % 10
            num //= 10

            rev *= 10
            rev += trailing_digit

            if rev >= 2 ** 31:
                return 0

        return rev * sign

