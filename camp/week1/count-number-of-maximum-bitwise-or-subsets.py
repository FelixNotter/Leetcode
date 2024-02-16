class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = []

        def backtrack(i,curr):
            if i == len(nums):
                res.append(curr.copy())
                return 
            backtrack(i+1,curr+[nums[i]])
            backtrack(i+1,curr)
        backtrack(0,[])
        track = defaultdict(int)
        for sub in res:
            acc = 0
            for num in sub:
                acc= acc|num
            track[acc]+=1
        take = max(track.keys())
        return track[take]
        