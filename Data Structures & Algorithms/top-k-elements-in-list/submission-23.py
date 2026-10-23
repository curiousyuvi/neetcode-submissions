
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m1={}

        for num in nums:
            m1[num]=m1.get(num,0)+1

        
        m2={}
        for key,value in m1.items():
            m2[value]=[*m2.get(value,[]),key]
        
        
        # bucket sort
        arr=[0]*10001


        for key,value in m1.items():
            arr[value]+=1
        
        
        output=[]
        i=k
        j=10000
        while i>0 and j>0:
            if arr[j]>0:
                output.extend(m2[j])
                i-=len(m2[j])
            j-=1

        return output           






            
        
        


        