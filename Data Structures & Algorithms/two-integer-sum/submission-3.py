class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        values = {}
        values[nums[0]] = 0

        for i in range(1,length):
            needed = target - nums[i]
            if needed in values:
                result = [0] * 2
                result[0] = values[needed]
                result[1] = i
                return result
            values[nums[i]] = i

