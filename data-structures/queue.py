__author__ = 'Kyle DeRosa'

from collections import deque

queue = deque(['Spike', 'Jet', 'Faye'])

# add
queue.append('Faye')

# delete
queue.popleft()

# search
'Spike' in queue


# Big O test
# insert (1); insert into end of queue
# delete (1); delete first element
# search (worst case, n); traverse list and find at final element
#               note, deque has pointers at both end,
#               with O(1) at the ends, and O(n) in the middle
# sorted search (worst case, n); still must traverse entire list,
#                               unless indexed O(logn) binary search
# sort (n^2),  insertion or selection sort
# sort (n lg n), if indexed, merge sort
