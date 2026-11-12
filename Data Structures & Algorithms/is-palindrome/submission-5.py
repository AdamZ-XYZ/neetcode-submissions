class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #2 pointer from edge, runs in O(N)
        # Given it's not a max palindrome, but true/false edge makes more snese

        #Clean string
       
        s = s.lower()
        fixed = ""
        for c in s:
            if c.isalnum():
                fixed += c
        s = fixed        
        i = 0
        j = len(s)-1

        while i < j:
            
    

            if s[i] != s[j]:
                print(s[i],s[j])
                return False
            else:
                i += 1
                j -= 1
        return True

        


    