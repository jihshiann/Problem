class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.ans = 0
        n = len(nums)
        
        # dfs(idx, curr_xor): 處理到索引 idx，當前 XOR 值為 curr_xor
        def dfs(idx, curr_xor):
            # 如果已處理完所有元素，將 curr_xor 累加到答案
            if idx == n:
                self.ans += curr_xor
                return
            # 選擇不包含 nums[idx]
            dfs(idx + 1, curr_xor)
            # 選擇包含 nums[idx]
            dfs(idx + 1, curr_xor ^ nums[idx])
        
        # 從索引 0 開始，初始 XOR 值為 0
        dfs(0, 0)
        return self.ans
# --------------------
# 測試案例
if __name__ == "__main__":
    sol = Solution()


    print(sol.subsetXORSum([5,1,6]))  # 28

    
