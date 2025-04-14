class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        l = len(arr)
        ans = 0
        for i in range(l):
            for j in range(i+1, l):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1, l):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                            ans+=1
        return ans