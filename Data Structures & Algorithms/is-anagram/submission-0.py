class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        result  = [0] * 26

        

        for char in s:
            pos = ord(char)-ord('a')
            result[pos] += 1
            #print(result[pos])

        for char in t:
            pos = ord(char)-ord('a')
            result[pos] -= 1
            #print(result[pos])

        for let in result:


            if let != 0:
                return False

        
        
        return True