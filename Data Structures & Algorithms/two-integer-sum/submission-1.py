class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Add the shi you find into a dictionary, retrieve 
        #store the index in the value
        dic = {}
        for num in range(len(nums)):
            compl = target - nums[num]
            if compl in dic:
                return [dic[compl], num]
            else:
                dic[nums[num]] = num
        
                