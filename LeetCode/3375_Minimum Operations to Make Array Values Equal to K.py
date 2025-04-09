class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if min(nums) < k :
            return -1
        
        count = 0

        distinct = set(nums)
        # ���C�@�ӲŦX����]x > k�^�������A���ͤ@�ӼƦr 1
        count = sum(1 for x in distinct if x > k)
        return count

