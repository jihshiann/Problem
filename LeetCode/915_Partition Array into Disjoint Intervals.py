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
            # ��s�����̤j��
            if nums[i] > current_max:
                current_max = nums[i]
            
            # �p�G��e�����p�� left_max�A�����N���k�J�����l�}�C�A�ç�s partition_index
            if nums[i] < left_max:
                partition_index = i
                #�����̤j�Ȳ{�b�~��s
                left_max = current_max
        
        # ��^�����l�}�C�����סA�Y partition_index + 1
        return partition_index + 1


if __name__ == '__main__':
    s = Solution()
    print(s.partitionDisjoint([5,0,3,8,6]))   
    print(s.partitionDisjoint([90,47,69,10,43,92,31,73,61,97]))   
    