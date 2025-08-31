class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result_chars = []
        while columnNumber > 0:
            # �l0 => A
            columnNumber -= 1

            remainder = columnNumber % 26
            
            # �N�l���ഫ�� ASCII
            # ord('A') �O 'A' �� ASCII �X
            result_chars.append(chr(ord('A') + remainder))
            
            columnNumber //= 26

        # 5. �ݭn����C��
        return "".join(reversed(result_chars))

# --- ���սd�� ---
solver = Solution()

# Example 1:
columnNumber1 = 1
print(f"Input: {columnNumber1}, Output: \"{solver.convertToTitle(columnNumber1)}\"") # ���� "A"

# Example 2:
columnNumber2 = 28
print(f"Input: {columnNumber2}, Output: \"{solver.convertToTitle(columnNumber2)}\"") # ���� "AB"

# Example 3:
columnNumber3 = 701
print(f"Input: {columnNumber3}, Output: \"{solver.convertToTitle(columnNumber3)}\"") # ���� "ZY"

# ��ɴ���
columnNumber4 = 26
print(f"Input: {columnNumber4}, Output: \"{solver.convertToTitle(columnNumber4)}\"") # ���� "Z"

columnNumber5 = 52
print(f"Input: {columnNumber5}, Output: \"{solver.convertToTitle(columnNumber5)}\"") # ���� "AZ"