class Solution(object):
    def doesAliceWin(self, s):
        Alice_score = 0
        Bob_score = 0
        c = 0
        vowels = set('aeiou')
        count = 0

        for i, char in enumerate(s):
            if char in vowels:
                count+=1
            if count % 2 == 1 and c%2==0:
                Alice_score+=1
                c+=1
            elif count % 2 == 0 and c%2==1:
                Bob_score+=1
                c+=1
        if Alice_score == 0:
            return False
        return Alice_score >= Bob_score
