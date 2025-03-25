class Solution(object):
    #���νu�������b�x����ɤW�B�������x�Τ����A�]���i�H�q�@�Ӥ�V�]�����Ϋ����^�ݡA�N�C�ӯx�Φb�Ӥ�V���϶�
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        #�i��X�֨íp��̫�o�쪺���s��϶��ƶq
        def merge_intervals(intervals):
            intervals.sort(key=lambda interval: interval[0])
            merged = []
            for interval in intervals:
                #��e�϶����_�l�ȬO�_�j��ε���̫�@�ӦX�ְ϶���������
                if not merged or interval[0] >= merged[-1][1]:
                    merged.append(interval[:])
                else:
                    # ���|�h�X�֡A��s�����Ȭ����j��
                    merged[-1][1] = max(merged[-1][1], interval[1])
            return len(merged)
        
        total = len(rectangles)
        if total < 3:
            return False
        
        # ���o�Ҧ��x�Φb y �b�W���϶� [starty, endy]
        y_intervals = []
        # ���o�Ҧ��x�Φb x �b�W���϶� [startx, endx]
        x_intervals = []
        for rect in rectangles:
            # rect = [startx, starty, endx, endy]
            x_intervals.append([rect[0], rect[2]])
            y_intervals.append([rect[1], rect[3]])
        horizontal_groups = merge_intervals(y_intervals)
        # �Y�䤤�@��V�W�i�H���X�ܤ֤T�Ӥ��s��϶��A��ܦs�b��Ӥ��νu�i�N�x�Τ����T��
        if horizontal_groups >= 3:
            return True
        
        vertical_groups = merge_intervals(x_intervals)
        # �Y�䤤�@��V�W�i�H���X�ܤ֤T�Ӥ��s��϶��A��ܦs�b��Ӥ��νu�i�N�x�Τ����T��
        if vertical_groups >= 3:
            return True

        return False


# ���սd��
if __name__ == '__main__':
    sol = Solution()

    n = 5
    rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
    print(sol.checkValidCuts(n, rectangles))  # �w����X True

    n = 4
    rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
    print(sol.checkValidCuts(n, rectangles))  # �w����X True

    n = 4
    rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
    print(sol.checkValidCuts(n, rectangles))  # �w����X False
