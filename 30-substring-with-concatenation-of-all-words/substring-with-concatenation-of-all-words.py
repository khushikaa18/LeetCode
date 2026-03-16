class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len=len(words[0])
        num_len=len(words)
        total_len=word_len*num_len

        target=Counter(words)

        res=[]
        for i in range(word_len):
            left=i
            window={}
            count=0

            for right in range(i,len(s)-word_len+1,word_len):
                word=s[right:right+word_len]
                if word in target:
                    window[word]=window.get(word,0)+1
                    count+=1
                    while window[word]>target[word]:
                        left_word=s[left:left+word_len]
                        window[left_word]-=1
                        left+=word_len
                        count-=1

                    if count==num_len:
                        res.append(left)
                        left_word=s[left:left+word_len]
                        window[left_word]-=1
                        left+=word_len
                        count-=1
                else:
                    window.clear()
                    count=0
                    left=right+word_len
        return res