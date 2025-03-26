class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(1,len(nums)):
            result += (nums[i]-nums[0])

        return result 


