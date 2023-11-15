##1. Write a program to define a function that can accept an integer number as  
#  input and print the "It is an even number" if the number is even,
# otherwise print "It is odd".
def check_even_or_odd(number):
    if number % 2 == 0:
        print("It is an even number")
    else:
        print("It is odd")
number= int(input("Enter an integer: "))
print(check_even_or_odd(number))
# Input from the user
# try:
#     num = int(input("Enter an integer: "))
#     check_even_or_odd(num)
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")

#2. Write a program to define a function which can print a 
# dictionary where the keys are numbers between 1 and 20
#  (both included) and the values are square of keys.
# def generate_square_dictionary():
#     square_dict = {}  # Create an empty dictionary to store the key-value pairs
#     for num in range(1, 21):  # Iterate through numbers from 1 to 20 (inclusive)
#         square_dict[num] = num ** 2  # Calculate the square and add it to the dictionary
#     return square_dict  # Return the dictionary

# # Call the function to generate the dictionary
# result_dict = generate_square_dictionary()

# # Print the resulting dictionary
# for key, value in result_dict.items():
#     print(f"Key: {key}, Value: {value}")

#3. Write a program to take a string as input and return a string 
#with vowels removed.(implement List Comprehesion)
# string = "PrepInsta"

# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# result = ""

# for i in range(len(string)):
#     if string[i] not in vowels:
#         result = result + string[i]

# print("\nAfter removing Vowels: ", result)
#4. Write a program to display Powers of 2  
#using Anonymous functions?(lambda,map).
# Define the range of powers
# n = 10  # You can change this to the desired number of powers

# # Use lambda and map to calculate and display powers of 2
# powers_of_2 = map(lambda x: 2 ** x, range(n))

# Display the powers of 2
# print("Powers of 2:")
# for power in powers_of_2:
#     print(power)

 #Write a program to implement bubble-sort algorithm
 # Optimized Bubble sort in Python

def bubbleSort(array):
    
  # loop through each element of array
  for i in range(len(array)):
        
    # keep track of swapping
    swapped = False
    
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping occurs if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

        swapped = True
          
    # no swapping means the array is already sorted
    # so no need for further comparison
    if not swapped:
      break
data = [-2, 45, 0, 11, -9]

print(bubbleSort(data))

print('Sorted Array in Ascending Order:')
print(data)

#6. Write a program to implement binary-search algorithm
# Sorted array
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Target number to search for
target = 7

# Binary search function
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Element not found in the array

# Perform binary search
result = binary_search(arr, target)

# Check the result
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")

#7. Write a program to take two list of same length as input and return a dictionary with one as keys and other as values.
# Function to create a dictionary from two lists
def create_dict(keys, values):
    # Check if both lists have the same length
    if len(keys) != len(values):
        return None  # Lists must have the same length to create a dictionary

    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]

    return result_dict

# Input lists
keys_list = ["name", "age", "city"]
values_list = ["Alice", 25, "New York"]

# Create the dictionary
result = create_dict(keys_list, values_list)

# Check if the dictionary was successfully created
if result:
    print(result)
else:
    print("Lists must have the same length to create a dictionary.")

## Function to print Fibonacci series using recursion
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

# Number of Fibonacci numbers to generate
n = 10

# Call the function and print the result
fib_series = fibonacci(n)
print(f"Fibonacci series of length {n}:")
print(fib_series)

#
# Function for nth fibonacci
# number
FibArray = [0, 1]

def fibonacci(n):

	# Check is n is less
	# than 0
	if n < 0:
		print("Incorrect input")
		
	# Check is n is less
	# than len(FibArray)
	elif n < len(FibArray):
		return FibArray[n]
	else:	
		FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
		return FibArray[n]

# Driver Program
print(fibonacci(9))

#

#9. Write a program to find the factorial of a number using recursion.
# Python 3 program to find
# factorial of given number
def factorial(n):
	
	# Checking the number
	# is 1 or 0 then
	# return 1
	# other wise return
	# factorial
	if (n==1 or n==0):
		
		return 1
	
	else:
		
		return (n * factorial(n - 1))

# Driver Code
num = 5;
print("number : ",num)
print("Factorial : ",factorial(num))

#10. Program to implement concept of decorator to calculate the time needed 
#to execute one or more function in a program.
import time

