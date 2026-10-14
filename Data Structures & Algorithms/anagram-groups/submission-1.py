class Solution:
   
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def generateHashTable(string:str) -> List[int]:
            ht=[0]*26
            for c in string:
                ht[ord(c)-ord("a")]+=1
            return ht
        n=len(strs)
        hts=[[]]*n

        for i in range(n):
            hts[i]=generateHashTable(strs[i])
        
        covered=set([])
        groups=[]
        
        # for i in range(len(strs)):
        #     if i in covered:
        #         continue
        #     else:
        #         covered.add(i)
        #         group=[strs[i]]
        #         for j in range(len(strs)):
        #             if j in covered:
        #                 continue
        #             else:
        #                 if hts[i]==hts[j]:
        #                     covered.add(j)
        #                     group.append(strs[j])
        #         groups.append(group)

        h={}
        for i in range(n):
            hts_tuple=tuple(hts[i])
            if hts_tuple in h:
                h[hts_tuple].append(strs[i])
            else:
                h[hts_tuple]=[strs[i]]
        
        groups=list(h.values())

        return groups





        



        
        



        