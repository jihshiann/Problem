class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if min(nums) < k:
            return -1
        # 對於每一個符合條件（x > k）的元素，產生一個數字 1
        return sum(1 for x in set(nums) if x > k)
