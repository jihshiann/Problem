class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        # dp[i] ��ܱq�� i �D�}�l�ү���o���̤j���ơAdp[n] = 0
        dp = [0] * (n + 1)
        
        # �q�˼ƲĤ@�D�}�l�V�e�p��
        #�T�O��ڭ̳B�z�� i �Ӱ��D�ɡA�Ҧ��� i �j�����D���̨Τ��Ƴ��w�g�p�⧹��
        for i in reversed(range(n)):
            points, brainpower = questions[i]
            # ���D�᪺�U�@�ӥi�H�Ѫ��D�د���
            next_index = i + brainpower + 1
            # �p�G next_index �W�X�d��A�h dp[next_index] ���� 0
            solve = points + (dp[next_index] if next_index < n + 1 else 0)
            skip = dp[i + 1]
            dp[i] = max(solve, skip)
        
        return dp[0]


        


# ���սd��
if __name__ == '__main__':
    sol = Solution()
    print(sol.mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]])) #157
