class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasher = {}
        hasher2 = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in hasher:
                hasher[char] += 1
            else:
                hasher[char] = 1
        for char in t:
            if char in hasher2:
                hasher2[char] += 1
            else:
                hasher2[char] = 1

        return hasher == hasher2
                
        