# 1: reverse without revers function
def sort_list(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

numbers = [3, 10, 7, 8, 1]
print(sort_list(numbers))

# 2: char_count

def char_count(s):
    my_dict = {}
    for char in s:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict

print(char_count('allalab'))

# Q 3: second largest without sorted


def second_largest(my_list):
    first = second = float('-inf')
    for num in my_list:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second


numbers = [3, 5, 4]
print(second_largest(numbers))

# Q 4


def sum_of_squares(lst):
    return sum(x**2 for x in lst)


li = [1, 2, 3]
print(sum_of_squares(li))


# Q 5
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
print(factorial(5))

# Q 6