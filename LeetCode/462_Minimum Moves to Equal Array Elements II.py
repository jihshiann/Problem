class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = nums[len(nums)//2]
        result = 0
        for n in nums:
            result += abs(mid - n)

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.minMoves2([1,2,3]))  # 2
    