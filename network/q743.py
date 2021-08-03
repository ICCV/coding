class Solution:
    def networkDelayTime(self, times,n,k):
        used = [False] * n
        dis = [float('inf')] * n
        cost = [[float('inf')] * n for _ in range(n)]
        for x,y,time in times:
            cost[x-1][y-1] = time
        dis[k-1] = 0
        while True:
            v = -1
            for u in range(n):
                if not used[u] and (v==-1 or dis[u]<dis[v]):
                    v = u
            used[v] = True
            if v==-1:
                break
            for i in range(n):
                dis[i] = min(dis[i],dis[v]+cost[v][i])
        return max(dis) if max(dis) < float('inf') else -1
if __name__ == '__main__':
    s = Solution()
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    print(s.networkDelayTime(times,n,k))