class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        flag = 1
        res = 0
        INT_MAX, INT_MIN = 2147483647, -2147483648
        
        s = str.strip()

        if len(s) == 0:
            return 0
        
            
        if s[0] == '+'or s[0] == '-':
            if s[0] == '-':
                flag = -1
            s = s[1:]
            
        if s.isdigit():
            res = int(s)

        else:
            for i in s:
                digit = ord(i) - ord('0')
                if digit <=9 and digit >= 0:
                    res = res*10 + digit
                else:
                    break
            
        res *= flag
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
            
        return res

s = Solution()
print s.myAtoi("+")
print s.myAtoi("0")
print s.myAtoi("1")
print s.myAtoi("+1")
