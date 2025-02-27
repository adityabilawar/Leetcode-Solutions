class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #intitialize dict (hash map) where the key is the sorted string and the value is teh list of original stringts that match signature
        # 1. sort th estring to get sorted s and then 2. append s to groups [sorted_s]
        #return group values
        groups = defaultdict(list)
        
        for s in strs:
            sorted_s = ''.join(sorted(s))

            groups [sorted_s].append(s)
        return list(groups.values())
        