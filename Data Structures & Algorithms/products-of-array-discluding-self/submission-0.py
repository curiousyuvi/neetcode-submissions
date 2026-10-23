class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        zeroes=[]

        for i in range(len(nums)):
            if(nums[i]==0):
                zeroes=[*zeroes,i]
            else:
                product*=nums[i]
            

        if len(zeroes)>1:
            return [0]*len(nums)
        elif len(zeroes)==1:
            output=[0]*len(nums)
            output[zeroes[0]]=product
            return output
        else:
            output=[]

            for num in nums:
                output.append(int(product/num))
            
            return output



        