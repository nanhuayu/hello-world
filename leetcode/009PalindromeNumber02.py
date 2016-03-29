class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        s = str(x)
        return s == s[::-1] if x >= 0 else False


s = Solution()
print s.isPalindrome(3)
print s.isPalindrome(-42324)
print s.isPalindrome(22)
print s.isPalindrome(-2147447412)
