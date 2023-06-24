class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reverse = []
        for num in nums:
            s = str(num)
            reverse.append(int(s[::-1]))
        return len(set(nums+reverse))
