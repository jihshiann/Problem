from curses import flash
import math

class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            #1跟自己
            divisor_count = 2
            qs = [1, num]
            if num == 1:
                continue
            i = 2
            # 10 * 10 = 100
            while i * i <= num:
                if num % i == 0:
                    divisor_count += 1
                    q = num//i
                    qs.append(q)
                    # 4*25 and 25*4
                    if i != q:
                        divisor_count += 1
                        qs.append(i)
                    if divisor_count > 4:
                        break
                i += 1   
            if divisor_count == 4:
                ans += sum(qs)
        
        return ans

    def sumFourDivisors2(self, nums):
        max_prime = math.sqrt(10 **5)+1
        #存質數
        sieve = [True] * (max_prime+1)
        sieve[0] = sieve[1] =False #0跟1非質數
        primes = []
        for i in range(2, max_prime+1):
            if sieve[i]:
                primes.append(i)
                for j in range(i*i, max_prime+1, i):#4,6,8；9,12,15...
                    sieve[j] = False
        cache = {}  # 快取結果以免重複計算
        
        def four_divisor_sum(num):
            # 如果已計算過則直接返回
            if num in cache:
                return cache[num]
            # 若 num 為 1，proper divisors 為空，返回 0
            if num == 1:
                cache[num] = 0
                return 0
            
            temp = num
            factors = {}
            # 用預先計算好的 primes 進行質因數分解
            for p in primes:
                if p * p > temp:
                    break
                if temp % p == 0:
                    count = 0
                    while temp % p == 0:
                        count += 1
                        temp //= p
                    factors[p] = count
            if temp > 1:
                factors[temp] = factors.get(temp, 0) + 1
            
            res = 0
            # 情況一：num = p * q, 其中 p, q 為不同質數（各1次方）
            if len(factors) == 2 and all(exp == 1 for exp in factors.values()):
                p, q = list(factors.keys())
                res = (1 + p) * (1 + q)
            # 情況二：num = p^3
            elif len(factors) == 1:
                p, exp = list(factors.items())[0]
                if exp == 3:
                    res = 1 + p + p * p + p * p * p
            
            cache[num] = res
            return res
        
        ans = 0
        for num in nums:
            ans += four_divisor_sum(num)
        
        return ans




       
            

# 測試範例
if __name__ == '__main__':
    sol = Solution()
    print(sol.sumFourDivisors([21,4,7])) #32
