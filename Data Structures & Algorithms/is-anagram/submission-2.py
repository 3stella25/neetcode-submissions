class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        num = {

        }
        num2 = {

        }
        for thing in s:
            num.get(thing, 0) + 1
        for c in t:
            num2.get(c, 0) + 1
        if sorted(s) == sorted(t):
            return True
        return False
            
        


        