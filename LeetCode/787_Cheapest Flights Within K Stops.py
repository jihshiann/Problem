from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 初始化dp數組，設置為無窮大
        dp = [[float('inf')] * (k + 2) for _ in range(n)]
        # 從src出發，0次中轉的成本為0
        for i in range(k + 2):
            dp[src][i] = 0
        
        # 遍歷每一次可能的中轉次數
        for i in range(1, k + 2):
            for flight in flights:
                frm, to, price = flight
                # min(經過i-1次中轉到to, 到frm+price(frm-to))
                dp[to][i] = min(dp[to][i], dp[frm][i - 1] + price)
                
        # 找到最小的費用，如果為無窮大則返回-1
        ans = min(dp[dst][1:k + 2])
        return -1 if ans == float('inf') else ans

sol = Solution()
ans = sol.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)