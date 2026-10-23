class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product=1
        post_product=1

        prefix=[1]*len(nums)
        postfix=[1]*len(nums)

        
        for i in range(len(nums)):
            pre_product*=nums[i]
            post_product*=nums[len(nums)-i-1]

            prefix[i]=pre_product
            postfix[len(nums)-i-1]=post_product
        
        outputs=[]
        for i in range(len(nums)):
            output=1
            if i>0:
                output*=prefix[i-1]
            if i<(len(nums)-1):
                output*=postfix[i+1]
            outputs.append(output)
        
        return outputs


        



        