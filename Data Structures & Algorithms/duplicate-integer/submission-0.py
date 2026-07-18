class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        more = []
        for num in nums:
            if num in more:
                return True
            else: 
                more.append(num)
        return False
        