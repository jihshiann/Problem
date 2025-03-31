class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        n = len(weights)
        # ��u���@�U�Ϊ̨C�Ӥ����@�U�ɡA���Ʈt��0
        if k == 1 or k == n:
            return 0
        
        # diff[i]�Y�����I�����k�䤧�X
        # diff[i] = weights[i] + weights[i+1]
        diffs = []
        for i in range(n-1):
            diffs.append(weights[i] + weights[i+1])
        
        # �� diff �C��Ƨ�
        diffs.sort()
        
        #���K�ӥN��n��k-1�M
        max_cost_extra = sum(diffs[-(k-1):])
        min_cost_extra = sum(diffs[:k-1])
        #�̤j�X�M�X-�̤p�X�M�M�Y���ѵ�

        return max_cost_extra - min_cost_extra

        


# ���սd��
if __name__ == '__main__':
    sol = Solution()
    print(sol.putMarbles([1,3,5,1], 2))  # 4

