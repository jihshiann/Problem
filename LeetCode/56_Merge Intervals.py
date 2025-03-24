class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals_sorted = sorted(intervals)
        merged_start, merged_end = intervals_sorted[0][0], intervals_sorted[0][1]
        result = []
        for i in range(1, len(intervals_sorted)):
            start, end = intervals_sorted[i]
            # 天數重複則合併
            if start <= merged_end:
                merged_end = max(merged_end, end)
            else:
                # 記錄已完成區間並開新區間
                result.append([merged_start, merged_end])
                merged_start, merged_end = intervals_sorted[i]

        result.append([merged_start, merged_end])

        return result