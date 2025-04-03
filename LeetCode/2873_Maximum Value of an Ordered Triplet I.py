class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        #O(n^3)
        ans = 0
        lens = len(nums)
        for i, num in enumerate(nums):
            max_distance = 0
            for j in range(i+1, lens-1):
                max_distance = max(nums[i] - nums[j], max_distance)
                ans = max(ans, max_distance * max(nums[j+1:]))

        return ans
        

        

        


# ´ú¸Õ½d¨Ò
if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumTripletValue([12,6,1,2,7])) #77
