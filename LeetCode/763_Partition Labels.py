class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        # hash
        seen = set()
        # 至少有一個字串
        ans = 1
        for char in s:
            # 已出現則字串+1
            if char in seen:
                ans += 1
                #新字串
                seen = set()
            seen.add(char)







if __name__ == '__main__':
    s = Solution()
    print(s.partitionString("abacaba")) #4

    