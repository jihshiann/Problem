class Fenwick:
    def __init__(self, n):
        self.n = n
        self.fw = [0] * (n + 1)  # 1-based 樹狀陣列

    def update(self, i, v):
        # 在位置 i 加上 v
        while i <= self.n:
            self.fw[i] += v
            i += i & -i

    def query(self, i):
        # 查詢前綴和 [1..i]
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s

    def query_range(self, l, r):
        # 查詢區間和 [l..r]
        return self.query(r) - self.query(l - 1)


class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        # 1. 建立 nums2 中每個值 v 的位置映射 pos2[v]
        pos2 = [0] * n
        for i, v in enumerate(nums2):
            pos2[v] = i

        # 2. 將 nums1 映射成 A：A[j] = nums1[j] 在 nums2 中的位置 +1（1-based）
        A = [pos2[v] + 1 for v in nums1]

        # 3. 計算 left_smaller[j] = j 左側有多少 A[i] < A[j]
        fw1 = Fenwick(n)
        left_smaller = [0] * n
        for j in range(n):
            aj = A[j]
            # 查詢 [1..aj-1] 的總和，就是比 aj 小的個數
            left_smaller[j] = fw1.query(aj - 1)
            # 將 aj 加入樹狀陣列
            fw1.update(aj, 1)

        # 4. 計算 right_larger[j] = j 右側有多少 A[k] > A[j]
        fw2 = Fenwick(n)
        right_larger = [0] * n
        for j in range(n - 1, -1, -1):
            aj = A[j]
            # 查詢 [aj+1..n] 的總和，就是比 aj 大的個數
            right_larger[j] = fw2.query_range(aj + 1, n)
            fw2.update(aj, 1)

        # 5. 累加所有以 j 為中間元素的好三元組數
        ans = 0
        for j in range(n):
            ans += left_smaller[j] * right_larger[j]
        return ans
