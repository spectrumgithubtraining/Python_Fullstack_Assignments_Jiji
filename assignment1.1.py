 #1. Write a Program to following Patterns

# (a)*
#    *  *
#    *  *  *
#    *  *  *  *
#    *  *  *  *  *
# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")


#(b) 1
    # 2  3
    # 4  5  6
    # 7  8  9  
    # Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of numbers
# def contnum(n):
	
	# initializing starting number
	# num = 1

	# outer loop to handle number of rows
	# for i in range(0, n):
	
		# not re assigning num
		# num = 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		# for j in range(0, i+1):
		
			# printing number
			# print(num, end=" ")
		
			# incrementing number at each column
			# num = num + 1
	
		# ending line after each row
		# print("\r")

# n = 4

# sending 5 as argument
# calling Function
# contnum(n)



# (c) A
#     A  B
#     A  B  C
#     A  B  C  D
n = 4
alph = 65
for i in range(0, n):
	print(" " * (n-i), end=" ")
	for j in range(0, i+1):
		print(chr(alph), end=" ")
		alph += 1
	alph = 65
	print()

#     A
    # B  C
    # D  E  F
    # G  H  I  J
    # ASCII number of 'A'
ascii_number = 65
rows = 4
for i in range(0, rows):
    for j in range(0, i + 1):
        character = chr(ascii_number)
        print(character, end=' ')
        ascii_number += 1
    print(" ")

#e) 2
    # 4   6
    # 8   10  12
    # 14  16  18  20


rows = 4  # You can change the number of rows here
current_number = 2

# Outer loop for the number of rows
for i in range(rows):
    # Inner loop for each number in the current row
    for j in range(i + 1):
        print(current_number, end=" ")
        current_number += 2
    print()  # Move to the next line after printing the row



print("Print equilateral triangle Pyramid using asterisk symbol ")
# printing full Triangle pyramid using stars
size = 4
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("# ", end=' ')
    print(" ")

    