class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs == []:
            return ""
        lenstr = min([len(s) for s in strs])
        for i in range(lenstr):
            if len({s[i] for s in strs}) > 1:
                return strs[0][:i]
            
        return strs[0][:lenstr]



s = Solution()
a = ["123","12","124"]
b = []

print s.longestCommonPrefix(a)
print s.longestCommonPrefix(b)
