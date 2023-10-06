book = {}
book['book_title'] = 'To kill a Mockingbird'
book['book_author'] = 'Harper Lee'
book['publishing_year'] = '1960'
print(book)
author_name = book.get('book_author')
print('The author of book is: ', author_name)
book['publishing_year'] = '2022'
print(book)
book['chapters'] = 'Chapter 1', 'Chapter 2', 'Chapter 3'
print(book)
del book['publishing_year']
print(book)
keys = book.keys()
for key in keys:
    print(key)
values = book.values()
for value in values:
    print(value)
my_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(my_dict)
merged_dict = {**book, **my_dict}
print('The merged dictionary is: ', merged_dict)
import copy
deep_copy = copy.deepcopy(book)
deep_copy['publishing_year'] = '2023'
print(book)
print(deep_copy)
colors_set = {'red', 'green', 'blue'}
print(colors_set)
colors_set.add('yellow')
print(colors_set)
colors_set.discard('red')
print(colors_set)
animals_set = {'lion', 'tiger', 'zebra'}
print(animals_set)
union_set = colors_set | animals_set
print(union_set)
intersection_set = colors_set & animals_set
print(intersection_set)
difference_set = colors_set.difference(animals_set)
print(difference_set)
subset = {'red', 'green'}
colors_set = {'red', 'green', 'blue'}
subset_check = subset.issubset(colors_set)
print(subset_check)
my_list = list(colors_set)
print(my_list)
my_set = set(my_list)
print(my_set)
set_1 = {x for x in range(1,16) if x%3 == 0}
print(set_1)
student_tuple = ('Wasiq', 'Umar', 'Ali', 'Ahmed', 'Yasir')
print(student_tuple)
third_student = student_tuple[2]
print(third_student)
index = student_tuple.index('Yasir')
print(index)
student_list = list(student_tuple)
print(student_list)
my_tuple = tuple(student_list)
print(my_tuple)
tuple_1 = ('x','y','z')
a,b,c = tuple_1
print(a,b,c)
student_dict = {'stu 1': {'age':16, 'grade': 'C'},
'stu 2': {'age': 18, 'grade': 'B'},
'stu 3': {'age':17, 'grade': 'A'}}
print(student_dict)
student_name = input('Enter the name of student whose age you want to find: ')
student_age = student_dict[student_name]['age']
print(f"{student_name}'s age is {student_age}")
student_dict['stu 1']['grade'] = 'A'
print(student_dict)
for student_name, student_info in student_dict.items():
    print(f"Student Name:{student_name}")
    print(f"Student Age: {student_info['age']}")
    print(f"Student Grade:{student_info['grade']}")
    