class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if min(nums) < k:
            return -1
        # ���C�@�ӲŦX����]x > k�^�������A���ͤ@�ӼƦr 1
        return sum(1 for x in set(nums) if x > k)
