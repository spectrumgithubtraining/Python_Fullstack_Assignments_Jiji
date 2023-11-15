#1. Write a program to create a new file and write data to it ?
# import io

# with open("data.txt", "w") as f:
#     f.write("This is Spectrum softech solutions")
#2. Write a program to read data from a file ? (using read() and readline())?
f = open("sample.txt", "r")
print(f.read(3)) 

f = open("sample.txt")
#open a file and read
f = open("sample.txt", "r")
print(f.read()) 

f = open("sample.txt", "r")
print(f.readline())

# 3. Write a program to  solve Quadratic Equation ?
import math

# Input coefficients a, b, and c from the user
a = float(input("Enter the coefficient 'a': "))
b = float(input("Enter the coefficient 'b': "))
c = float(input("Enter the coefficient 'c': "))

# Calculate the discriminant (the value inside the square root)
discriminant = b**2 - 4*a*c

# Check if the discriminant is positive, zero, or negative
if discriminant > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Two real roots: {root1} and {root2}")
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (2*a)
    print(f"One real root: {root}")
else:
    # Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    root1 = complex(real_part, imaginary_part)
    root2 = complex(real_part, -imaginary_part)
    print(f"Complex roots: {root1} and {root2}")

#4. Write a program to perform read and write operation on a CSV File ?
import csv
with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
#write
with open('data.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Name', 'Age', 'City'])
    csvwriter.writerow(['Alice', 25, 'New York'])
    csvwriter.writerow(['Bob', 30, 'Los Angeles'])
 
#5. Write a program to write JSON data to a file ?
# Open the file in write mode to write JSON data to it
import json
with open("json.txt", "w") as file_obj:
    x = [1, 'simple', 'list']
    json.dump(x, file_obj)
    file_obj.close()

# Close the file after writing
# Reopen the file in read mode to read the JSON data back
with open("json.txt", "r") as file_obj:
    json_str = file_obj.read()
    x = json.loads(json_str)
    #json file can be converted into readable mode then loads

# Now 'x' contains the parsed JSON data
print(x)

#6. Write a program to append data to an existing file ?
# Append data to an existing file :
file_obj = open("sample.txt","a")

for i in range(1,4):
    file_obj.write("Hai")
file_obj.close()