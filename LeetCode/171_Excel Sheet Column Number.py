class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            value = ord(char) - ord('A') + 1
            result = result * 26 + value
        
        return result


sol = Solution()
print(f"A �����s���O: {sol.titleToNumber('A')}")      # ��X: 1
print(f"Z �����s���O: {sol.titleToNumber('Z')}")      # ��X: 26
print(f"AA �����s���O: {sol.titleToNumber('AA')}")     # ��X: 27
print(f"AB �����s���O: {sol.titleToNumber('AB')}")     # ��X: 28
print(f"ZY �����s���O: {sol.titleToNumber('ZY')}")     # ��X: 701
print(f"FXSHRXW �����s���O: {sol.titleToNumber('FXSHRXW')}") # ��X: 2147483647
