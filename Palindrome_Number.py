

class Solution:
    
    def isPalindrome1(self, x: int) -> bool:
        """
        Easiest solution
        Complexity: O(2n) = O(n)| n = len(str(x))
        """
        s = str(x)
        return s == s[::-1]
    
    def isPalindrome2(self, x: int) -> bool:
        """
        Improvement: only reverse half of the string
        
        Complexity: O(n) | n = len(str(x))   
        """
        s = str(x)
        mid = len(s) // 2
        first_half = s[:mid]
        second_half = s[mid:] if len(s) % 2 == 0 else s[mid+1:]
        return first_half == second_half[::-1]
    
    def isPalindrome3(self, x: int) -> bool:
        """
        Improvements:
            * no reversal needed
            * potential for early stopping if x is not a palindrome
            
        Complexity: O(n/2) = O(n) | n = len(str(x)) 
        ... execution time slightly better
        """
        s = str(x)
        mid = len(s) // 2
        for i in range(mid):
            if not s[i] == s[-(i+1)]:
                return False
        return True
    
    @staticmethod
    def get_divisor(x: int) -> int:
        """
        for x of magnitued p: return 10^(p-1)
        e.g: for 123, return 100
        """
        divisor = 1
        while x / divisor >= 10:
            divisor *= 10
        return divisor
    
    def isPalindrome(self, x: int) -> bool:
        """
        Integer version
        Complexity: still O(n) | n = len(str(x))
        ... no runtime improvement over string method
        """
        if x < 0:
            return False
        
        div = self.get_divisor(x)
        
        while x > 0:
            
            first = x // div
            last = x % 10
            if first != last:
                return False
            
            x = (x % div) // 10  # remove first and last digit
            div /= 100  # drop to same order of magnitue as x
            
        return True
            
