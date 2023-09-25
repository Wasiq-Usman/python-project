# slicing string to get first, middle, and, last character of a name
str_1 = 'James'
print(str_1[::2])
# slicing string to get middle three characters
str_2 = 'JhonDipPeta'
print(str_2[4:7])
str_3 = 'JaSonAy'
print(str_3[5:7])
# appending new string in the middle of a string
s1 = 'Ault'
s2 = 'Kelly'
middle = len(s1) // 2
s3 = s1[:middle] + s2 + s1[middle:]
print(s3)
# Creating a new string that consists of first, middle, and last characters of each input string
s_1 = 'America'
s_2 = 'Japan'
middle_1 = len(s_1) // 2
middle_2 = len(s_2) // 2
s_3 = s_1[0] + s_2[0] + s_1[middle_1] + s_2[middle_2] + s_1[-1] + s_2[-1]
print(s_3)
# Arranging string characters such that lowercase letters should come first
my_string = 'PyNaTive'
upper_case = ''
lower_case = ''
for char in my_string:
    if char.islower():
        lower_case += char
    else:
        upper_case += char
new_string = lower_case + upper_case
print(new_string)
# Counting all letters, digits, and special symbols from a given string
str = '"P@#yn26at^&i5ve'
characters = 0
digits = 0
special_characters = 0
for char in str:
    if char.isalpha():
        characters += 1
    elif char.isdigit():
        digits += 1
    else:
        special_characters += 1
print('Chars = ', characters)
print('Digits = ', digits)
print('Symbols =', special_characters)
# string balance test
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
for char in str1:
    if char not in str2:
        string_check = False
    else:
        string_check = True
print(string_check)
#Creating a mixed string
mystring_1 = input('Enter first string: ')
mystring_2 = input('Enter second string: ')
mystring_3 = ''
pointer_1 = 0
pointer_2 = len(mystring_2)-1
while pointer_1 < len(mystring_1) and pointer_2 >=0:
    mystring_3 += mystring_1[pointer_1]
    mystring_3 += mystring_2[pointer_2]
    pointer_1 += 1
    pointer_2 -= 1
mystring_3 += mystring_1[pointer_1:]
mystring_3 += mystring_2[:pointer_2+1]
print('The final mixed string is: ', mystring_3)
# calculating sum and average of digits in a string
my_string_1 = input('Enter the string: ')
digit_sum = 0
digit_count = 0
for char in my_string_1:
    if char.isdigit():
        digit_sum += int(char)
        digit_count += 1
if digit_count > 0:
    average = digit_sum/digit_count
else:
    average = 0
print('The sum of digits in the string is: ', digit_sum)
print('The average of digits in the string is: ', average)
# counting number of times each character occurs in a string
str = input('Enter the string: ')
char_count = {}
for char in str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char, count in char_count.items():
    print(f"{char} occurs {count} times")
# number of times a string occurs with same first and last characters and with more than 2 characters.
list_input = input('Enter the elements of string separated by spaces: ')
list_1 = list_input.split()
str_count = 0
for str in list_1:
    if len(str) >=2 and str[0]==str[-1]:
        str_count += 1
    else:
        str_count += 0
print(str_count)
# converting temperature from celsius to fahrenheit
celsius_temp = float(input('Enter temperature in celsius: '))
fahrenheit_temp = (celsius_temp * 9/5) + 32
print('The value in fahrenheit is: ', fahrenheit_temp)
# taking input and printing a sentence
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
age = int(input('Enter your age: '))
print(f"{first_name} {last_name} is {age} years old")
# counting number of times a substring occurs in a string
main_string = input('Enter main string: ')
sub_string = input('Enter sub string: ')
sub_string_count = main_string.count(sub_string)
print(f"{sub_string} occurs {sub_string_count} times in {main_string}")












