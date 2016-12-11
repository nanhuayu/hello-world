class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if heights == []:return 0
        h_list = [[0,-1]]
        ret = 0
        for i in range(len(heights)):
            while h_list[-1][0] > heights[i]:
                temp = h_list.pop()
                ret = max(temp[0]*(i-h_list[-1][1]-1),ret)
            h_list.append([heights[i],i])
            
        while len(h_list)>1:
            temp = h_list.pop()
            ret = max(temp[0]*(len(heights)-h_list[-1][1]-1),ret)
            
        return ret

sol=Solution()
print sol.largestRectangleArea([1,2])