class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        point = 0
        result = 0
        
        if x < 0:
            flag = 0
            x = -x
            
        
        while x <> 0:
            result *= 10
            point = x - x / 10 * 10
            x /= 10
            result += point
            
        if flag == 0:
            result = -result
            
        return result
