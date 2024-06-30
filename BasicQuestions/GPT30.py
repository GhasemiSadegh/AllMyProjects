# Q5 palindrome
word = input('Write it: ')
str_lng = int(len(word))
baraskshode = word[::-1]
print(baraskshode)
if word == baraskshode:
    print("ok")
else:
    print('not ok')
# Q6
list_vorodi = input('Enter a list of numbers:')
list_joda = list_vorodi.split()
print(list_joda)
for i in range(0, int(len(list_joda))):
    list_joda[i] = int(list_joda[i])
print(max(list_joda))
# Q7 Max
list_vorodi = input('Enter a list of numbers:')
list_joda = list_vorodi.split()

for i in range(0, int(len(list_joda))):
    list_joda[i] = int(list_joda[i])
print(list_joda)
maximum = 0
for j in range(0, int(len(list_joda))): #  6 5 4
    if list_joda[j] > maximum:
         maximum = list_joda[j]
    else:
        j += 1
print(maximum)

# Q8
word = list(input("type a word: "))
print(word)
count = 0
for i in ('a', 'e', 'i', 'o', 'u'):
    if i in word:
       count += 1
print(count)
# Q9
given_number = int(input('Write a number: '))
for i in (2, 3, 5, 7):
    if given_number == 2:
        print('it is prime and 2')
        break
    if given_number%i == 0:
        print('not prime')
        break
else:
    print('it is prime')
# Q10
word = 'hello'
reversed_word = ''
length = int(len(word) - 1)
for i in range(length, -1, -1):
    reversed_word += word[i]
print(reversed_word)
# Q11
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
list_1 = []
list_2 = []
for i in range(1, a):
    if a % i == 0:
        list_1.append(i)
print(list_1)
for j in range(1, b):
    if b % j == 0:
        list_2.append(j)
print(list_2)
x = list(set(list_1).intersection(list_2))
cgd = print(max(x))

# Q12 Number of words in a sentence
sentence = input('write a sentence here: ')
devided = list(sentence)
print(devided)
count = 0
for i in devided:
    if i == ' ':
        count += 1
print(count + 1)

# Q13 second largest number
list_vorodi = input('Enter a list of numbers separated by comma: ')
list_joda = list_vorodi.split(',')
list_asli = [int(num) for num in list_joda]
print(list_asli)
list_asli.sort()
print(list_asli)
print(list_asli[len(list_asli) - 2])

# Q14 Remove Duplicates
user_list = input('Please write a list with comma: \n')
list_divided = user_list.split(',')
list_divided = [int(num) for num in list_divided]
print("Original list:", list_divided)
list_final = list(set(list_divided))
list_final.sort()
print("List without duplicates:", list_final)

# Q15: Leap year
try:
    year = int(input('Enter the year: '))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f'year {year} is a leap year')
    else:
        print(f'year {year} is not a leap year')
except ValueError:
    print('Number only')

# Q 16: Factorial
try:
    number = int(input('Enter a number: '))
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f'The factorial of {number} is {factorial}')
except ValueError:
    print('Please enter a valid number')

# Q 17: all alphabet included
sentence = input('write a sentence here: ').lower()
devided = set(sentence)
final_list = []
for i in ('a', 'b', 'c'):
    if i in devided:
        final_list.append(i)
print(final_list)
set(final_list)
if len(final_list) == 3:
    print("all letters included")
else:
    print('not ok')

# Q extra Sep and End
list_1 = []
for i in range (10):
    list_1.append(i)
print(*list_1, sep='x', end='!!')

# Q 17_2: Pangram, all alphabet included
import string

text = input('Write here: ').lower()

# Create a set of all alphabet letters
alphabet_set = set(string.ascii_lowercase)

# Create a set of letters found in the input text
letters_found = set(text)

# Check if all alphabet letters are in the text
if alphabet_set.issubset(letters_found):
    print("The text is a pangram.")
else:
    print("The text is not a pangram.")

# Q 18 Even numbers from given list
message_divided = input('here: ')
message_divided = message_divided.split(' ')
message_divided = [int(num) for num in message_divided]
list_even = []
for i in range(0, int(len(message_divided))):
    if message_divided[i] % 2 == 0:
        list_even.append(message_divided[i])
print(sum(list_even))

# Q 19 alphabet, total letters
message = input('Enter a string: ')
message = message.lower()  # Convert to lowercase to count characters case-insensitively

# Initialize an empty dictionary to store character counts
char_count = {}

# Loop through each character in the message
for char in message:
    if char.isalpha():  # Consider only alphabetic characters
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

# Print the character counts
for char, count in char_count.items():
    print(f"{char}: {count}")

# Q 20 find max min
list_user = input('Here with space: ')
list_user = list_user.split(' ')
list_user = [int(num) for num in list_user]
largest = max(list_user)
smallest = min(list_user)
print(f'largest is {largest} and the smallest is {smallest}')

# Q 20 number of vowels
final_list = {}

for char in user_list:
    if char in ('a', 'i', 'o', 'e', 'u'):
        if char in final_list:
            final_list[char] += 1
        else:
            final_list[char] = 1

for char, count in final_list.items():
    pass
print(dict(final_list.items()))

# Q 21
def is_palindrome(string_one):
    divided =list(string_one)
    print(divided)
    new = divided[::-1]
    print(new)
    if new == divided:
        print('ok')
    else:
        print("no")


is_palindrome('rad')

# Q 22 dictionaries creation with zip
a = ['a', 'b']
b = [1, 2]
my_dict = {}
for i, j in zip(a, b):
    my_dict[i] = j
print(my_dict)
# or
print(dict(zip(a, b)))

# Q 23 one list, one dictionary
def key_val_creator(my_list):
    if len(my_list) % 2 == 0:
        my_dict = {}
        list_key = []
        list_value = []
        for num in my_list:
            if num % 2 != 0:
                list_key.append(num)
            else:
                list_value.append(num)
        print(dict(zip(list_key, list_value)))
    else:
        print('even number of numbers is needed')


my_list = input('write a set a of numbers: ')
new_list = [int(item) for item in my_list.split(' ')]
print(new_list)
key_val_creator(new_list)

# Q 24 remove duplicates


def duplicate_remover(my_list):
    li = []
    for i in my_list:
        if i not in li:
            li.append(i)
    return li


given_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 6, 6, 7 , 8, 8, 9]
print(duplicate_remover(given_list))

# Q 25


def has_common_elements(list1, list2):
    if len(set(list1).intersection(list2)) == 0:
        return False
    else:
        return True


x = [1, 2, 4]
y = [3, 4]

print(has_common_elements(x, y))


# Q 26

def reverse_list(li):
    li_reversed = []
    for i in range(len(li) - 1, -1, -1):
        li_reversed.append(li[i])
    return li_reversed


li = ['a', 'b', 'c']
print(reverse_list(li))

# Q 27


