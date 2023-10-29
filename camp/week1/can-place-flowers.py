class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i in range(len(flowerbed)):
            left = 0 if i-1 == -1 else flowerbed[i-1]
            right = 0 if i+1 == len(flowerbed) else flowerbed[i+1]
            if n == 0:
                return True
            if not left and not right and not flowerbed[i]:
                flowerbed[i] = 1
                n-=1
        return n == 0
        
        