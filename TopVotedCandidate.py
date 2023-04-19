"""
        You are given two integer arrays persons and times. In an election, the ith vote was cast for persons[i] at time times[i].
        For each query at a time t, find the person that was leading the election at time t. Votes cast at time t will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.
                        
        Explanation
        topVotedCandidate = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
        topVotedCandidate.q(3); // return 0, At time 3, the votes are [0], and 0 is leading.
        topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and 1 is leading.
        topVotedCandidate.q(25); // return 1, At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
        topVotedCandidate.q(15); // return 0
        topVotedCandidate.q(24); // return 0
        topVotedCandidate.q(8); // return 1
"""
from bisect import bisect_right
from collections import defaultdict

class TopVotedCandidate:
    def __init__(self, persons, times):
        self.leaders = {}
        self.times = times
        vote_count = defaultdict(int)  # Replace the dictionary with a defaultdict
        leader = -1

        for i, person in enumerate(persons):
            time = times[i]
            vote_count[person] += 1  # Simplify the vote count update
            if vote_count[person] >= vote_count[leader]:
                leader = person
            self.leaders[time] = leader

    def q(self, t):
        index = bisect_right(self.times, t)
        if index == 0:
            return self.leaders[self.times[0]]
        if index == len(self.times):
            return self.leaders[self.times[-1]]
        time = self.times[index - 1]
        return self.leaders[time]


topVotedCandidate = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
print(topVotedCandidate.q(3) == 0)
print(topVotedCandidate.q(12) == 1)
print(topVotedCandidate.q(25) == 1)
print(topVotedCandidate.q(15) == 0)
print(topVotedCandidate.q(24) == 0)
print(topVotedCandidate.q(8) == 1)
