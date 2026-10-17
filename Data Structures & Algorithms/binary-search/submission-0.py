class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        s=0
        e=n-1
        while (s<e):
            m=(s+e)//2

            if target>nums[m]:
                s=m+1
            elif target<nums[m]:
                e=m-1
            else:
                 return m

        if s>e:
            return -1
        elif s==e and target==nums[s]:
            return s
        else:
            return -1


        