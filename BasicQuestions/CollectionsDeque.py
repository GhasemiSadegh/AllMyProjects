import queue

""""Learning Advanced Data Structures"""
"""First In First Out, FIFO"""

q = queue.Queue()
nums = [12, 2, 4, 6, 8, 10]
for num in nums:
    q.put(num)

print(q.get())
print(q.get())

"""Last In First Out, LIFO"""
q_reverse = queue.LifoQueue()
for num in nums:
    q_reverse.put(num)

print(q_reverse.get())

"""Priority Queue"""
q_prio = queue.PriorityQueue()
tuple_list = [(1, 'hi'), (0, 'why'), (4, 'die')]

for item in tuple_list:
    q_prio.put(item)

while not q_prio.empty():
    print(q_prio.get())

while not q_prio.empty():
    print(q_prio.get()[0])

while not q_prio.empty():
    print(q_prio.get()[1])