# Implement a calendar where you can book events
# Three or more events cannot overlap
class MyCalendarTwo:

    def __init__(self):
        # Store the number of bookings at each point.
        self.booking_count = SortedDict()
        # The maximum number of overlapped bookings allowed.
        self.max_overlaps = 2

    def book(self, start: int, end: int) -> bool:
        '''
        Try to add an event to the calendar.
        If there are more than two events at a specific time,
        don't add the event and return False.
        Otherwise, add the event and return True.
        '''
        # Increase and decrease the booking count at the start and end respectively.
        self.booking_count[start] = self.booking_count.get(start, 0) + 1
        self.booking_count[end] = self.booking_count.get(end, 0) - 1

        overlaps = 0

        # Calculate the prefix sum of bookings.
        for count in self.booking_count.values():
            overlaps += count
            # If the number of overlaps exceeds the allowed limit
            # rollback and return False.
            if overlaps > self.max_overlaps:
                # Rollback changes.
                self.booking_count[start] -= 1
                self.booking_count[end] += 1

                # Remove entries if their count becomes zero to clean up the SortedDict.
                if self.booking_count[start] == 0:
                    del self.booking_count[start]

                return False

        return True
