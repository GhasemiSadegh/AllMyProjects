import queue

""""Learning Advanced Data Structures"""

q = queue.Queue()
nums = [2, 4, 6, 8, 10]
for num in nums:
    q.put(num)

print(q.get())
print(q.get())