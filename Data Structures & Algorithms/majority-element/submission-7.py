class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #nums.sort()
        #return nums[int(len(nums)/2)]

        candidate = -1
        votes = 0

        for current in range(len(nums)):
            if votes == 0:
                candidate = nums[current]
                votes = 1
            elif  nums[current] == candidate:
                votes += 1
            elif nums[current] != candidate:
                votes -= 1
        
        confirm = 0
        for check in range(len(nums)):
            if nums[check] == candidate:
                confirm += 1
        
    
        return candidate