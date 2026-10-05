from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        top_pair = count.most_common(k)
        return [num for num, val in top_pair]