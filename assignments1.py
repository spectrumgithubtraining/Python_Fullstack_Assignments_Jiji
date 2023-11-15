# 1.Write a program to check whether the entered number is postive or negative

# num=int(input("Enter a number"))
# if num>0:
#     print("number is positive")
# else :
#     print("number is negative")

#2. write a prgm to demonstrate swapping of two variables


# x = 10
# y = 50

# Swapping of two variables
# Using third variable

# swap= x
# x = y
# y = swap

# print("Value of x:", x)
# print("Value of y:", y)



# 3.Write a program to  Determine If Year Is Leap Year

#leap year conditions
#1.year is exactly divided by 4 and 100 and 400
#it is return true leap year otherwise not leap year


# year = 2000

# if (year%400 == 0) or (year%4==0 and year%100!=0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

# year = 2035

# if (year%400 == 0) or (year%4==0 and year%100!=0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")



#4.Write a program check whether the given number is odd or even.

# num=int(input("Enter any number to test whether it is odd or even:"))

# if (num % 2) == 0:
#     print ("The number is even")

# else:
#     print ("The provided number is odd")


# 5.Write a program to print the fibonocci series.

#Fibonacci numbers are the numbers in the following integer sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …….. 
#In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation.

#Fn = Fn-1 + Fn-2

#with seed values : F0 = 0 and F1 = 1.

# n = 10
# num1 = 0
# num2 = 1
# next_number = num2
# count = 1

# while count <= n:
# 	print(next_number, end=" ")
# 	count += 1
# 	num1, num2 = num2, next_number
# 	next_number = num1 + num2
# print()


#6.Write a program to  generate following pyramid or triangle like  given below using for loop.
            # Python 3.x code to demonstrate star pattern

# # downward triangle star pattern
# n = 6

# for i in range(n):
#     # internal loop run for n - i times
#     for j in range(n - i):
#         print('*', end='')
#     print()



#next
# right pascal triangle
# n = 5

# upper triangle
# for i in range(n):
#     for j in range(i + 1):
#         print('*', end="")
#     print()
# # lower triangle
# for i in range(n):
#     for j in range(n - i - 1):
#         print('*', end="")
#     print()


#7. Write a program to print the prime numbers between given interval.
# Python program to display all the prime numbers within an interval

# lower = 500
# upper = 1000

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)


#8.Write a program for Printing Odd numbers between 1 and 50 and calculate the sum of that numbers.
# x = 0

# for i in range(1,50):

#    if(i%2 == 1):

#        print(i)

#        x += i

# print("sum of all odd numbers between 1 and 50 is",x)


#9.9. Write a program to find the factorial of the given number.

                    
# n = int (input ("Enter a number: "))

# factorial = 1

# if n >= 1:
#     for i in range (1, n+1):
#         factorial = factorial *i
#         print ("Factorial of the given number is: ", factorial)

                #OR

                # python program to find factorial of given number

# number = int(input("enter any number"))
#initialize fact to 1
# fact =1

# checking if the given number is negative...
# if number < 0:
#    print("Factorial does not exist of negative numbers")
# if number is zero
# elif number == 0: 
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,number + 1):
#        fact = fact*i
#    print("The factorial of",number,"is",fact)


#10.Write a program to Check if the given string  is Palindrome or not. 
# Python program to check
# if a string is palindrome
# or not

# x = "malayalam"

# w = ""
# for i in x:
# 	w = i + w

# if (x == w):
# 	print("Yes")
# else:
# 	print("No")
#11.  Write a program to find sum of all integers greater than 100 and less than 200 that are divisible by 7.          

 
# lower=int(input("Enter the lower range:"))
# upper=int(input("Enter the upper range:"))
# for i in range (lower,upper+1):
#     if(i%7==0 ):
#         print(i)


#12.Write a program to Display Multiplication Table


# numb = int(input(" Enter a number : "))    

# # using the for loop to generate the multiplication tables     

# print("Table of: ")  

# for i in range(1,11):    

#    print(numb,'x',i,'=',numb*i) 


#13.Write a program to calculate the area and perimeter of a rectangle..        

# Area & Perimeter of Rectangle

# Reading length from user
# length = float(input("Enter length of the rectangle: "))

# # Reading breadth from user
# breadth = float(input("Enter breadth of the rectangle: "))

# # Calculating area
# area = length * breadth

# # Calculating perimeter
# perimeter = 2 * (length + breadth)

# # Displaying results
# print("Area of rectangle = ", area)
# print("Perimeter of rectangle = ", perimeter)

#14.  Write a program to find the sum of n' Natural Numbers.
#Taking user input

# num = int(input('Enter a number:'))

# if num < 0:
#    num = input('Please enter a positive number:')
# else:
#    sum = 0
#    #Loop to iterate till zero
#    while(num > 0):
#        sum += num
#        num -= 1
#    print("The sum of the natural numbers is:", sum)


 #15 Write a program to find whether given no. is Armstrong or not.
