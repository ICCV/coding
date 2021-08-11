#-*- coding:utf-8 -*-

def format_list(str1):
    str1 = str1.strip('[]')
    res = []
    stack = []
    tmp_dict_str = ''
    for s in str1:
        if tmp_dict_str=='' and (s==',' or s==' '):
            continue
        if s=='{':
            stack.append('{')
        if s=='}':
            stack.pop()
        tmp_dict_str = tmp_dict_str+s
        if (not stack) and tmp_dict_str:
            res.append(eval(tmp_dict_str))
            tmp_dict_str=''
    return res
str1 = "[{'a':{'b':5}},{'c':{'d':6}}]"
print(format_list(str1))
