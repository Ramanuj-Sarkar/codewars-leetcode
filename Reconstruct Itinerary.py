'''
The list tickets consist of lists [from, to] representing the departure and the arrival airports of flights.

The tickets belong to a man departing from JFK, so you have to start at JFK.

JFK will be there.

Each of the tickets must be used once and only once.
'''
class Solution:
    def findItinerary(self, tickets):
        targets = defaultdict(list)
        # represent the connections between two airports
        # as lists which show all the connections that one airport has
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        
        # the actual route
        route = []
        
        def visit(airport):
            while targets[airport]:
                # pop this airport from this list
                # and visit it recursively
                visit(targets[airport].pop())
            
            # doing this appends the airports backwards
            route.append(airport)
        
        # you start at JFK
        visit('JFK')

        # you return the airports in the correct order
        # i.e. not backwards
        return route[::-1]
