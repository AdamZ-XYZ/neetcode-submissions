class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        values = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in values:
                return [values[needed],i]
    
      
            values[nums[i]] = i

