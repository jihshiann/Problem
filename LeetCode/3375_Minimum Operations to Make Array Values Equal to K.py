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
        # 對於每一個符合條件（x > k）的元素，產生一個數字 1
        count = sum(1 for x in distinct if x > k)
        return count

