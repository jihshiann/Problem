class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        # �p�G�`�M�O�_�ơA�N���i�७��
        if total % 2 == 1:
            return False
        
        target = total // 2
        # dp[j] ��ܬO�_�s�b�@�Ӥl���A��M��n�� j
        dp = [False] * (target + 1)
        dp[0] = True  # �M�� 0 ���l���@�w�s�b�]�Ŷ��^
        
        # ��C�Ӽ� num�A��s dp
        for num in nums:
            # �f�ǹM���A�קK���ƨϥΦP�@�� num
            for j in range(target, num - 1, -1):
                # �Y���� num�]dp[j]�^�ή� num�]dp[j-num]�^�A�u�n���@�ئ��ߴN��
                dp[j] = dp[j] or dp[j - num]
            # �p�G�w�g���X target�A���e��^
            if dp[target]:
                return True
        
        return dp[target]