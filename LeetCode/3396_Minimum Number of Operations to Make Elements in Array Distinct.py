import math
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        ans = 0
        if len_nums == 0:
            return ans

        # # counter = {num: times} ex: {1: 3}
        # counter = Counter(nums)
        # # dups = {num: times} ex: {1: 3}
        # dups = {x: count for x, count in counter.items() if count > 1}
        # if not dups:
        #     return ans
        # for i in range(0, len_nums, 3):
        #     if len_nums <= 3:
        #         ans += 1
        #         return ans
        #     if dups.get(nums[i]):
        #         if dups[nums[i]] <= 2:
        #             del dups[nums[i]]
        #         else:
        #             dups[nums[i]] -= 1
        #     if dups.get(nums[i+1]):
        #         if dups[nums[i+1]] <= 2:
        #             del dups[nums[i+1]]
        #         else:
        #             dups[nums[i+1]] -= 1
        #     if dups.get(nums[i+2]):
        #         if dups[nums[i+2]] <= 2:
        #             del dups[nums[i+2]]
        #         else:
        #             dups[nums[i+2]] -= 1
        #     ans += 1
        #     len_nums -=3
        #     if not dups:
        #         return ans
        distinct = set()
        for i in range(len_nums -1, -1, -1):
            if nums[i] not in distinct:
                distinct.add(nums[i])
            else:
                break
        ans = int(math.ceil((len_nums - len(distinct)) / 3.0))

        return ans


            


            