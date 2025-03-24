class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        if not meetings:
            return days
        
        # meetings排序
        meetings_sort = sorted(meetings)
        
        # 初始化第一個合併區間
        merged_start, merged_end = meetings_sort[0][0], meetings_sort[0][1]
        covered_days = 0
        
        # 從第二個會議開始合併
        for i in range(1, len(meetings_sort)):
            start, end = meetings_sort[i]
            # 若當前會議與合併區間有重疊或是連續 (meeting[0] <= merged_end + 1)
            if start <= merged_end:
                merged_end = max(merged_end, end)
            else:
                # 將上一個合併區間覆蓋的天數累計 
                covered_days += merged_end - merged_start + 1
                merged_start, merged_end = start, end
        
        # 累計最後一個合併區間的覆蓋天數
        covered_days += merged_end - merged_start + 1
        
        # 可用天數 = 總天數 - 被會議覆蓋的天數
        return days - covered_days

def test_solution():

    sol = Solution()

    # 測試案例 1
    days = 10
    meetings = [[5,7], [1,3], [9,10]]
    expected = 2
    result = sol.countDays(days, meetings)
    print("Test Case 1:", "Pass" if result == expected else f"Fail (expected {expected}, got {result})")

    # 測試案例 2
    days = 5
    meetings = [[2,4], [1,3], [1,2]]
    expected = 1
    result = sol.countDays(days, meetings)
    print("Test Case 2:", "Pass" if result == expected else f"Fail (expected {expected}, got {result})")

    # 測試案例 3
    days = 6
    meetings = [[1,6]]
    expected = 0
    result = sol.countDays(days, meetings)
    print("Test Case 3:", "Pass" if result == expected else f"Fail (expected {expected}, got {result})")

if __name__ == "__main__":
    test_solution()
