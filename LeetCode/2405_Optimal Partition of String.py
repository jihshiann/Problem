class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last={}
        part_index = last_end = 0
        result = []
        #last = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            last[c] = i

        for i,c in enumerate(s):
            part_index = max(part_index, last[c])
            if i == part_index:
                result.append(i - last_end + 1)
                last_end = i + 1

        return result




if __name__ == '__main__':
    s = Solution()
    print(s.partitionLabels("abc"))

    