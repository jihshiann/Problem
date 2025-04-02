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

        #�s�b����i���e�̤j����
        n = len(nums)
        # �ܤֻݭn3�Ӥ����A�_�h�L�k�Φ��X�k�� triplet
        if n < 3:
            return 0

        # �c�y L �}�C�GL[j] = max_{i<j} nums[i]
        L = [0] * n
        L[0] = float('-inf')          # j=0 �S�� i�A�ҥH�]���t�L�a�j
        L[1] = nums[0]                # ��� j=1, i�ߤ@�O0
        for j in range(2, n):
            # �`�N�Gi < j�A�]�� L[j] ���ӬO�q���� 0 �� j-1 ���̤j��
            L[j] = max(L[j-1], nums[j-1])

        # �c�y R �}�C�GR[j] = max_{k>j} nums[k]
        R = [0] * n
        R[n-1] = float('-inf')        # j=n-1 �S�� k�A�ҥH�]���t�L�a�j
        R[n-2] = nums[n-1]            # ��� j=n-2, k�ߤ@�O n-1
        for j in range(n-3, -1, -1):
            # k > j, �ҥH R[j] = max(nums[j+1], R[j+1])
            R[j] = max(R[j+1], nums[j+1])
        
        ans = 0
        # �M��������m j (�X�k�� j: 1 �� n-2)
        for j in range(1, n-1):
            diff = L[j] - nums[j]
            if diff > 0:
                candidate = diff * R[j]
                ans = max(ans, candidate)
        return ans



        


# ���սd��
if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumTripletValue([12,6,1,2,7])) #77
