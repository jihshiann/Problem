class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        # 攤平成一維
        arr = [num for row in grid for num in row]
        # 將一維sort
        arr.sort()
        # 取中位數
        median = arr[len(arr)//2]
        result = 0
        # for 一維陣列
        for num in arr:
            distance = abs(median-num)
            if distance%x != 0:
                return -1
            result += distance // x

        return result  


# 測試範例
if __name__ == '__main__':
    sol = Solution()

    grid1 = [[2, 4], [6, 8]]
    x1 = 2
    print(sol.minOperations(grid1, x1))  # 預期輸出 4

    grid2 = [[1, 3], [5, 7]]
    x2 = 2
    print(sol.minOperations(grid2, x2))  
