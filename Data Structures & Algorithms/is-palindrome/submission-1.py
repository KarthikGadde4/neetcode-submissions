class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedStr = "".join(char for char in s if char.isalnum())
        cleanedStr = cleanedStr.lower()
        
        left = 0
        right = len(cleanedStr) - 1

        while(left < right):
            if(cleanedStr[left] != cleanedStr[right]):
                return False
            
            left += 1
            right -= 1
        return True
