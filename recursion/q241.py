class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        def helper(expression):
            if ('+' not in expression) and ('-' not in expression) and ('*' not in expression):
                return [int(expression)]
            res = []
            i= 0
            while i <=len(expression)-1:
                if expression[i] in ['+','-','*']:
                    a = helper(expression[:i])
                    b = helper(expression[i+1:])
                    for a1 in a:
                        for b1 in b:
                            if expression[i] == '+':
                                res.append(a1+b1)
                            elif expression[i] == '-':
                                res.append(a1-b1)
                            else:
                                res.append(a1*b1)
                i += 1
            return res
        return helper(expression)


if __name__ == '__main__':
    ob = Solution()
    expression = '10+5'
    print(ob.diffWaysToCompute(expression))


