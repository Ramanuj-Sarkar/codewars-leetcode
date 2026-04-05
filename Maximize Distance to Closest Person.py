class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # find where all the people are sitting
        people = [num for num, x in enumerate(seats) if x == 1]
        
        # find the distances between the people on either side
        distances = [(people[x] - people[x-1]) // 2 for x in range(1,len(people))]

        # what if you could sit in seat 0
        if seats[0] == 0:
            distances.append(people[0])
        
        # what if you could sit in the last seat
        if seats[-1] == 0:
            distances.append(len(seats) - people[-1] - 1)
        
        return max(distances)
