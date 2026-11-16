import tkinter as tk

root = tk.Tk()
root.title("Professional Calculator")
root.geometry("380x590")
root.resizable(False, False)
root.config(bg="#14141C")  # PRO - Charcoal Black

first_number = None
operator = None
new_number = False

display = tk.StringVar(value="0")
expression = tk.StringVar(value="Ready")

# Header
header = tk.Frame(root, bg="#14141C")
header.pack(fill="x", padx=22, pady=(22, 10))

title = tk.Label(header, text="C A L C U L A T O R", font=("Segoe UI", 16, "bold"), fg="#FFFFFF", bg="#14141C")
title.pack(anchor="w")

subtitle = tk.Label(header, text="SMART  •  SIMPLE  •  PROFESSIONAL", font=("Segoe UI", 8, "bold"), fg="#8A8A9E", bg="#14141C")
subtitle.pack(anchor="w", pady=(5, 0))

# Display
display_frame = tk.Frame(root, bg="#1E1E2A", padx=15, pady=15)
display_frame.pack(fill="x", padx=18, pady=15)

expression_label = tk.Label(display_frame, textvariable=expression, font=("Segoe UI", 11), fg="#8A8A9E", bg="#1E1E2A", anchor="e")
expression_label.pack(fill="x", pady=(0, 12))

screen = tk.Entry(display_frame, textvariable=display, font=("Segoe UI", 34, "bold"), fg="#FFFFFF", bg="#1E1E2A", justify="right", bd=0, state="readonly", readonlybackground="#1E1E2A")
screen.pack(fill="x", ipady=10)

# --- Functions (same logic) ---
def number_click(number):
    global new_number
    if new_number or display.get() == "Error":
        display.set(number); new_number = False
    elif display.get() == "0":
        display.set(number)
    else:
        display.set(display.get() + number)

def decimal_click():
    global new_number
    if new_number or display.get() == "Error":
        display.set("0."); new_number = False
    elif "." not in display.get():
        display.set(display.get() + ".")

def calculate():
    global first_number, operator, new_number
    if first_number is None or operator is None: return
    if display.get() == "Error": return
    second_number = float(display.get())
    expression.set(f"{first_number:g} {operator} {second_number:g}")
    if operator == "+": result = first_number + second_number
    elif operator == "-": result = first_number - second_number
    elif operator == "*": result = first_number * second_number
    elif operator == "/":
        if second_number == 0:
            display.set("Error"); first_number=None; operator=None; new_number=True; return
        result = first_number / second_number
    display.set(f"{result:.10g}")
    first_number=None; operator=None; new_number=True

def operator_click(selected_operator):
    global first_number, operator, new_number
    if display.get() == "Error": return
    if first_number is not None and new_number:
        operator = selected_operator; return
    if first_number is None:
        first_number = float(display.get())
    else:
        calculate(); first_number = float(display.get())
    operator = selected_operator
    expression.set(f"{first_number:g} {operator}")
    new_number = True

def clear():
    global first_number, operator, new_number
    display.set("0"); expression.set("Ready")
    first_number=None; operator=None; new_number=False

def backspace():
    global new_number
    if new_number or display.get() == "Error": return
    current = display.get()
    display.set(current[:-1] if len(current) > 1 else "0")

def percentage():
    global new_number
    if display.get() != "Error":
        display.set(f"{float(display.get())/100:.10g}"); new_number=True

def change_sign():
    global new_number
    if display.get() != "Error":
        display.set(f"{float(display.get())*-1:.10g}"); new_number=False

# --- Buttons ---
button_frame = tk.Frame(root, bg="#14141C")
button_frame.pack(fill="both", expand=True, padx=16, pady=10)

buttons = [
    ["C", "⌫", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["±", "0", ".", "="]
]

# PRO COLOR PALETTE
number_color = "#262633"
special_color = "#3A3A4A"
operator_color = "#F5A623"  # GOLD - Most Professional
clear_color = "#E5484D"
equal_color = "#0EA47A"     # Emerald

for row_index, row in enumerate(buttons):
    for column_index, text_value in enumerate(row):
        if text_value == "C": color, command = clear_color, clear
        elif text_value == "⌫": color, command = special_color, backspace
        elif text_value == "%": color, command = special_color, percentage
        elif text_value == "±": color, command = special_color, change_sign
        elif text_value == "=": color, command = equal_color, calculate
        elif text_value in ["÷", "×", "−", "+"]:
            color = operator_color
            command = lambda op={"÷":"/","×":"*","−":"-","+" : "+"}[text_value]: operator_click(op)
        elif text_value == ".": color, command = number_color, decimal_click
        else: color, command = number_color, lambda value=text_value: number_click(value)

        button = tk.Button(button_frame, text=text_value, font=("Segoe UI", 17, "bold"),
                           bg=color, fg="white", activebackground="#55556A", activeforeground="white",
                           bd=0, relief="flat", cursor="hand2", command=command)
        button.grid(row=row_index, column=column_index, sticky="nsew", padx=5, pady=5, ipadx=2, ipady=13)

        # PRO - Hover Effect
        def on_enter(e, b=button, c=color): b.config(bg="#55556A" if c != operator_color else "#FFB84D")
        def on_leave(e, b=button, c=color): b.config(bg=c)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

for row in range(5): button_frame.rowconfigure(row, weight=1)
for column in range(4): button_frame.columnconfigure(column, weight=1)

# PRO - Keyboard Support
def on_key(event):
    if event.char in "0123456789": number_click(event.char)
    elif event.char in "+-*/": operator_click(event.char)
    elif event.char == ".": decimal_click()
    elif event.keysym == "Return": calculate()
    elif event.keysym == "BackSpace": backspace()
    elif event.keysym == "Escape": clear()

root.bind("<Key>", on_key)

footer = tk.Label(root, text="MY PROFESSIONAL CALCULATOR", font=("Segoe UI", 8, "bold"), fg="#6B6B80", bg="#14141C")
footer.pack(pady=(5, 15))

root.mainloop()