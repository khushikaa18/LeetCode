class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase=set()
        uppercase=set()

        for ch in word:
            if ch.islower():
                lowercase.add(ch)
            else:
                uppercase.add(ch.lower())
        
        return len(lowercase & uppercase)


