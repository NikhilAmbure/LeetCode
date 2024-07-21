class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if k & ~n != 0:
            return -1
        res = k ^ n
        return bin(res).count('1')
