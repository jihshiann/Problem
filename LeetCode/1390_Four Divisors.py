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
            #1��ۤv
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
        #�s���
        sieve = [True] * (max_prime+1)
        sieve[0] = sieve[1] =False #0��1�D���
        primes = []
        for i in range(2, max_prime+1):
            if sieve[i]:
                primes.append(i)
                for j in range(i*i, max_prime+1, i):#4,6,8�F9,12,15...
                    sieve[j] = False
        cache = {}  # �֨����G�H�K���ƭp��
        
        def four_divisor_sum(num):
            # �p�G�w�p��L�h������^
            if num in cache:
                return cache[num]
            # �Y num �� 1�Aproper divisors ���šA��^ 0
            if num == 1:
                cache[num] = 0
                return 0
            
            temp = num
            factors = {}
            # �ιw���p��n�� primes �i���]�Ƥ���
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
            # ���p�@�Gnum = p * q, �䤤 p, q �����P��ơ]�U1����^
            if len(factors) == 2 and all(exp == 1 for exp in factors.values()):
                p, q = list(factors.keys())
                res = (1 + p) * (1 + q)
            # ���p�G�Gnum = p^3
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




       
            

# ���սd��
if __name__ == '__main__':
    sol = Solution()
    print(sol.sumFourDivisors([21,4,7])) #32
