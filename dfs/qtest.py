def q1(arr, target):
    mapping = {}
    for i, v in enumerate(arr):
        print(mapping)
        dis = target - v
        if dis in mapping:
            return mapping[dis], i
        if v not in mapping:
            mapping[v] = i
arr = [1,3,5,7,9]
target = 10
print(q1(arr, target))