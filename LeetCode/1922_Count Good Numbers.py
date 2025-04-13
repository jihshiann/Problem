class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # 0 1 2 3 4 5
        # ���_���_���_...

        even = (n+1) // 2
        odd = n // 2
        # ans = (5**even) * (4**odd) % MOD

        # pow(base, exp, mod)  ��  (base**exp) % mod
        # (a modm)��(b modm) mod m= (a��b) mod m,
        ans = pow(5, even, MOD) * pow(4, odd, MOD) % MOD



        
        return ans

        