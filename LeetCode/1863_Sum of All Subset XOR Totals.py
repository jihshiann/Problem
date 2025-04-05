class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.ans = 0
        n = len(nums)
        
        # dfs(idx, curr_xor): �B�z����� idx�A��e XOR �Ȭ� curr_xor
        def dfs(idx, curr_xor):
            # �p�G�w�B�z���Ҧ������A�N curr_xor �֥[�쵪��
            if idx == n:
                self.ans += curr_xor
                return
            # ��ܤ��]�t nums[idx]
            dfs(idx + 1, curr_xor)
            # ��ܥ]�t nums[idx]
            dfs(idx + 1, curr_xor ^ nums[idx])
        
        # �q���� 0 �}�l�A��l XOR �Ȭ� 0
        dfs(0, 0)
        return self.ans
# --------------------
# ���ծר�
if __name__ == "__main__":
    sol = Solution()


    print(sol.subsetXORSum([5,1,6]))  # 28

    
