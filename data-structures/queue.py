__author__ = 'Kyle DeRosa'

from collections import deque

queue = deque(['Spike', 'Jet', 'Faye'])

# add
queue.append('Ed')

# delete
queue.popleft()

# search
'Spike' in queue


# now for stacks

stack = deque(['Spike', 'Jet', 'Faye'])

# add
stack.append('Ed')

# delete
stack.pop()

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

# space
# n elements, with n pointers; (2n if pointers to and from)

# Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short
# for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from
# either side of the deque with approximately the same O(1) performance in either direction.

# Though list objects support similar operations, they are optimized for fast fixed-length
# operations and incur O(n) memory movement costs for pop(0) and insert(0, v) operations which
# change both the size and position of the underlying data representation.

# If maxlen is not specified or is None, deques may grow to an arbitrary length. Otherwise,
#  the deque is bounded to the specified maximum length. Once a bounded length deque is full,
#  when new items are added, a corresponding number of items are discarded from the opposite end.
#  Bounded length deques provide functionality similar to the tail filter in Unix. They are also
#  useful for tracking transactions and other pools of data where only the most recent activity
# is of interest.
