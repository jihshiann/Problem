import sys
input = sys.stdin.readline

#Sample Input
# 1
# 4 5
# 1 8
# 2 4
# 3 0
# 2 5
# 2 3

# Sample Output
# 13


class Solution:
    def solve(self):
        T = int(input())
        for _ in range(T):
            # S璉甧秖 N珇ン计MAP锣ΘINT
            S, N = map(int, input().split())
            # dp[j] ボ甧秖 j 眔程基
            dp = [0] * (S + 1)
            for _ in range(N):
                # w 珇秖 v 珇基
                w, v = map(int, input().split())
                # 0/1 璉ゲ斗癴眖S秨﹍w-1
                for cap in range(S, w - 1, -1):
                    # 安砞 S = 4, ヘ玡Τン秖 w = 1, 基 v = 8 珇dp ﹍ 0
                    # cap = 4dp[4] = max(dp[4], dp[3] + 8) = max(0, 0+3) = 3
                    # 璝珇玥逞甧秖 cap-w
                    dp[cap] = max(dp[cap], dp[cap - w] + v)
            # 程沧氮琌甧秖程 S 程基
            print(dp[S])


    def solve2(self):
        T = int(input())
        for _ in range(T):
            S, N = map(int, input().split())
            items = [tuple(map(int, input().split())) for _ in range(N)]
            
            # dp[i][j]: 玡 i ン珇甧秖 j 程基
            dp = [[0] * (S+1) for _ in range(N+1)]
            
            for i in range(1, N+1):
                w, v = items[i-1]
                for j in range(0, S+1):  # タ筂菌甧秖
                    # ぃ材 i ン
                    dp[i][j] = dp[i-1][j]
                    # 材 i ン璝甧秖ì镑
                    if j >= w:
                        dp[i][j] = max(dp[i][j], dp[i-1][j-w] + v)
            
            print(dp[N][S])

if __name__ == "__main__":
    Solution().solve()
