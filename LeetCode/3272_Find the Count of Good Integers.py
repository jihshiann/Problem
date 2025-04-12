class Solution(object):
    def countGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        half = n // 2
        is_odd = (n % 2 == 1)
        palins = []

        def build(prefix, pos):
            if pos == half:
                left = prefix
                right = prefix[::-1]
                if is_odd:
                    for d in range(10):
                        s = left + str(d) + right
                        if s[0] == '0': continue
                        x = int(s)
                        if x % k == 0:
                            palins.append(s)
                else:
                    s = left + right
                    if s[0] == '0': return
                    x = int(s)
                    if x % k == 0:
                        palins.append(s)
                return
            for d in range(10):
                if pos == 0 and d == 0: continue
                build(prefix + str(d), pos + 1)

        build("", 0)

        # 階乘與反階乘
        fact = [1] * (n + 1)
        inv = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i-1] * i % MOD
        inv[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            inv[i-1] = inv[i] * i % MOD

        def count_perms(cnt):
            # 總排列數
            total = fact[n]
            for c in cnt:
                total = total * inv[c] % MOD
            # 減去首位為0的排列
            if cnt[0] > 0:
                bad = fact[n-1]
                # 0 的剩餘為 cnt[0]-1
                bad = bad * inv[cnt[0]-1] % MOD
                for d in range(1,10):
                    bad = bad * inv[cnt[d]] % MOD
                total = (total - bad) % MOD
            return total

        seen = set()
        ans = 0
        for p in palins:
            cnt = [0]*10
            for ch in p:
                cnt[ord(ch)-48] += 1
            key = tuple(cnt)
            if key in seen: continue
            seen.add(key)
            ans = (ans + count_perms(cnt)) % MOD

        return ans
