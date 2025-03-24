class Solution(object):
    def merge(self, intervals_sorted):
            merged_start, merged_end = intervals_sorted[0][0], intervals_sorted[0][1]
            mergedList = []
            flag = False

            for i in range(1, len(intervals_sorted)):
                start, end = intervals_sorted[i]
                # 天數重複則合併
                if start <= merged_end:
                    merged_end = max(merged_end, end)
                    flag = True
                else:
                    # 記錄已完成區間並開新區間
                    mergedList.append([merged_start, merged_end])
                    merged_start, merged_end = intervals_sorted[i]
            
            mergedList.append([merged_start, merged_end])
            mergedList = sorted(mergedList)

            while flag:
                return self.merge(mergedList)

            return mergedList

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals_sorted = sorted(intervals, key=lambda x: x[0])
        result = []
        
        result = self.merge(intervals_sorted)

        return result