class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        a = abs(x)
        print a
        s = str(a)
        
        while True:
            print len(s)
            if len(s) == 1 or len(s) == 0:
                return True
            elif len(s)>1:
                if s[0] == s[-1]:
                    s = s[1:-1]
                else:
                    return False

s = Solution()
print s.isPalindrome(3)
print s.isPalindrome(-42324)
print s.isPalindrome(22)
print s.isPalindrome(-2147447412)
