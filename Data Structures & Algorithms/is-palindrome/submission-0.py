class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedStr = "".join(char for char in s if char.isalnum())
        cleanedStr = cleanedStr.lower()
        
        charsChecked = 0
        left = 0
        right = len(cleanedStr) - 1
        while(charsChecked != (len(cleanedStr))):
            if(len(cleanedStr) == 0 or len(cleanedStr) == 1):
                return True
            
            

            if(cleanedStr[left] != cleanedStr[right]):
                return False
            
            left += 1
            right -= 1
            charsChecked += 1
        return True
