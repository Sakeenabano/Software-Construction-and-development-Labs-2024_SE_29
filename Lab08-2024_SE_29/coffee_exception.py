import tkinter as tk
from tkinter import messagebox


# Custom Exceptions
class TooHotCoffeeCup(Exception):
    pass


class TooColdCoffeeCup(Exception):
    pass


# Main Window
root = tk.Tk()
root.title("Coffee Temperature Checker")
root.geometry("600x520")
root.resizable(False, False)
root.configure(bg="#F1EDFF")


# Colors
BG = "#F1EDFF"
PURPLE = "#563A8A"
DARK = "#30234A"
LAVENDER = "#DED4FF"
WHITE = "#FFFFFF"
BLUE = "#83B9E8"
GREEN = "#3A9D78"


# Main Heading
heading = tk.Label(
    root,
    text="☕ COFFEE TEMPERATURE",
    font=("Arial", 23, "bold"),
    bg=BG,
    fg=PURPLE
)
heading.pack(pady=(30, 5))


subtitle = tk.Label(
    root,
    text="Coffee Quality & Temperature Checker",
    font=("Arial", 11),
    bg=BG,
    fg=DARK
)
subtitle.pack(pady=5)


# Main Card
card = tk.Frame(
    root,
    bg=WHITE,
    padx=35,
    pady=25,
    highlightbackground=LAVENDER,
    highlightthickness=2
)
card.pack(pady=25, padx=45, fill="both")


# Instructions
tk.Label(
    card,
    text="Enter Coffee Temperature",
    font=("Arial", 15, "bold"),
    bg=WHITE,
    fg=PURPLE
).pack(pady=10)


# Temperature Entry
temperature_entry = tk.Entry(
    card,
    font=("Arial", 18),
    justify="center",
    width=15,
    bg="#F5F2FF",
    fg=DARK,
    relief="flat"
)
temperature_entry.pack(ipady=10, pady=12)


tk.Label(
    card,
    text="Temperature Range: 66°C - 84°C",
    font=("Arial", 11, "bold"),
    bg=WHITE,
    fg="#5679B8"
).pack(pady=8)


# Check Function
def check_temperature():

    try:
        temperature = float(temperature_entry.get())

        if temperature >= 85:
            raise TooHotCoffeeCup(
                "Too Hot Coffee Cup Exception!"
            )

        elif temperature <= 65:
            raise TooColdCoffeeCup(
                "Too Cold Coffee Cup Exception!"
            )

        else:
            result_label.config(
                text="✓ Coffee is Served Successfully!",
                fg=GREEN
            )

    except ValueError:
        result_label.config(
            text="Please enter a valid temperature!",
            fg=PURPLE
        )

    except TooHotCoffeeCup as e:
        result_label.config(
            text=str(e),
            fg=PURPLE
        )

    except TooColdCoffeeCup as e:
        result_label.config(
            text=str(e),
            fg="#5679B8"
        )


# Check Button
check_button = tk.Button(
    card,
    text="CHECK TEMPERATURE",
    font=("Arial", 12, "bold"),
    bg=PURPLE,
    fg=WHITE,
    activebackground="#7655B5",
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    command=check_temperature
)
check_button.pack(pady=20, ipadx=20, ipady=10)


# Result Display
result_label = tk.Label(
    card,
    text="Waiting for temperature...",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=DARK,
    wraplength=400
)
result_label.pack(pady=12)


# Footer
footer = tk.Label(
    root,
    text="Coffee Temperature Exception Handling | Lab 08",
    font=("Arial", 9),
    bg=BG,
    fg=PURPLE
)
footer.pack(pady=10)


# Run Application
root.mainloop()