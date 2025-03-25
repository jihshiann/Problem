class Solution(object):
    #切割線必須落在矩形邊界上且不能切到矩形內部，因此可以從一個方向（水平或垂直）看，將每個矩形在該方向的區間
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        #進行合併並計算最後得到的不連續區間數量
        def merge_intervals(intervals):
            intervals.sort(key=lambda interval: interval[0])
            merged = []
            for interval in intervals:
                #當前區間的起始值是否大於或等於最後一個合併區間的結束值
                if not merged or interval[0] >= merged[-1][1]:
                    merged.append(interval[:])
                else:
                    # 重疊則合併，更新結束值為較大者
                    merged[-1][1] = max(merged[-1][1], interval[1])
            return len(merged)
        
        total = len(rectangles)
        if total < 3:
            return False
        
        # 取得所有矩形在 y 軸上的區間 [starty, endy]
        y_intervals = []
        # 取得所有矩形在 x 軸上的區間 [startx, endx]
        x_intervals = []
        for rect in rectangles:
            # rect = [startx, starty, endx, endy]
            x_intervals.append([rect[0], rect[2]])
            y_intervals.append([rect[1], rect[3]])
        horizontal_groups = merge_intervals(y_intervals)
        # 若其中一方向上可以分出至少三個不連續區間，表示存在兩個切割線可將矩形分成三組
        if horizontal_groups >= 3:
            return True
        
        vertical_groups = merge_intervals(x_intervals)
        # 若其中一方向上可以分出至少三個不連續區間，表示存在兩個切割線可將矩形分成三組
        if vertical_groups >= 3:
            return True

        return False


# 測試範例
if __name__ == '__main__':
    sol = Solution()

    n = 5
    rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
    print(sol.checkValidCuts(n, rectangles))  # 預期輸出 True

    n = 4
    rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
    print(sol.checkValidCuts(n, rectangles))  # 預期輸出 True

    n = 4
    rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
    print(sol.checkValidCuts(n, rectangles))  # 預期輸出 False
