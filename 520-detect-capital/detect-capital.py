class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        uppercase=0

        for i in range(len(word)):
            if word[i].isupper():
                uppercase+=1
        
        if uppercase== len(word) or uppercase ==0 or uppercase==word[0].isupper():
            return True
        
        return False