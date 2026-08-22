class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()
        length = len(nums)
        for i in range(length):

            if nums[i] in seen:
                return True
            else: 
                seen.add(nums[i])        
        
        return False
            

        