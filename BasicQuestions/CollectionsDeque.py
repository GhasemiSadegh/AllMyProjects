import queue

""""Learning Advanced Data Structures"""
"""First In First Out, FIFO"""

q = queue.Queue()
nums = [2, 4, 6, 8, 10]
for num in nums:
    q.put(num)

print(q.get())
print(q.get())

"""Last In First Out, LIFO"""
q_reverse = queue.LifoQueue()
for num in nums:
    q_reverse.put(num)

print(q_reverse.get())
