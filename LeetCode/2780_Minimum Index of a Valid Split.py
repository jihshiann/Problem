from collections import Counter
class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr_len = len(nums)

        if arr_len == 1:
            return -1

        counter = Counter(nums)
        most_comm = counter.most_common(1)
        comm_val = most_comm[0][0]
        count_most = most_comm[0][1]

        if count_most == arr_len:
            return 0

        same_times = 0
        for i, num in enumerate(nums):
            if num == comm_val:
                same_times +=1
            #左邊有一半以上
            if same_times > (i+1)//2:
                #右邊一半以上
                if count_most-same_times > (arr_len - i - 1)//2:
                    return (i)
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.minimumIndex([1,2,2,2]))  # 2
    print(s.minimumIndex([1,1,1]))  # 0
    print(s.minimumIndex([1,1,1,2]))  # 0
    