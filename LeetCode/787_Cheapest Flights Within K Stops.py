from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # ��l��dp�ƲաA�]�m���L�a�j
        dp = [[float('inf')] * (k + 2) for _ in range(n)]
        # �qsrc�X�o�A0�����઺������0
        for i in range(k + 2):
            dp[src][i] = 0
        
        # �M���C�@���i�઺���স��
        for i in range(1, k + 2):
            for flight in flights:
                frm, to, price = flight
                # min(�g�Li-1�������to, ��frm+price(frm-to))
                dp[to][i] = min(dp[to][i], dp[frm][i - 1] + price)
                
        # ���̤p���O�ΡA�p�G���L�a�j�h��^-1
        ans = min(dp[dst][1:k + 2])
        return -1 if ans == float('inf') else ans

sol = Solution()
ans = sol.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)