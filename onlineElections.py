class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.track = defaultdict(int)
        self.votes = []
        max_person = self.persons[0]
        maximum = -1
        for person in self.persons:
            self.track[person]+=1
            if self.track[person] >= maximum:
                max_person = person
                maximum = self.track[person]
            self.votes.append(max_person)


    def q(self, t: int) -> int:
        l = bisect_left(self.times,t)
        if l == len(self.times):
            l-=1
        if t < self.times[l]:
            return self.votes[l-1]
        return self.votes[l]
        


        

        
      
        
        
    
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
