# Q 1 filter and lambda
list = list(filter(lambda x: x > 1, (1, 4, 6)))

print(list)

# Q 2 map and lambda
list = list(map(lambda x: x - 1, (1, 4, 6)))

print(list)

# Q 3 reduce and lambda
import functools

li = [1, 5, 6, 21, 90]
li2 = functools.reduce(lambda x, y: x + y, li)

print(li2)

# Q 4 lambda odd/even counter
# even odd counter
list_1 = [1, 2, 4, 5, 7, 89, 800]

even = len(list(filter(lambda x: x % 2 == 0, list_1)))
odd = len(list(filter(lambda x: x % 2 != 0, list_1)))
print(f'even = {even} and odd = {odd}')

# Q 5
#
li = [('ali', 10), ('sad', 8), ('fer', 15), ('hali', 4)]
li.sort(key = lambda x: x[1])
print(li)

# Q 5 reverse
#
li = [('ali', 10), ('sad', 8), ('fer', 15), ('hali', 4)]
li.sort(key = lambda x: x[1], reverse= True)
print(li)