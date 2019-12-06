#-*- coding:utf-8 -*-
import copy
'''
给n个数，分成k组，使每个组的和尽可能相同
'''

'''
思路:
1.如果是求最优解，尽可能相同表示:生成的每组和的方差最小；暴力搜索:n个数分成k组，有k^n种结果，再这些结果中找出方差最小的为最优解；
2.方法1耗时太长，如果再实际操作过程中，可以用较快的办法找出次优解,从n个数中随机选取k个数形成k组，剩下的n-k个数每次都分配给和最小的组，分配完后计算方差；随机k次，取方差最小的分配结果；
question:为什么要随机,感觉会好一些，如何证明
'''

#求方差
def get_variance(sum_list):
    mean = 1.0*sum(sum_list)/len(sum_list)
    res = 0
    for e in sum_list:
        res += (e-mean)**2
    return res

#解法1
def get_solution_1(data,k):
    n = len(data)
    #每个元素为一个list,表示一种分配方案
    group_list = []
    res = [-1] * n #每个元素的位置初始化为-1
    def bfs(start):#bfs搜索出所有情况
        if start == n:
            group_list.append(copy.deepcopy(res))
        for i in range(start,n):
            if res[i] == -1:
                for j in range(k):
                    res[i] = j
                    start += 1
                    bfs(start)
                    res[i] = -1
                    start -= 1
    bfs(0)
    #求方差最小的分配方案
    min_variance = float("inf")#初始化一个无穷大值
    init_group_list = [-1] * n
    for group in group_list:
        ele_group_dict = {}
        for pos,ele in enumerate(group):
            if ele not in ele_group_dict:
                ele_group_dict[ele] = []
            ele_group_dict[ele].append(data[pos])
        sum_list = []
        for i in range(k):
            if i in ele_group_dict:
                sum_list.append(sum(ele_group_dict[i]))
            else:
                sum_list.append(0)
        variance = get_variance(sum_list)
        if variance < min_variance:
            min_variance = variance
            init_group_list = group
    #输出分配方案
    output_list = [[]  for i in range(k)]
    for pos,ele in enumerate(init_group_list):
        output_list[ele].append(data[pos])
    return output_list

def get_solution_2(data,k):
    pass

if __name__ == '__main__':
    data = [6, 6, 5, 2, 1, 1]
    k = 3
    print get_solution_1(data,k)
    
