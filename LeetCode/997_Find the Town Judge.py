from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n==1:
            return 1
        if not trust:
            return -1
            
        trust_list = list(zip(*trust))
        if n - len(set(trust_list[0]))== 1:
            for i in range(1, n+1):
                if i not in trust_list[0] and trust_list[1].count(i) == n-1:
                    return i
                    
        return -1


# 創建 Solution 實例
sol = Solution()

# 調用 findJudge 方法並打印結果
trust_list = sol.findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]])
print(trust_list)

