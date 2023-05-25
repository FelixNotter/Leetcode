class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for index in range(len(strs[0])):
            for word in strs:
                if len(word) == index or word[index] != strs[0][index]:
                    return res
            res += strs[0][index]
        return res
