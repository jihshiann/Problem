class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        if not meetings:
            return days
        
        # meetings�Ƨ�
        meetings_sort = sorted(meetings)
        
        # ��l�ƲĤ@�ӦX�ְ϶�
        merged_start, merged_end = meetings_sort[0][0], meetings_sort[0][1]
        covered_days = 0
        
        # �q�ĤG�ӷ|ĳ�}�l�X��
        for i in range(1, len(meetings_sort)):
            start, end = meetings_sort[i]
            # �Y��e�|ĳ�P�X�ְ϶������|�άO�s�� (meeting[0] <= merged_end + 1)
            if start <= merged_end:
                merged_end = max(merged_end, end)
            else:
                # �N�W�@�ӦX�ְ϶��л\���ѼƲ֭p 
                covered_days += merged_end - merged_start + 1
                merged_start, merged_end = start, end
        
        # �֭p�̫�@�ӦX�ְ϶����л\�Ѽ�
        covered_days += merged_end - merged_start + 1
        
        # �i�ΤѼ� = �`�Ѽ� - �Q�|ĳ�л\���Ѽ�
        return days - covered_days

def test_solution():

    sol = Solution()

    # ���ծר� 1
    days = 10
    meetings = [[5,7], [1,3], [9,10]]
    expected = 2
    result = sol.countDays(days, meetings)
    print("Test Case 1:", "Pass" if result == expected else f"Fail (expected {expected}, got {result})")

    # ���ծר� 2
    days = 5
    meetings = [[2,4], [1,3], [1,2]]
    expected = 1
    result = sol.countDays(days, meetings)
    print("Test Case 2:", "Pass" if result == expected else f"Fail (expected {expected}, got {result})")

    # ���ծר� 3
    days = 6
    meetings = [[1,6]]
    expected = 0
    result = sol.countDays(days, meetings)
    print("Test Case 3:", "Pass" if result == expected else f"Fail (expected {expected}, got {result})")

if __name__ == "__main__":
    test_solution()
