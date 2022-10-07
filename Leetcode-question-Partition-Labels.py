def partitionLabels(self, s: str) -> List[int]: 
        d={}
        r,l=0,0 
        lst=[]
        for i in range(len(s)):
            d[s[i]]=i
        for i in range(len(s)):
            r=max(r,d[s[i]])
            if i==r:
                lst.append(r-l+1)
                l=r+1
        return lst
