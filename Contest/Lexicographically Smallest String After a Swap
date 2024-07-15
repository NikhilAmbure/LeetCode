class Solution(object):
    def getSmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res1 = [int(i) for i in s]
        s = [int(i) for i in s]
        
        for i in range(1, len(s), 1):
            c = [c for c in s]
            if c[i] % 2 == c[i-1] % 2:
                c[i], c[i-1] = c[i-1], c[i]
                if c < res1:
                    res1 = c
        return "".join([str(i) for i in res1])
