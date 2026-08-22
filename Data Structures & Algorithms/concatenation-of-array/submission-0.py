class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        length = len(nums)
        out = [0] * (length * 2)

        for i in range(length):
            out[i] = nums[i] 
            out[i+length] = nums [i]
        
        return out
            