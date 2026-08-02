class Solution:
    from collections import defaultdict
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # At each index, calculate the difference between the current index and the target. Add the value and current index into a set or dict to keep track, then keep going unless remainder is in the seen set or dict. If it is, return the index of the remainder
        found = defaultdict()
        for index, value in enumerate(nums):
            remain = target - value 
            if remain in found:
                return [found[remain], index]
            else:
                found[value] = index

        
                       