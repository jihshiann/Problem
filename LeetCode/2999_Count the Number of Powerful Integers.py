class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # 1. 檢查後綴 s 自身是否有任何一位 > limit，若有則不可能有解
        for ch in s:
            if int(ch) > limit:
                return 0

        L = len(s)
        v = int(s)
        base = 10 ** L

        # 2. 計算 t 的範圍，使得 x = t*10^L + v 落在 [start, finish]
        t_min = (start - v + base - 1) // base  # 向上取整
        t_max = (finish - v) // base             # 向下取整
        if t_max < 0:
            return 0
        t_min = max(t_min, 0)
        if t_min > t_max:
            return 0

        # 3. 定義數位 DP 函數 count_upto(X)：計算 [0..X] 中
        #    符合「每位數字都 ≤ limit」的整數個數
        def count_upto(X: int) -> int:
            sX = list(map(int, str(X)))  # 將 X 轉成數位列表
            n = len(sX)
            dp = {}  # 手動快取 (pos, tight, lead) -> count

            def dfs(pos: int, tight: int, lead: int) -> int:
                """
                pos   : 當前處理到第 pos 位（0 為最高位）
                tight : 前面是否都和 X 的前綴一致 (1: 一致, 0: 已小於)
                lead  : 是否仍在前導零階段 (1: 目前全是 0, 0: 已經出現過非零)
                """
                if pos == n:
                    # 處理完所有數位，算 1 個合法數（包含全 0）
                    return 1
                key = (pos, tight, lead)
                if key in dp:
                    return dp[key]

                # 決定當前位的最大可選數字
                up = sX[pos] if tight else limit
                res = 0
                for d in range(up + 1):
                    # 如果不是前導零且 d > limit，跳出
                    if not (lead and d == 0) and d > limit:
                        break
                    ntight = tight and (d == up)
                    nlead = lead and (d == 0)
                    res += dfs(pos + 1, ntight, nlead)

                dp[key] = res
                return res

            return dfs(0, 1, 1)

        # 4. 答案 = count_upto(t_max) - count_upto(t_min - 1)
        total = count_upto(t_max)
        if t_min > 0:
            total -= count_upto(t_min - 1)
        return total
