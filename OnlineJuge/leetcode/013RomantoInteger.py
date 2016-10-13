class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        var = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        temp = 0
        res = 0
        
        for i in s:
            """if var[i] > temp:
                res += var[i] - 2*temp
            else:
                res += var[i]"""
            now = var[i]
            res += now - 2*temp if now > temp else now
            temp = now
            
        return res

s = Solution()
print s.romanToInt("V")
print s.romanToInt("VIII")
print s.romanToInt("XCIX")
print s.romanToInt("CMXCIX")
