def minimumPushes(self, word):
        letters = Counter(word)
        c = 1
        res = 0

        for i, j in sorted(letters.items(), key=lambda x:x[1], reverse=True):
            if c <= 8:
                res += (1 * j)
            elif c <= 16:
                res += (2 * j)
            elif c <= 24:
                res += (3 * j)
            elif c <= 26:
                res += (4 * j)
            c+=1
        return res
