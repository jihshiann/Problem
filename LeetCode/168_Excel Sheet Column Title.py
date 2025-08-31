class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result_chars = []
        while columnNumber > 0:
            # 餘0 => A
            columnNumber -= 1

            remainder = columnNumber % 26
            
            # 將餘數轉換成 ASCII
            # ord('A') 是 'A' 的 ASCII 碼
            result_chars.append(chr(ord('A') + remainder))
            
            columnNumber //= 26

        # 5. 需要反轉列表
        return "".join(reversed(result_chars))

# --- 測試範例 ---
solver = Solution()

# Example 1:
columnNumber1 = 1
print(f"Input: {columnNumber1}, Output: \"{solver.convertToTitle(columnNumber1)}\"") # 應為 "A"

# Example 2:
columnNumber2 = 28
print(f"Input: {columnNumber2}, Output: \"{solver.convertToTitle(columnNumber2)}\"") # 應為 "AB"

# Example 3:
columnNumber3 = 701
print(f"Input: {columnNumber3}, Output: \"{solver.convertToTitle(columnNumber3)}\"") # 應為 "ZY"

# 邊界測試
columnNumber4 = 26
print(f"Input: {columnNumber4}, Output: \"{solver.convertToTitle(columnNumber4)}\"") # 應為 "Z"

columnNumber5 = 52
print(f"Input: {columnNumber5}, Output: \"{solver.convertToTitle(columnNumber5)}\"") # 應為 "AZ"