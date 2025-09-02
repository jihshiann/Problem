class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            value = ord(char) - ord('A') + 1
            result = result * 26 + value
        
        return result


sol = Solution()
print(f"A 的欄位編號是: {sol.titleToNumber('A')}")      # 輸出: 1
print(f"Z 的欄位編號是: {sol.titleToNumber('Z')}")      # 輸出: 26
print(f"AA 的欄位編號是: {sol.titleToNumber('AA')}")     # 輸出: 27
print(f"AB 的欄位編號是: {sol.titleToNumber('AB')}")     # 輸出: 28
print(f"ZY 的欄位編號是: {sol.titleToNumber('ZY')}")     # 輸出: 701
print(f"FXSHRXW 的欄位編號是: {sol.titleToNumber('FXSHRXW')}") # 輸出: 2147483647
