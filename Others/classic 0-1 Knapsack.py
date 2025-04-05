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
            # S���I�]�e�q N�����~��ơAMAP�૬��INT
            S, N = map(int, input().split())
            # dp[j] ��ܮe�q��n�� j �ɯ���o���̤j����
            dp = [0] * (S + 1)
            for _ in range(N):
                # w �����~���q v �����~����
                w, v = map(int, input().split())
                # 0/1 �I�]�G�����f�ǡA�qS�}�l��w-1
                for cap in range(S, w - 1, -1):
                    # ���] S = 4, �ثe���@�󭫶q w = 1, ���� v = 8 �����~�Adp ��l���� 0�G
                    # cap = 4�Gdp[4] = max(dp[4], dp[3] + 8) = max(0, 0+3) = 3
                    # �Y�������~�A�h�ѤU�e�q cap-w
                    dp[cap] = max(dp[cap], dp[cap - w] + v)
            # �̲׵��׬O�e�q�̦h�� S �ɪ��̤j����
            print(dp[S])


    def solve2(self):
        T = int(input())
        for _ in range(T):
            S, N = map(int, input().split())
            items = [tuple(map(int, input().split())) for _ in range(N)]
            
            # dp[i][j]: �e i �󪫫~�A�e�q j ���̤j����
            dp = [[0] * (S+1) for _ in range(N+1)]
            
            for i in range(1, N+1):
                w, v = items[i-1]
                for j in range(0, S+1):  # ���ǹM���e�q
                    # ������ i ��
                    dp[i][j] = dp[i-1][j]
                    # ���� i ��]�Y�e�q�����^
                    if j >= w:
                        dp[i][j] = max(dp[i][j], dp[i-1][j-w] + v)
            
            print(dp[N][S])

if __name__ == "__main__":
    Solution().solve()
