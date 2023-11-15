#1. Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)

#2. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
sentence = "i love PYTHON"

# converts first character to uppercase and others to lowercase
capitalized_string = sentence.capitalize()

print(capitalized_string)

# Output: I love python

#3.Write a program to implement all built-in methods of list.
# Create an initial list
my_list = [1, 2, 3, 4, 5]

# Append an element to the list
my_list.append(6)
print("Append:", my_list)

# Extend the list with another list
my_list.extend([7, 8, 9])
print("Extend:", my_list)

# Insert an element at a specific index
my_list.insert(3, 10)
print("Insert:", my_list)

# Remove the first occurrence of an element
my_list.remove(4)
print("Remove:", my_list)

# Pop an element by index (default is the last element)
popped_element = my_list.pop(2)
print("Pop:", my_list)
print("Popped Element:", popped_element)

# Find the index of an element
index = my_list.index(5)
print("Index:", index)

# Count the occurrences of an element
count = my_list.count(3)
print("Count:", count)

# Sort the list in-place
my_list.sort()
print("Sort (in-place):", my_list)

# Reverse the list in-place
my_list.reverse()
print("Reverse (in-place):", my_list)

# Make a shallow copy of the list
copy_list = my_list.copy()
print("Copy:", copy_list)

# Clear all elements from the list
my_list.clear()
print("Clear:", my_list)

#4. Write a program to read dictionary values through keyboard and merge two dictionaries.
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)
#5.Write a program to demonstrate all built-in methods of dictionary.
# creating a dictionary
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}

# printing the dictionary
print(country_capitals)
#6. Write a program to find the sum of all the elements in a list.
# Python program to find sum of elements in list

total = 0

# creating a list
list1 = [11, 5, 17, 18, 23]

# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
	total = total + list1[ele]

# printing total value
print("Sum of all elements in given list: ", total)

#7. With a given integral number n, write a program to generate a dictionary 
#that contains(i,i*i) such that i is an integral number between 1 and n. And then 
#the program should print the dictionary.
n=int(input("Input a number "))
d = dict()

for i in range(1,n+1):
    d[i]=i*i

print(d)

#8. Write a program that accepts a sentence and calculate the number of letters & digits.
# str =input("Input a string: ")

# d=l=0

# for c in str:

#     if c.isdigit():

#         d=d+1

#     elif c.isalpha():

#         l=l+1

#     else:

#         pass

# print("Letters", l)

# print("Digits", d)

#9. Write a program to implement filter(), map() and reduce() .
# Example using map()
numbers = [1, 2, 3, 4, 5]
#MAP
# Define a function to square a number
def square(x):
    return x ** 2

squared_numbers = list(map(square, numbers))
print(squared_numbers)

#FILTER()
# Example using filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Define a function to filter even numbers
def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)

#REDUCE()
# Example using reduce()
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Define a function to calculate the product of two numbers
def multiply(x, y):
    return x * y

product = reduce(multiply, numbers)
print(product)
#10. Write a program to implement List Comprehension .

h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

#11. Write a program to implement Dictionary Comprehension .


square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)

#12.Write a program to find the largest and smallest element from a list.
# numbers = [9, 34, 11, -4, 27]

# # find the maximum number
# max_number = max(numbers)
# print(max_number)

# # Output: 34

# numbers = [9, 34, 11, -4, 27]

# # find the maximum number
# min_number = min(numbers)
# print(min_number)

# Output: -4

#13. Write a Python program to print the numbers of a specified list after removing even numbers from it. 
# Python program to print Even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 == 0:
		print(num, end=" ")


#14. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30
# Generate a list of squares of numbers from 1 to 30
squares_list = [i * i for i in range(1, 31)]

# Extract the first 5 elements
first_5 = squares_list[:5]

# Extract the last 5 elements
last_5 = squares_list[-5:]

# Print the first 5 elements
print("First 5 elements:", first_5)

# Print the last 5 elements
print("Last 5 elements:", last_5)


#15. Write a Python program to insert a given string at the beginning of all items in a list. 

# Define a list of items
my_list = ["apple", "banana", "cherry", "date"]

# Define the string to insert at the beginning
prefix = "fruit_"

# Use a list comprehension to insert the string at the beginning of each item
modified_list = [prefix + item for item in my_list]

# Print the modified list
print(modified_list)


#16.  Write a Python program to iterate over two lists simultaneously.
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

# Iterate over both lists simultaneously using zip
for item1, item2 in zip(list1, list2):#zip() function to combine elements from both lists.
    print(item1, item2)

# 17 Write a Python program to add a key to a dictionary.
# Define an initial dictionary
my_dict = {'name': 'Alice', 'age': 30}

# Add a new key-value pair to the dictionary
my_dict['city'] = 'New York'

#18 Print the updated dictionary
print(my_dict)

# Write a Python script to concatenate following dictionaries to create a new one.

#Sample Dictionary :
              #dic1={1:10, 2:20}


              #dic2={3:30, 4:40}
              #dic3={5:50,6:60} 

              # Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate the dictionaries into a new one
concatenated_dict = {**dic1, **dic2, **dic3}

# Print the concatenated dictionary
print(concatenated_dict)

#19. Write a Python program to iterate over dictionaries using for loops.
#iterating over keys
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

for key in my_dict:
    print(key)
#iterating over values
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

for value in my_dict.values():
    print(value)
#. Iterating over key-value pairs (items):
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

for key, value in my_dict.items():
    print(key, value)


#20.Write a Python program to sum all the items in a dictionary.
# Sample dictionary
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# Initialize a variable to store the sum
total_sum = 0

# Iterate through the values in the dictionary and add them to the total sum
for value in my_dict.values():
    total_sum += value

# Print the total sum
print("The sum of all items in the dictionary is:", total_sum)


#Create a dictionary to hold information about pets. Each key is an animal's name, and each value is the kind of animal.Eg : {'Dog':'Willie'}

    # Put at least 3 key-value pairs in your dictionary.
    # Use a for loop to print out a series of statements such as "Willie is a dog."

 

## Define a dictionary with pet information
pets = {
    'Willie': 'Dog',
    'Mittens': 'Cat',
    'Nemo': 'Fish'
}

# Iterate through the dictionary and print statements
for pet_name, pet_type in pets.items():
    print(f"{pet_name} is a {pet_type}.")

# 22. Write a python function to create and return a new dictionary from the given dictionary (subject: mark).

# Create a new dictionary with subject having marks more than 50.
def filter_passed_subjects(original_dict):
    passed_subjects = {}  # Initialize an empty dictionary for passed subjects

    # Iterate through the original dictionary
    for subject, mark in original_dict.items():
        if mark > 50:
            passed_subjects[subject] = mark  # Add subject and mark to the new dictionary

    return passed_subjects

# Sample dictionary of subjects and marks
marks_dict = {'Math': 85, 'Science': 45, 'History': 60, 'English': 30}

# Call the function to get a new dictionary with passed subjects
passed_subjects_dict = filter_passed_subjects(marks_dict)

# Print the new dictionary
print(passed_subjects_dict)


#23 Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.

#It should return a dictionary in which the key should be letter count and value should be digit count. Ignore the spaces or any other special character in the sentence.
s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

#24. 24. Write a Python function which generates and returns a dictionary where the keys are numbers between 1 and n (both inclusive) and the values are square of keys.


d=dict()
n=20
for x in range(1,n):
    d[x]=x**2
print(d)  
