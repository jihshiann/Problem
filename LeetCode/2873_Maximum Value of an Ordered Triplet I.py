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
            for j in range(i+1, lens):
                max_distance = max(nums[i] + nums[j], max_distance)
                for k in range(j+1, lens):
                    ans = max(ans, max_distance * nums[k])

        return ans

        #存在索引i之前最大的數
        n = len(nums)
        # 至少需要3個元素，否則無法形成合法的 triplet
        if n < 3:
            return 0

        # 構造 L 陣列：L[j] = max_{i<j} nums[i]
        L = [0] * n
        L[0] = float('-inf')          # j=0 沒有 i，所以設為負無窮大
        L[1] = nums[0]                # 對於 j=1, i唯一是0
        for j in range(2, n):
            # 注意：i < j，因此 L[j] 應該是從索引 0 到 j-1 的最大值
            L[j] = max(L[j-1], nums[j-1])

        # 構造 R 陣列：R[j] = max_{k>j} nums[k]
        R = [0] * n
        R[n-1] = float('-inf')        # j=n-1 沒有 k，所以設為負無窮大
        R[n-2] = nums[n-1]            # 對於 j=n-2, k唯一是 n-1
        for j in range(n-3, -1, -1):
            # k > j, 所以 R[j] = max(nums[j+1], R[j+1])
            R[j] = max(R[j+1], nums[j+1])
        
        ans = 0
        # 遍歷中間位置 j (合法的 j: 1 到 n-2)
        for j in range(1, n-1):
            diff = L[j] - nums[j]
            if diff > 0:
                candidate = diff * R[j]
                ans = max(ans, candidate)
        return ans



        


# 測試範例
if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumTripletValue([12,6,1,2,7])) #77
