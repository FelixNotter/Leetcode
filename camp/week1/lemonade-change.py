class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        papers = {5:0,10:0,20:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                papers[5]+=1
            
            elif bills[i] == 10:
                if not papers[5]:
                    print(bills[i],i)
                    return False
                papers[5]-=1
                papers[10]+=1
            else:
                if not papers[5] or not papers[10]:
                    if papers[5] < 3:
                        return False
                    else:
                        papers[5]-=3
                    continue
                papers[5]-=1
                papers[10]-=1
                papers[20]+=1
        return True
            

        
        