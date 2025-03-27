class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left_max = nums[0]
        current_max = nums[0]
        partition_index = 0
        
        for i in range(1, len(nums)):
            # 更新全局最大值
            if nums[i] > current_max:
                current_max = nums[i]
            
            # 如果當前元素小於 left_max，必須將它歸入左側子陣列，並更新 partition_index
            if nums[i] < left_max:
                partition_index = i
                #左側最大值現在才更新
                left_max = current_max
        
        # 返回左側子陣列的長度，即 partition_index + 1
        return partition_index + 1


if __name__ == '__main__':
    s = Solution()
    print(s.partitionDisjoint([5,0,3,8,6]))   
    print(s.partitionDisjoint([90,47,69,10,43,92,31,73,61,97]))   
    