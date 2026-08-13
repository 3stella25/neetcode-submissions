from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Group into sublists- sort and find things with same sorted contents. Use dict
        tracker = defaultdict(list)

        for s in strs:
            sorted_s = sorted(s)
            anagram = "".join(sorted_s)

            tracker[anagram].append(s)
        
        return list(tracker.values())



        