MOD = 10**9 + 7

class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        # 1. 預處理：計算質因數分數
        # 先計算 1 ~ max_val 的最小質因數，用篩法
        max_val = max(nums)
        spf = list(range(max_val+1))  # spf[x] = smallest prime factor of x

        for i in range(2, int(max_val**0.5)+1):
            if spf[i] == i:  # i 是質數
                for j in range(i*i, max_val+1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        # 函數：計算 x 的質因數分數
        def primeScore(x):
            score = 0
            prev = -1
            while x > 1:
                #取得 x 的最小質因數
                p = spf[x]
                if p != prev:
                    score += 1
                    prev = p
                # 整數除法分解質因數
                x //= p
            return score
        
        # 計算每個數字的質因數分數
        pscore = [primeScore(x) for x in nums]
        
        # 2. 使用單調棧計算每個索引的有效子陣列數量 count[i]
        # L[i] = 最近左邊索引 j, j < i, 使得 pscore[j] >= pscore[i]，如果無則 -1
        L = [-1] * n
        stack = []
        for i in range(n):
            # 當前數字的質因數分數
            while stack and pscore[stack[-1]] < pscore[i]:
                stack.pop()
            L[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # R[i] = 最近右邊索引 j, j > i, 使得 pscore[j] > pscore[i]，如果無則 n
        R = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and pscore[stack[-1]] <= pscore[i]:
                stack.pop()
            R[i] = stack[-1] if stack else n
            stack.append(i)
        
        # count[i] 為 (i - L[i]) * (R[i] - i)
        count = [ (i - L[i]) * (R[i] - i) for i in range(n) ]
        
        # 3. 將每個索引 i 形成 (nums[i], count[i]) 配對
        # 我們希望根據 nums[i] 從大到小排序，因為較大的乘數更有利
        pairs = [(nums[i], count[i]) for i in range(n)]
        pairs.sort(key=lambda x: x[0], reverse=True)
        
        # 4. 貪心選取操作次數，不超過 k
        remaining = k
        score = 1
        for x, cnt in pairs:
            if remaining <= 0:
                break
            use = min(cnt, remaining)
            # score *= x^use  (模 MOD)
            # 使用快速冪
            score = (score * pow(x, use, MOD)) % MOD
            remaining -= use
        
        return score


if __name__ == '__main__':
    s = Solution()
    print(s.maximumScore([8,3,9,3,8], 2)) # 81
    print(s.maximumScore([19,12,14,6,10,18], 3)) # 4788

    