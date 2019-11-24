
class Solution:
    """
    cases to cover:
    * sign
    * trailing zeros (covered if str is converted to int)
    """

    def reverse(self, x: int) -> int:
        """
        Trivial approach: convert to string
        """
        s = str(abs(x))
        rev = int(s[::-1])

        if rev >= 2**31:
            return 0
        else:
            sign = -1 if x < 0 else 1
            return rev * sign

