class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        values = [0] * length

        values[0] = nums[0]

        for i in range(1,length):
            needed = target - nums[i]
            for j in range(0,i) :
                if values[j] == needed:
                    result = [0] * 2
                    result[0] = j
                    result[1] = i
                    return result
            values[i] = nums[i]

        return [0,0]