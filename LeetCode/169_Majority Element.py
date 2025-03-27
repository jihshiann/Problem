class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        
        # 遍歷陣列，利用多數投票法找到候選元素
        for num in nums:
            if count == 0:
                candidate = num
            #若當前數字與候選元素相等，則將 count 加 1；否則減 1。
            count += 1 if num == candidate else -1
        
        return candidate

if __name__ == '__main__':
    s = Solution()
    print(s.minimumIndex([1,2,2,2]))  
    print(s.minimumIndex([1,1,1]))  
    print(s.minimumIndex([1,1,1,2]))  
    