class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        n = len(weights)
        # 當只有一袋或者每個元素一袋時，分數差為0
        if k == 1 or k == n:
            return 0
        
        # diff[i]即為切點的左右邊之合
        # diff[i] = weights[i] + weights[i+1]
        diffs = []
        for i in range(n-1):
            diffs.append(weights[i] + weights[i+1])
        
        # 對 diff 列表排序
        diffs.sort()
        
        #分拆成K個代表要切k-1刀
        max_cost_extra = sum(diffs[-(k-1):])
        min_cost_extra = sum(diffs[:k-1])
        #最大幾刀合-最小幾刀和即為解答

        return max_cost_extra - min_cost_extra

        


# 測試範例
if __name__ == '__main__':
    sol = Solution()
    print(sol.putMarbles([1,3,5,1], 2))  # 4

