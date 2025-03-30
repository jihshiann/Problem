class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        mod = 10**9 + 7

        #�إ�graph graph[0] = [(v,t)...]
        #graph �� N*N �x�}
        graph = [[] for _ in range(n)]
        for u, v, t in roads:
            graph[u].append((v, t)) 
            graph[v].append((u, t))

        #time[i] = 0��i���̵u�ɶ� 
        time = [float('inf')] * n
        time[0] = 0
        #ways[i] = 0��i���̵u�ɶ���k��
        ways = [0] *n
        ways[0] = 1
        # �̤p��G(��ei��Ӹ`�I���Z��, �`�I)
        heap = [(0, 0)]

        while heap:
            d, u = heapq.heappop(heap)
            #��̵u�Z���j�h���L
            if d > time[u]:
                continue

            #�ˬdu�I���Ҧ��F�~ 
            for v, t in graph[u]:
                #�q0��u���Z��+��e�`�I��v�Z��
                nd = d + t
                #�p�G��0��v�p
                if nd < time[v]:
                    #��s0��v���Z��
                    time[v] = nd
                    heapq.heappush(heap, (nd, v))
                    #�]�����w�g�Lu
                    ways[v] = ways[u]
                elif nd == time[v]:
                    #���l���קK�L�j
                    ways[v] = (ways[v] + ways[u]) % mod
            
        return ways[n-1] % mod

        


# ���սd��
if __name__ == '__main__':
    sol = Solution()

    n = 5
    roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    print(sol.countPaths(n, roads))  # 4

