class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        # 如果總和是奇數，就不可能平分
        if total % 2 == 1:
            return False
        
        target = total // 2
        # dp[j] 表示是否存在一個子集，其和恰好為 j
        dp = [False] * (target + 1)
        dp[0] = True  # 和為 0 的子集一定存在（空集）
        
        # 對每個數 num，更新 dp
        for num in nums:
            # 逆序遍歷，避免重複使用同一個 num
            for j in range(target, num - 1, -1):
                # 若不拿 num（dp[j]）或拿 num（dp[j-num]），只要有一種成立就行
                dp[j] = dp[j] or dp[j - num]
            # 如果已經能湊出 target，提前返回
            if dp[target]:
                return True
        
        return dp[target]