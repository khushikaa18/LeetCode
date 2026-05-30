class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pf=Counter(p)
        wf=Counter(s[:len(p)])

        needed=len(pf)
        matches=sum(1 for c in pf if wf[c]==pf[c])
        res=[0] if matches==needed else []

        for r in range(len(p),len(s)):
            rc=s[r]
            if pf[rc] and wf[rc]==pf[rc]:
                matches-=1
            wf[rc]+=1
            if pf[rc] and wf[rc]==pf[rc]:
                matches+=1
            

            lc=s[r-len(p)]
            if pf[lc] and wf[lc]==pf[lc]:
                matches-=1
            wf[lc]-=1
            if pf[lc] and wf[lc]==pf[lc]:
                matches+=1
            
            if matches==needed:
                res.append(r-len(p)+1)
        
        return res
