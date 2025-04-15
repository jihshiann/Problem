class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ans = 0
        for i,num_i in enumerate(arr):
            for j, num_j in enumerate(arr[i+1:], start = i+1):
                if abs(num_i - num_j) <= a:
                    for k, num_k in enumerate(arr[j+1:], start = j+1):
                        if abs(num_j- num_k) <= b and abs(num_i-num_k) <= c:
                            ans+=1
        return ans