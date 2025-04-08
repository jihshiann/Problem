class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        # 1. ���N nums �Ѥp��j�Ƨ�
        nums.sort()
        n = len(nums)
        
        # dp[i]�G�H nums[i] �@���������̤j�i�㰣�l������
        dp = [1] * n
        # prev[i]�G���ظ��|�ɡA���� nums[i] �e�@�Ӥ���������
        prev = [-1] * n
        
        max_size = 1  # �����̤j�l������
        max_idx = 0   # �����̤j�l������������
        
        # 2. �ʺA�W�� O(n^2)
        for i in range(n):
            for j in range(i):
                # �p�G nums[i] ��Q nums[j] �㰣�A�B���b j ����i�H���l����j
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            # ��s�����̤j�l��
            if dp[i] > max_size:
                max_size = dp[i]
                max_idx = i
        
        # 3. ���ص��פl��
        res = []
        idx = max_idx
        while idx != -1:
            res.append(nums[idx])
            idx = prev[idx]
        res.reverse()
        return res