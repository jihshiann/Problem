class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        ans = 0
        for num in range(low, high+1):
            digs = [int(d) for d in str(num)]
            lenth = len(digs)
            if lenth % 2 != 0:
                continue
            else:
                mid = lenth//2
                left = digs[:mid]
                right = digs[mid:]
                if sum(left) == sum(right):
                    ans += 1
        
        return ans
