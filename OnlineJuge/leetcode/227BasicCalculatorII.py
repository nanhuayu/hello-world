import re

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        stacknum = []
        stackop = []
        table = {'+':1,'-':1,'*':2,'/':2,'#':0}

        s0 = re.split(r"(\D)",s+"#")
        for i in s0:
            if i.isdigit():
                stacknum.append(int(i))
            if i in table:
                stackop.append(i)

        """

        for i in s+"#":
            if i in table:
                stackop.insert(0,i)

        for i in table:s = s.replace(i," ")
        stacknum = [int(i) for i in s.split()][::-1]
        """
        if len(stacknum) == 1:return stacknum[0]
        if len(stacknum) == 0:return 0

        stack = []
        op = []

        for i in range(len(stackop)):
            op.append(stackop[i])
            stack.append(stacknum[i])

            if len(op) < 2:continue
            while len(op) > 1 and table[op[-1]] <= table[op[-2]]:
                op2 = stack.pop()
                op1 = stack.pop()
                opd = op.pop(-2)
                if opd == "+":stack.append(op1+op2)
                elif opd == "-":stack.append(op1-op2)
                elif opd == "*":stack.append(op1*op2)
                elif opd == "/":stack.append(op1//op2)
                else:break
                #if len(op) == 1:break

        return stack[0]


test = Solution()
s = "1+2*3"
print test.calculate(s)