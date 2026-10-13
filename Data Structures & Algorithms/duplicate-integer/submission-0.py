class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h=dict([])
        for el in nums:
            if (h.get(el,0))>0:
                return True
            else:
                h[el]=1
        else:
            return False

        
        