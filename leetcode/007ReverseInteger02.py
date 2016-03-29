class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = -1 if x < 0 else 1
        result = int(str(abs(x))[::-1])    
        return result*flag if result <= 2147483647 else 0


s = Solution()
print s.reverse(2048)
