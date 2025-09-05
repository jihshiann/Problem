class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # num1 -= (2^i + num2) 
        # 做k次
        for k in range(1, 61):
            x = num1 - num2 * k
            # num1 - (2^{i_1} + num2) - (2^{i_2} + num2) - ... - (2^{i_k} + num2) = 0
            # num1 - k * num2 = 2^{i_1} + 2^{i_2} + ... + 2^{i_k}
            x = num1 - num2 * k
            # x = (>0) + (>0) + ... + (>0) {k}
            # x >= k
            if x < k:
                return -1
            # 單位都是2進制
            # 13 = 1101, 至少要有3個2^i
            bit_count = bin(x).count('1')
            #if k >= x.bit_count():
            if k >= bit_count:
                return k

        return -1

solver = Solution()
    # 測試範例 1：基本情況
    # 預期結果: 2
assert solver.makeTheIntegerZero(10, 3) == 2

    # 測試範例 2：num2 為負數
    # 預期結果: 3
assert solver.makeTheIntegerZero(3, -2) == 3

    # 測試範例 3：無解的情況
    # 預期結果: -1
assert solver.makeTheIntegerZero(5, 7) == -1
    
    # 測試範例 4: k=1 就是答案
    # 預期結果: 1
assert solver.makeTheIntegerZero(10, 6) == 1
