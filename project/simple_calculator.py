import tkinter as tk
root = tk.Tk()
root.title("Basic Calculator")
expression = ""

# Function to update expression
def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)

# Function to evaluate result
def evaluate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Function to clear input
def clear():
    global expression
    expression = ""
    input_text.set("")

# Entry widget
input_text = tk.StringVar()
entry = tk.Entry(root, textvariable=input_text, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, command=evaluate).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, padx=94, pady=20, command=clear).grid(row=row, column=col, columnspan=3)
    else:
        tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: press(t)).grid(row=row, column=col)

# Run the app
root.mainloop()