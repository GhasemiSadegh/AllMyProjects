from collections import deque

names = ["Alexander", "Emily", "Michael", "Sophia",
         "Benjamin", "Olivia", "James", "Isabella", "William", "Mia"]
my_deque = deque(names)
my_deque.append('Ali')
my_deque.appendleft('Feri')
my_deque.pop()
my_deque.popleft()
my_deque.remove('Emily')
my_deque.extend(['Gholi','Ghasem'])
print(my_deque)
my_deque.reverse()
print(my_deque)
my_deque.rotate() # [+1]
print(my_deque)
my_deque.rotate(-3)
print(my_deque)