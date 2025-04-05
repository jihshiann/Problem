class Solution(object):
    def sumProperDivisors(self, n):
        """
        �p�� n �� proper divisors�]�p�� n ���Ҧ���㰣 n ���Ʀr�^���M
        :type n: int
        :rtype: int
        """
        # �p�G n �O 1�A�S�� proper divisor
        if n == 1:
            return 0
        
        total = 1  # 1 �@�w�O proper divisor�]n > 1�ɡ^
        i = 2
        # �q 2 �M���� sqrt(n)
        # 10 * 10 = 100
        while i * i <= n:
            if n % i == 0:
                total += i
                # �p�G i ���O����ڡA�h n//i �]�O proper divisor
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
