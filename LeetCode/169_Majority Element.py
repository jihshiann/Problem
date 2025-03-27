class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        
        # �M���}�C�A�Q�Φh�Ƨ벼�k���Կ露��
        for num in nums:
            if count == 0:
                candidate = num
            #�Y��e�Ʀr�P�Կ露���۵��A�h�N count �[ 1�F�_�h�� 1�C
            count += 1 if num == candidate else -1
        
        return candidate

if __name__ == '__main__':
    s = Solution()
    print(s.minimumIndex([1,2,2,2]))  
    print(s.minimumIndex([1,1,1]))  
    print(s.minimumIndex([1,1,1,2]))  
    