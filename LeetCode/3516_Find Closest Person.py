class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1 = abs(x-z)
        d2 = abs(y-z)
        ans = d1-d2
        if ans == 0:
            return 0
        elif ans < 0:
            return 1
        else:
            return 2

sol = Solution()
result1 = sol.findClosest(3, 8, 5)
print(f"�d�� (3, 8, 5): ���G�O {result1}")

# �d�� 2
result2 = sol.findClosest(10, 1, 4)
print(f"�d�� (10, 1, 4): ���G�O {result2}")

# �d�� 3
result3 = sol.findClosest(2, 8, 5)
print(f"�d�� (2, 8, 5): ���G�O {result3}")