class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        # �u�����@��
        arr = [num for row in grid for num in row]
        # �N�@��sort
        arr.sort()
        # �������
        median = arr[len(arr)//2]
        result = 0
        # for �@���}�C
        for num in arr:
            distance = abs(median-num)
            if distance%x != 0:
                return -1
            result += distance // x

        return result  


# ���սd��
if __name__ == '__main__':
    sol = Solution()

    grid1 = [[2, 4], [6, 8]]
    x1 = 2
    print(sol.minOperations(grid1, x1))  # �w����X 4

    grid2 = [[1, 3], [5, 7]]
    x2 = 2
    print(sol.minOperations(grid2, x2))  