# Decorator function to calculate and print the execution time of a function
def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of '{func.__name__}': {execution_time} seconds")
        return result
    return wrapper

# Example functions to demonstrate the decorator
@calculate_execution_time
def slow_function():
    time.sleep(2)

@calculate_execution_time
def fast_function():
    time.sleep(1)

if __name__ == "__main__":
    slow_function()
    fast_function()

#11. Write a program using generator to print the numbers which can be
# divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
#(implement generator). using if else
def divisible_by_5_and_7_generator(n):
    for num in range(n + 1):
        if num % 5 == 0 and num % 7 == 0:
            yield num

n = int(input("Enter a value for n: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    result = divisible_by_5_and_7_generator(n)
    divisible_numbers = list(result)

    if not divisible_numbers:
        print("There are no numbers divisible by 5 and 7 between 0 and", n)
    else:
        print("Numbers divisible by 5 and 7 between 0 and", n, "are:")
        print(", ".join(map(str, divisible_numbers)))


#12 Write a program using generator to print the even numbers between 0 and n in comma separated form while
# n is input by console.(implement generator)

def even_numbers_generator(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

n = int(input("Enter a value for n: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    result = even_numbers_generator(n)
    even_numbers = list(result)

    if not even_numbers:
        print("There are no even numbers between 0 and", n)
    else:
        print("Even numbers between 0 and", n, "are:")
        print(", ".join(map(str, even_numbers)))


#13. Write a program to implement Insertion-Sort algorithm in python.
def insertion_sort(arr):#This line defines a function called insertion_sort that takes an input list arr as its argument. This function will sort the list using the Insertion Sort algorithm.
    for i in range(1, len(arr)):
        # Set key:
        key = arr[i]#    Here, you're defining a variable key and setting it equal to the value of the current element arr[i]. This is the element that will be moved to its correct position within the sorted portion of the list.
#Inside the while loop, you're swapping the elements. arr[j + 1] is assigned the value of arr[j], effectively shifting the larger element one position to the right.
#Then, arr[j] is assigned the value of the key, inserting it into the correct position within the sorted portion of the list


        j = i - 1#You're initializing a variable j to i - 1. j represents the index of the last element in the sorted portion of the list.
        while j >= 0 and arr[j] > key:#This line starts a while loop that continues as long as j is greater than or equal to 0 (indicating we haven't reached the beginning of the list) and the element at index j is greater than the key.
            # Swap:
            arr[j + 1] = arr[j]
            arr[j] = key
            
            # Decrement 'j':
            j -= 1#After the swap, you decrement j to continue checking and swapping elements until the key is in its correct sorted position.

    return arr


array = [5, 2, 12, 12, 1]
print("Original array: %s" % array)
print("Sorted array: %s" % insertion_sort(array))

#14. Program to implement Linear-Search Algorithm.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if the target is not found in the list

# Example usage
if __name__ == "__main__":
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    target_element = 4

    result = linear_search(my_list, target_element)

    if result != -1:
        print(f"Element {target_element} found at index {result}")
    else:
        print(f"Element {target_element} not found in the list")
#15. Program to implement Selection-Sort Algorithm.
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
if __name__ == "__main__":
    my_list = [64, 25, 12, 22, 11]
    print("Unsorted list:", my_list)

    selection_sort(my_list)

    print("Sorted list:", my_list)

    #16.Write a Python program to find the second smallest number in a list using function.
def find_second_smallest(arr):
    if len(arr) < 2:
        return "List should contain at least two elements"
    
    smallest = float('inf')  # Initialize the smallest to positive infinity
    second_smallest = float('inf')  # Initialize the second smallest to positive infinity
    
    for num in arr:
        if num < smallest:
            second_smallest = smallest  # Update second_smallest to the previous smallest
            smallest = num  # Update smallest to the new smallest
        elif num < second_smallest and num != smallest:
            second_smallest = num  # Update second_smallest if a smaller non-duplicate number is found
    
    if second_smallest == float('inf'):
        return "There is no second smallest element in the list"
    
    return second_smallest

# Example usage
if __name__ == "__main__":
    my_list = [64, 25, 12, 22, 11]
    result = find_second_smallest(my_list)
    print("Second smallest number in the list:", result)
