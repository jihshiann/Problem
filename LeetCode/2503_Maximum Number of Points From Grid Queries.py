import heapq

class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        # min-heap(val, row, column)
        heap=[]
        heapq.heappush(heap, (grid[0][0], 0, 0))

        count = 0
        # 四個鄰居方向：下、上、右、左
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(grid), len(grid[0])
        ans = [0] * len(queries)

        #已尋訪
        visited = [[False for n in range(col)] for m in range(row)]
        visited[0][0] = True

        # 排序query，並保留原始順序
        sorted_q = sorted((q, i)for i, q in enumerate(queries))

        for q, i in sorted_q:
            while heap and heap[0][0]<q:
                count +=1
                #取得目前座標並結束尋訪
                val , r, c = heapq.heappop(heap)
                #擴展
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<row and 0<=nc<col and visited[nr][nc] == False:
                        visited[nr][nc] = True
                        heapq.heappush(heap, (grid[nr][nc], nr, nc))

            ans[i] = count
        return ans

        




if __name__ == '__main__':
    s = Solution()
    print(s.maxPoints([[1,2,3],[2,5,7],[3,5,1]], [5,6,2]))  # [5,8,1]
    print(s.maxPoints([[5,2,1],[1,1,2]], [3]))  # [0]

    