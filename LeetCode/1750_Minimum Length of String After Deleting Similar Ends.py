class Solution:
    def minimumLength(self, s: str) -> int:
        
        #recursive
        # lastRemove = ""
        # if len(s) <= 1:
        #     return len(s)
        
        # # check1 
        # if s[0] == s[-1]:
        #     lastRemove = s[0]
        #     s = s[1:-1]
        #     if len(s) < 1:
        #         return len(s)
            
        #     # check2 
        #     while s[0] == lastRemove and len(s) > 0 :
        #         s = s[1:]
        #         if len(s) < 1:
        #             return len(s)
            
        #     # check3 
        #     while s[-1] == lastRemove and len(s) > 0 :
        #         s = s[:-1]
        #         if len(s) < 1:
        #             return len(s)
        
        #     return self.minimumLength(s)            

        # else:
        #     return len(s)
            
        left = 0  # 初始化左指針
        right = len(s) - 1  # 初始化右指針

        while left < right and s[left] == s[right]:
            # 紀錄當前需要移除的字符
            current_char = s[left]
            
            # 移動左指針直到遇到不同的字符
            while left <= right and s[left] == current_char:
                left += 1
            
            # 移動右指針直到遇到不同的字符
            while right >= left and s[right] == current_char:
                right -= 1

        # 計算剩餘字符串的長度
        return right - left + 1

sol = Solution()
sol.minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb")