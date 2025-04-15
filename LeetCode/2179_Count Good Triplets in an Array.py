class Fenwick:
    def __init__(self, n):
        self.n = n
        self.fw = [0] * (n + 1)  # 1-based �𪬰}�C

    def update(self, i, v):
        # �b��m i �[�W v
        while i <= self.n:
            self.fw[i] += v
            i += i & -i

    def query(self, i):
        # �d�߫e��M [1..i]
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s

    def query_range(self, l, r):
        # �d�߰϶��M [l..r]
        return self.query(r) - self.query(l - 1)


class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        # 1. �إ� nums2 ���C�ӭ� v ����m�M�g pos2[v]
        pos2 = [0] * n
        for i, v in enumerate(nums2):
            pos2[v] = i

        # 2. �N nums1 �M�g�� A�GA[j] = nums1[j] �b nums2 ������m +1�]1-based�^
        A = [pos2[v] + 1 for v in nums1]

        # 3. �p�� left_smaller[j] = j �������h�� A[i] < A[j]
        fw1 = Fenwick(n)
        left_smaller = [0] * n
        for j in range(n):
            aj = A[j]
            # �d�� [1..aj-1] ���`�M�A�N�O�� aj �p���Ӽ�
            left_smaller[j] = fw1.query(aj - 1)
            # �N aj �[�J�𪬰}�C
            fw1.update(aj, 1)

        # 4. �p�� right_larger[j] = j �k�����h�� A[k] > A[j]
        fw2 = Fenwick(n)
        right_larger = [0] * n
        for j in range(n - 1, -1, -1):
            aj = A[j]
            # �d�� [aj+1..n] ���`�M�A�N�O�� aj �j���Ӽ�
            right_larger[j] = fw2.query_range(aj + 1, n)
            fw2.update(aj, 1)

        # 5. �֥[�Ҧ��H j �������������n�T���ռ�
        ans = 0
        for j in range(n):
            ans += left_smaller[j] * right_larger[j]
        return ans
