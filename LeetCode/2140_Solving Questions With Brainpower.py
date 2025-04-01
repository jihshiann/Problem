class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        # dp[i] 表示從第 i 題開始所能獲得的最大分數，dp[n] = 0
        dp = [0] * (n + 1)
        
        # 從倒數第一題開始向前計算
        #確保當我們處理第 i 個問題時，所有比 i 大的問題的最佳分數都已經計算完畢
        for i in reversed(range(n)):
            points, brainpower = questions[i]
            # 解題後的下一個可以解的題目索引
            next_index = i + brainpower + 1
            # 如果 next_index 超出範圍，則 dp[next_index] 視為 0
            solve = points + (dp[next_index] if next_index < n + 1 else 0)
            skip = dp[i + 1]
            dp[i] = max(solve, skip)
        
        return dp[0]


        


# 測試範例
if __name__ == '__main__':
    sol = Solution()
    print(sol.mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]])) #157
