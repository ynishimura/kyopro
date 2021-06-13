from typing import List;

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # if len(words) == 1:
        #     return True
        # for i, word in enumerate(words):
        #     words.remove(word)

        #     joined_words = '-'.join(words)
        #     if word in joined_words:
        #         return True
        #     else:
        #         return False
        map_ = {}
        for word in words:
            for i in word:
                if i not in map_:
                    map_[i] = 1
                else:
                    map_[i] += 1
        n = len(words)
        for k,v in map_.items():
            if (v%n) != 0:
                return False
        return True

a = Solution()
print(a.makeEqual(["abc", "aabc", "bc"])) # true
print(a.makeEqual(["ab", "a"]))
print(a.makeEqual(["ab"])) # true
print(a.makeEqual(["abc", "cba"])) # true