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
            
        left = 0  # ��l�ƥ����w
        right = len(s) - 1  # ��l�ƥk���w

        while left < right and s[left] == s[right]:
            # ������e�ݭn�������r��
            current_char = s[left]
            
            # ���ʥ����w����J�줣�P���r��
            while left <= right and s[left] == current_char:
                left += 1
            
            # ���ʥk���w����J�줣�P���r��
            while right >= left and s[right] == current_char:
                right -= 1

        # �p��Ѿl�r�Ŧꪺ����
        return right - left + 1

sol = Solution()
sol.minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb")