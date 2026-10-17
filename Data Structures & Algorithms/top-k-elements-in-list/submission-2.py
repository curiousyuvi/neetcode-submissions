class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht=[0]*2001

        for num in nums:
            ht[num+1000]+=1
            
        pairs=[]

        for i in range(2001):
            if ht[i]>0:
                pairs.append((i-1000,ht[i]))

        pairs.sort(key=lambda pair:pair[1],reverse=True)

        output=[]

        for i in range(k):
            output.append(pairs[i][0])
        
        return output

            
        
        


        