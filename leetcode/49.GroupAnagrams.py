
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp_dict = {}
        for word in strs:
            sorted_word = sorted(word)
            key = ''.join(sorted_word)
            if key in tmp_dict:
                tmp_dict.get(key).append(word)
            else:
                tmp_dict[key] = [word]
        print(tmp_dict.values())
    

strs = ["eat","tea","tan","ate","nat","bat"]
Solution().groupAnagrams(strs)
