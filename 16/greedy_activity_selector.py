from collections import namedtuple

Activity = namedtuple("Activity", ("start", "end"))

"""

    GreddyActivity Class Solution

"""


class GreedyActivity:

    def __init__(self, starts, ends):

        self.initialize(starts, ends)

    def initialize(self, starts, ends):

        self._lists = []
        for start, end in zip(starts, ends):
            self._lists.append(Activity(start, end))

        self._lists.sort(key=lambda x : x.end)

    def selector(self):

        start_length = len(self._lists)
        activity_list = [1,]
        k = 1

        for m in range(1, start_length):
            if self._lists[m].start >= self._lists[k].end:
                activity_list.append(k + 1)
                k = m
        return activity_list

"""

    GreedyActivity Function Solution

"""


def GreedyActivitySelector(start, finish):

    start_length = len(start)
    activity_list = [1,]
    k = 1
    for m in range(1, start_length):
        if start[m] >= finish[k]:
            activity_list.append(k + 1)
            k = m
    return activity_list

if __name__ == "__main__":

    starts = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    ends = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    print(GreedyActivitySelector(starts, ends))

    greedy_activity = GreedyActivity(starts, ends)
    print(greedy_activity.selector())

