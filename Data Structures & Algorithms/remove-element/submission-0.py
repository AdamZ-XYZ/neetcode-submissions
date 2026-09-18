class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
       #Itterate through list
       #Write it in place
       #Write i,j 
       #pos 
    
        k = 0

        for current in range(len(nums)):
           if nums[current] != val:
            nums[k] = nums[current]
            k += 1 
        
        return k
            
