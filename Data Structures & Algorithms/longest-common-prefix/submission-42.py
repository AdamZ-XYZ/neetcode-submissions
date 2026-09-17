class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #Take letter - itterate through list of words - fail/pass 
        #Missing Out of bounds cases


        firstWord = strs[0]

        if len(firstWord) == 0:
            return ""

       
        #Itterate through letters
        for letterNumber in range(len(firstWord)):
            print(letterNumber)

            #itterate through words
            for i in range(1,len(strs)):
                currentWord = strs[i]
                
                if len(currentWord) == 0:
                    return ""

                if len(currentWord) < letterNumber+1:
                    return firstWord[:letterNumber]
            
                if firstWord[letterNumber] != currentWord[letterNumber]:
                    print("EARLY")
                    return firstWord[:letterNumber]

        return firstWord[:letterNumber+1]               
                

        