# Python program to check if the number is an Armstrong number or not


# num = int(input("Enter a number: "))

# # initialize sum
# sum = 0

# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10

# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
      


#16.Write a program to find the largest among 3 numbers.

# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
# num1 = 10
# num2 = 14
# num3 = 12

# uncomment following lines to take three numbers from user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))

# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3

# print("The largest number is", largest)


#17.Write a program to remove all punctuations from given string.
# define punctuation
# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")
# no_punct = ""
# for char in my_str:
#    if char not in punctuations:
#        no_punct = no_punct + char

# display the unpunctuated string
# print(no_punct)



#18. Write a program to  Display Triangle as follow : 
# rows = int(input("Enter the number of rows:"))  
# Outer loop will print number of rows  
# for i in range(rows+1):
    # Inner loop will print the value of i after each iteration  
    # for j in range(i):
        # print(i, end=" ")
        # line after each row to display pattern correctly 
    # print(" ")   



#19.Write a program to count the no:of each vowel in a given string.
# string=input("Enter string:")
# vowels=0
# for i in string:
#       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#             vowels=vowels+1
# print("Number of vowels are:")
# print(vowels)



# 20.Program to perform Addition,Subtraction,Multiplication and division on Complex-No's.
# print("Enter First Number: ")
# numOne = int(input())
# print("Enter Second Number: ")
# numTwo = int(input())
# res = numOne+numTwo
# print("\nAddition Result = ", res)
# res = numOne-numTwo
# print("Subtraction Result = ", res)
# res = numOne*numTwo
# print("Multiplication Result = ", res)
# res = numOne/numTwo
# print("Division Result = ", res)


#21. Find Value of the following expressions

# num_1 = 10

# num_2 = 11

 

# num_1 % num_2

# res1=num_1 % num_2
# print(res1)

# num_1 - num_2
# res2=num_1 - num_2
# print(res2)
# num_1 * num_2
# res3=num_1 * num_2
# print(res3)

#22. Find the results of the following expressions (True or False)

    # num_1=7

    # num_2 = 6

    # res1=num_1 < num_2
    # print(res1)

    # res2=num_1 > num_2
    # print(res2)
    # res3=num_1 <= num_2
    # print(res3)
    # res4=num_1 >= num_2
    # print(res4)

    # res5=num_1=num_2#ITS NOT COMPARISON ITS ASSIGNMENT OPERATION SO VALUE OF NUM_2 IS ASSIGN TO NUM_1
    # print(res5)

#23. Find the results of the following expressions (True or False)

# num_1=3

# num_2 = 4

 

# res1=(num_1 < num_2) and (num_1 != num_2)
# print(res1)
# res2=(num_2 >= num_1) or (num_1 > num_2)
# print(res2)
# res3=not (num_1 == num_2)
# print(res3)

#24.  Output of the following while loop

# i=1

# while (i<6):
#     i = i +1
#     print(i)

 #answer b

# Options

# a. 12345

# b. 23456

# c. 2345


#25 Select the correct option

 #answer A

customer_num =5

invoice_num =1212

print("Invoice No(s):")

while(customer_num >0):

     print("INV -", invoice_num)

     invoice_num = invoice_num +3

     customer_num = customer_num -1


#26.Write a python function to add ‘python’ at the end of a given string and return the new string. If the given string already ends with ‘python’ then add ‘java’. If the length of the given string is less than 5, then add ‘php’.
# def add_string(str1):
#   length = len(str1)

#   if length > 2:
#     if str1[-3:] == 'ing':
#       str1 += 'ly'
#     else:
#       str1 += 'ing'

#   return str1
# print(add_string('ab'))
# print(add_string('abc'))
# print(add_string('string'))

#.27.Write a python function which accepts a string containing a pattern of braces and returns true if the pattern of braces is correct. Otherwise it returns false.

# The string of braces is correct if it satisfies the following conditions:
# a. Number of opening and closing braces are equal.
# b. Pattern should not start with closing braces and end with opening brace.

# def bracket_pattern(input_str):
    #Remove pass and write your code here
#     cou=0
#     c=0
#     if(input_str.startswith("(")and input_str.endswith(")")):
#         for i in input_str:
#             if(i=="("):
#                 cou+=1
#             else:
#                 c+=1
#         if(c==cou and c+cou==len(input_str)):
            
#             return True
#     return False

    
# input_str="(())"
# print(bracket_pattern(input_str))

#28. Given two numbers, write a python function which returns true if first number is a seed of second number. Otherwise it returns false.
# def ProdOfDigits(i):
#     if i < 10:
#         return i
#     prod=1
#     while(i!=0):
#         prod=prod*(i%10)
#         i=i//10
#     return prod


# n=4977
# for i in range(1 , n+1):
#     if n%i==0:
#         if ProdOfDigits(i)*i==n:
#             print(i)   