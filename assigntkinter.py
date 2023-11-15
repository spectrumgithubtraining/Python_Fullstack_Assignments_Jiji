# 1.Program to illustrate Simple Calculator?
# import tkinter as tk

# # Function to perform calculations
# def calculate():
#     try:
#         expression = entry.get()
#         result = eval(expression)
#         entry.delete(0, tk.END)  # Clear the input field
#         entry.insert(tk.END, str(result))  # Display the result
#     except Exception as e:
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, "Error")

# # Create a tkinter window
# window = tk.Tk()
# window.title("Simple Calculator")

# # Create an entry widget for input
# entry = tk.Entry(window, width=30, borderwidth=5)
# entry.grid(row=0, column=0, columnspan=4)

# # Create buttons for digits and operators
# buttons = [
#     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#     ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
# ]

# for (text, row, col) in buttons:
#     button = tk.Button(window, text=text, padx=20, pady=20, command=lambda t=text: entry.insert(tk.END, t))
#     button.grid(row=row, column=col)

# # Create the 'Clear' button
# clear_button = tk.Button(window, text='Clear', padx=20, pady=20, command=lambda: entry.delete(0, tk.END))
# clear_button.grid(row=5, column=0, columnspan=4)

# # Create the 'Calculate' button
# calculate_button = tk.Button(window, text='Calculate', padx=20, pady=20, command=calculate)
# calculate_button.grid(row=6, column=0, columnspan=4)

# Start the tkinter main loop
# window.mainloop()

#2.    Try to configure GUI, that should define a simple function which will print the data entered by the user in the text-area, upon clicking on a button.
# import tkinter as tk

# # Function to print the data entered by the user
# def print_data():
#     user_data = text_area.get("1.0", "end-1c")  # Get the text from the text area
#     print("User data entered:")
#     print(user_data)

# # Create a tkinter window
# window = tk.Tk()
# window.title("Simple GUI Example")

# # Create a label
# label = tk.Label(window, text="Enter some data:")
# label.pack()

# # Create a text area for user input
# text_area = tk.Text(window, height=5, width=30)
# text_area.pack()

# # Create a button to trigger the printing function
# print_button = tk.Button(window, text="Print Data", command=print_data)
# print_button.pack()

# # Start the tkinter main loop
# window.mainloop()

#3.Try to configure Label widget with various options like background red and font   with Times New Roman 18 size.
import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="This is a label")
label.config(bg="red", font=("Times New Roman", 18))
label.pack()
root.mainloop()