class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        left = maxi = max_f = 0

        for right in range(len(s)):
            window[s[right]] += 1
            max_f = max(max_f, window[s[right]])

            while (right-left+1) - max_f > k:
                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1
            maxi = max(maxi, right-left+1)

        return maxi
