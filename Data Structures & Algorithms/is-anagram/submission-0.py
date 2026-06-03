
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        from collections import Counter

        sfreq = Counter(s)
        tfreq = Counter(t)

        print(sfreq)
        print(tfreq)

        if sfreq == tfreq:
            return True
        return False

   