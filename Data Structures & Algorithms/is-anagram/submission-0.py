class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        else:
            h1=dict([])
            h2=dict([])
            for i in range(len(s)):
                h1[s[i]]=h1.get(s[i],0)+1
                h2[t[i]]=h2.get(t[i],0)+1
            
            if len(h1)!=len(h2):
                return False
            
            for key,value in h1.items():
                if h2.get(key,0)!=value:
                    return False
            
            return True



        