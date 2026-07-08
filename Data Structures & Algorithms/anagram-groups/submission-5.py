class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Brute force:
        have hashmap of the original 
        """

        #hashmap for the sorted anagrams
        original_sorted_map = {}
        res = []

        for i in range(len(strs)):
            sorted_word = tuple(sorted(strs[i]))
            if sorted_word in original_sorted_map:
                res[original_sorted_map[sorted_word]].append(strs[i])

            else:
                original_sorted_map[sorted_word] = len(res)
                res.append(([strs[i]]))
            
        return res
