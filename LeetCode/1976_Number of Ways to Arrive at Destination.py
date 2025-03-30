class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        mod = 10**9 + 7

        #建立graph graph[0] = [(v,t)...]
        #graph 為 N*N 矩陣
        graph = [[] for _ in range(n)]
        for u, v, t in roads:
            graph[u].append((v, t)) 
            graph[v].append((u, t))

        #time[i] = 0到i的最短時間 
        time = [float('inf')] * n
        time[0] = 0
        #ways[i] = 0到i的最短時間方法數
        ways = [0] *n
        ways[0] = 1
        # 最小堆：(當前i到該節點的距離, 節點)
        heap = [(0, 0)]

        while heap:
            d, u = heapq.heappop(heap)
            #比最短距離大則跳過
            if d > time[u]:
                continue

            #檢查u點的所有鄰居 
            for v, t in graph[u]:
                #從0到u的距離+當前節點到v距離
                nd = d + t
                #如果比0到v小
                if nd < time[v]:
                    #更新0到v的距離
                    time[v] = nd
                    heapq.heappush(heap, (nd, v))
                    #因為必定經過u
                    ways[v] = ways[u]
                elif nd == time[v]:
                    #取餘數避免過大
                    ways[v] = (ways[v] + ways[u]) % mod
            
        return ways[n-1] % mod

        


# 測試範例
if __name__ == '__main__':
    sol = Solution()

    n = 5
    roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    print(sol.countPaths(n, roads))  # 4

