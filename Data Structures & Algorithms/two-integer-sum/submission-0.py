class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h=dict([])

        for i in range(len(nums)):
            if target-nums[i] in h:
                return sorted([i,h[target-nums[i]]])
            else:
                h[nums[i]]=i
        
        