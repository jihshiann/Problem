class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        # 1. 先將 nums 由小到大排序
        nums.sort()
        n = len(nums)
        
        # dp[i]：以 nums[i] 作為結尾的最大可整除子集長度
        dp = [1] * n
        # prev[i]：重建路徑時，紀錄 nums[i] 前一個元素的索引
        prev = [-1] * n
        
        max_size = 1  # 全局最大子集長度
        max_idx = 0   # 全局最大子集結尾的索引
        
        # 2. 動態規劃 O(n^2)
        for i in range(n):
            for j in range(i):
                # 如果 nums[i] 能被 nums[j] 整除，且接在 j 之後可以讓子集更大
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            # 更新全局最大子集
            if dp[i] > max_size:
                max_size = dp[i]
                max_idx = i
        
        # 3. 重建答案子集
        res = []
        idx = max_idx
        while idx != -1:
            res.append(nums[idx])
            idx = prev[idx]
        res.reverse()
        return res