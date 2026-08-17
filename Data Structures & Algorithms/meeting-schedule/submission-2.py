"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)
        current_end=intervals[0].end

        for interval in intervals[1:]:
            if interval.start<current_end:
                return False
            current_end=interval.end
        return True
