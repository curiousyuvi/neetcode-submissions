
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m1={}

        for num in nums:
            m1[num]=m1.get(num,0)+1

        
        # bucket sort
        arr=[[]]*10001


        for key,value in m1.items():
            arr[value]=[*arr[value],key]
        
        
        output=[]
        i=k
        j=10000
        while i>0 and j>0:
            if len(arr[j])>0:
                output.extend(arr[j])
                i-=len(arr[j])
            j-=1

        return output           






            
        
        


        