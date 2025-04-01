class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_gain = [0] * (n+1)
        for i in reversed(range(n)):
            money = nums[i]
            next_i = i+2
            rob = money + (max_gain[next_i] if next_i < n +1 else 0)
            skip = max_gain[i+1]
            max_gain[i] = max(rob, skip)

        return max_gain[0]


        


# ´ú¸Õ½d¨Ò
if __name__ == '__main__':
    sol = Solution()
    print(sol.rob([1,2])) #2
