class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        both = [(n,h) for n,h in zip(names,heights)]
        both.sort(key = lambda a: a[1],reverse = True)
        res = [name for name,height in both]
        return res
