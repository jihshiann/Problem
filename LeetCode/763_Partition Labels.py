class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        # hash
        seen = set()
        # �ܤ֦��@�Ӧr��
        ans = 1
        for char in s:
            # �w�X�{�h�r��+1
            if char in seen:
                ans += 1
                #�s�r��
                seen = set()
            seen.add(char)







if __name__ == '__main__':
    s = Solution()
    print(s.partitionString("abacaba")) #4

    