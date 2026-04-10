class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        check_dict = {}
        
        for idx in range(len(strs)):

            if tuple(sorted(strs[idx])) not in check_dict:

                dummy = []
                dummy.append(strs[idx])
                check_dict[tuple(sorted(strs[idx]))] = 0

                for idx2 in range(idx+1, len(strs)):

                    if strs[idx2] not in check_dict:

                        if sorted(strs[idx]) == sorted(strs[idx2]):

                            dummy.append(strs[idx2])
                            check_dict[tuple(sorted(strs[idx]))] = 0 

                lst.append(dummy)   

        return lst
