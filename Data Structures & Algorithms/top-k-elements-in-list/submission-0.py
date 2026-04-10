class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        freq_list = sorted(freq_dict.values())
        kth = freq_list[-k]
        ret_list = []
        for key in freq_dict:
            if freq_dict[key] >= kth:
                ret_list.append(key)
        return ret_list

