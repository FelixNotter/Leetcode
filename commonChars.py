class Solution:
    def commonChars(self,words):
      #initialise our check map
        check = Counter(words[0])
        for word in words[1:]:
          #update the check as we iterate
            newCheck = defaultdict(int)
            for letter in word:
                if check[letter]:
                    newCheck[letter] += 1
                    check[letter] -= 1
            check = newCheck
        res = []
        #convert the check dictionary into our result array
        for key in check:
            for _ in range(check[key]):
                res.append(key)
        return res
