class Solution(object):
    def sumProperDivisors(self, n):
        """
        計算 n 的 proper divisors（小於 n 的所有能整除 n 的數字）的和
        :type n: int
        :rtype: int
        """
        # 如果 n 是 1，沒有 proper divisor
        if n == 1:
            return 0
        
        total = 1  # 1 一定是 proper divisor（n > 1時）
        i = 2
        # 從 2 遍歷到 sqrt(n)
        # 10 * 10 = 100
        while i * i <= n:
            if n % i == 0:
                total += i
                # 如果 i 不是平方根，則 n//i 也是 proper divisor
                # 4*25 and 25*4
                if i != n // i:
                    total += n // i
            i += 1
        return total

# Sample Input
# 2
# 220
# 284

# Sample Output
# 284
# 220
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    output = []
    sol = Solution()
    for idx in range(1, t+1):
        n = int(data[idx])
        output.append(str(sol.sumProperDivisors(n)))
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
