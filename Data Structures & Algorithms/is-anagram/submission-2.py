class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        letters = {}

        for char in s:
            if char not in letters:
                letters[char] = 1
            else:
                 letters[char] += 1
        print(letters)

        for char in t:
            if char not in letters:
                return False
            else:
                letters[char] -= 1
        print(letters)
        
        for letter,count in letters.items():
            print(count)
            if count != 0:
                return False
        return True
