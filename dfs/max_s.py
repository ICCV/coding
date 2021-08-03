def get_max_back(arr):
    dp = [0]*len(arr)
    max_back = 0
    if len(arr) == 0:
        return 0
    for i in range(1,len(arr)):
        if arr[i]>=arr[i-1]:
            back = max(0,dp[i-1]-abs(arr[i]-arr[i-1]))
        else:
            back = dp[i-1]+abs(arr[i]-arr[i-1])
        dp[i] = back
        if back>max_back:
            max_back = back
    return  max_back
arr = [3,2,6,4,10,7]
print(get_max_back(arr))




