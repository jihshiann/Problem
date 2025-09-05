class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # num1 -= (2^i + num2) 
        # ��k��
        for k in range(1, 61):
            x = num1 - num2 * k
            # num1 - (2^{i_1} + num2) - (2^{i_2} + num2) - ... - (2^{i_k} + num2) = 0
            # num1 - k * num2 = 2^{i_1} + 2^{i_2} + ... + 2^{i_k}
            x = num1 - num2 * k
            # x = (>0) + (>0) + ... + (>0) {k}
            # x >= k
            if x < k:
                return -1
            # ��쳣�O2�i��
            # 13 = 1101, �ܤ֭n��3��2^i
            bit_count = bin(x).count('1')
            #if k >= x.bit_count():
            if k >= bit_count:
                return k

        return -1

solver = Solution()
    # ���սd�� 1�G�򥻱��p
    # �w�����G: 2
assert solver.makeTheIntegerZero(10, 3) == 2

    # ���սd�� 2�Gnum2 ���t��
    # �w�����G: 3
assert solver.makeTheIntegerZero(3, -2) == 3

    # ���սd�� 3�G�L�Ѫ����p
    # �w�����G: -1
assert solver.makeTheIntegerZero(5, 7) == -1
    
    # ���սd�� 4: k=1 �N�O����
    # �w�����G: 1
assert solver.makeTheIntegerZero(10, 6) == 1
