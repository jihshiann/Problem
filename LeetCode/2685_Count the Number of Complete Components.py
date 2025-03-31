class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = [False] * n
        complete_count = 0
        # 建立graph(dict)
        # {0 :set(), 1:set()...}
        graph = {i: set() for i in range(n)}
        for u, v in edges:
            graph[u].add(v) #{0:{1}}
            graph[v].add(u)
        
        # 所有節點檢查連通的邊
        for i in range(n):
            if not visited[i]:
                #連通的點
                con_nodes = []
                stack = [i]
                visited[i] = True
                # 使用 DFS 
                while stack:
                    node = stack.pop()
                    #連通的點包含自己
                    con_nodes.append(node)
                    #檢查連通的點
                    for nei in graph[node]:
                        if not visited[nei]:
                            visited[nei] = True
                            stack.append(nei)
                
                # con_nodes的數量 = 與i連通節點數
                r = len(con_nodes)
                # 對於單個節點，默認認為是完全連通（完全圖的定義在只有一個頂點時成立）
                if r == 1:
                    complete_count += 1
                    continue
                
                
                comp_set = set(con_nodes)
                edge_count = 0
                # 計算這個圖的邊數
                for node in con_nodes:
                    # 僅統計相連的邊
                    for nei in graph[node]:
                        if nei in comp_set:
                            edge_count += 1
                edge_count //= 2  # 每條邊被計算了兩次
                
                # 完全圖需要的邊數
                required = r * (r - 1) // 2
                if edge_count == required:
                    complete_count += 1
        
        return complete_count

        


# 測試範例
if __name__ == '__main__':
    sol = Solution()
    n = 6
    edges = [[0,1],[0,2],[1,2],[3,4]]
    print(sol.countCompleteComponents(n, edges)) #3
