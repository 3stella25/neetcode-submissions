class Solution:
    #push on open
    #pop on close
    #if not empty when you reach the end, or close != open when pop, return false
    def isValid(self, s: str) -> bool:
        arr = []
        for b in s:
            if not arr and b not in "[{(":
                return False
            if b in "[{(":
                arr.append(b)
            else:
                bob = arr.pop() 
                if not ((bob == "{" and b == "}") or (bob == "[" and b == "]") or (bob == "(" and b == ")")):
                    return False
                    
        return len(arr) == 0


        