"""
给定一个化学式formula（作为字符串），返回每种原子的数量。

原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。

两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。

一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。

给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。
输入:
formula = "Mg(OH)2"
输出: "H2MgO2"
解释:
原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。

输入:
formula = "K4(ON(SO3)2)2"
输出: "K4N2O14S4"
解释:
原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。

"""



from collections import defaultdict
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        formula = "K4(ON(SO3)2)2"
        输出: "K4N2O14S4"
        """
        i,idx = 0,0
        n = len(formula)
        stack = []
        res = defaultdict(lambda x:1)
        while i <n:
            if formula[i] == '(' or formula[i] == ')':
                stack.append(formula[i])
                i += 1
            else:
                if formula[i].isdigit():
                    j = i+1
                    while j < n and formula[j].isdigit():
                        j += 1
                    cnt = int(formula[i:j])
                    i = j
                    if stack[-1] == ')':
                        stack.pop()
                        tmp = []
                        while stack[-1] != '(':
                            tmp.append(stack[-1])
                            res[stack[-1]] = res[stack[-1]] * cnt
                            stack.pop()
                        stack.pop()
                        for k in range(len(tmp)-1,-1,-1):
                            stack.append(tmp[k])
                    else:
                        res[stack[-1]] = res[stack[-1]] * cnt
                else:
                    j = i+1
                    while j<n and formula[j].islower():
                        j += 1
                    one_atom = ''.join(formula[i:j]) + '_' + str(idx)
                    idx += 1
                    stack.append(one_atom)
                    res[one_atom] = 1
                    i = j
        format_res = defaultdict(int)
        for k,v in res.items():
            one_atom = k.split('_')[0]
            format_res[one_atom] = format_res[one_atom] + v
        sorted_format_res = sorted(format_res.items(),key=lambda x:x[0])
        res = ''
        for k,v in sorted_format_res:
            res += str(k)
            res += str(v)
        return res





if __name__ == '__main__':
    formula = 'K4(ON(SO3)2)2'
    s = Solution()
    print(s.countOfAtoms(formula))
