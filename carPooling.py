from typing import List

"""
    There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).
    You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.
    Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.
    
    Example 1:
    Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    Output: false
    Example 2:
    
    Input: trips = [[2,1,5],[3,3,7]], capacity = 5
    Output: true
"""


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = []

        for trip in trips:
            num_passengers, start, end = trip
            timeline.append((start, num_passengers))
            timeline.append((end, -num_passengers))

        timeline.sort()

        current_passengers = 0
        for _, passengers in timeline:
            current_passengers += passengers
            if current_passengers > capacity:
                return False

        return True


trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4
print(Solution().carPooling(trips, capacity))

trips = [[2, 1, 5], [3, 3, 7]]
capacity = 5
print(Solution().carPooling(trips, capacity))
