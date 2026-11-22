import tkinter as tk
from tkinter import messagebox

# ---------- Custom Exceptions ----------

class LowHemoglobin(Exception):
    pass


class HighHemoglobin(Exception):
    pass


# ---------- Hemoglobin Checking Function ----------

def check_hemoglobin(category, hb):

    normal_ranges = {
        "Men": (14, 18),
        "Women": (12, 16),
        "Children": (11, 16)
    }

    low, high = normal_ranges[category]

    if hb < low:
        raise LowHemoglobin(
            f"Hemoglobin level {hb} g/dL is LOW.\n"
            f"Normal range for {category}: {low}-{high} g/dL"
        )

    elif hb > high:
        raise HighHemoglobin(
            f"Hemoglobin level {hb} g/dL is HIGH.\n"
            f"Normal range for {category}: {low}-{high} g/dL"
        )

    else:
        return (
            f"Hemoglobin level: {hb} g/dL\n"
            f"Status: NORMAL\n"
            f"Normal range: {low}-{high} g/dL"
        )


# ---------- Colour Theme ----------

PURPLE = "#312E81"
CYAN = "#06B6D4"
WHITE = "#FFFFFF"
BACKGROUND = "#EDE9FE"
DARK = "#1E1B4B"
GREEN = "#15803D"
ORANGE = "#C2410C"
RED = "#B91C1C"


# ---------- Main Window ----------

root = tk.Tk()
root.title("Hemoglobin Level Monitor")
root.geometry("440x590")
root.configure(bg=BACKGROUND)
root.resizable(False, False)


# ---------- Header Section ----------

header = tk.Frame(root, bg=PURPLE, height=105)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="HEMOGLOBIN MONITOR",
    font=("Segoe UI", 19, "bold"),
    bg=PURPLE,
    fg=CYAN
).pack(pady=(17, 5))

tk.Label(
    header,
    text="Custom Exception Handling",
    font=("Segoe UI", 10),
    bg=PURPLE,
    fg=WHITE
).pack()


# ---------- Main Input Card ----------

card = tk.Frame(
    root,
    bg=WHITE,
    padx=25,
    pady=20,
    highlightbackground=CYAN,
    highlightthickness=2
)
card.pack(fill="x", padx=25, pady=22)


# ---------- Category Selection ----------

tk.Label(
    card,
    text="Select Your Category",
    font=("Segoe UI", 12, "bold"),
    bg=WHITE,
    fg=PURPLE
).pack(anchor="w")

category = tk.StringVar(value="Women")

options = tk.Frame(card, bg=WHITE)
options.pack(fill="x", pady=12)

tk.Radiobutton(
    options,
    text="Men",
    variable=category,
    value="Men",
    font=("Segoe UI", 10, "bold"),
    bg=WHITE,
    fg="#2563EB",
    selectcolor="#DBEAFE",
    activebackground=WHITE
).pack(side="left", padx=5)

tk.Radiobutton(
    options,
    text="Women",
    variable=category,
    value="Women",
    font=("Segoe UI", 10, "bold"),
    bg=WHITE,
    fg="#DB2777",
    selectcolor="#FCE7F3",
    activebackground=WHITE
).pack(side="left", padx=5)

tk.Radiobutton(
    options,
    text="Children",
    variable=category,
    value="Children",
    font=("Segoe UI", 10, "bold"),
    bg=WHITE,
    fg=GREEN,
    selectcolor="#DCFCE7",
    activebackground=WHITE
).pack(side="left", padx=5)


# ---------- Hemoglobin Input ----------

tk.Label(
    card,
    text="Enter Hb Level (g/dL)",
    font=("Segoe UI", 12, "bold"),
    bg=WHITE,
    fg=PURPLE
).pack(anchor="w", pady=(8, 5))

tk.Label(
    card,
    text="Men: 14-18 | Women: 12-16 | Children: 11-16",
    font=("Segoe UI", 9),
    bg=WHITE,
    fg="#64748B"
).pack(anchor="w", pady=(0, 10))

hb_entry = tk.Entry(
    card,
    font=("Segoe UI", 16),
    justify="center",
    bg="#F8FAFC",
    fg=DARK,
    relief="solid",
    bd=1
)
hb_entry.pack(fill="x", ipady=7)


# ---------- Result Section ----------

result_box = tk.Frame(
    card,
    bg="#E0F2FE",
    padx=12,
    pady=15
)
result_box.pack(fill="x", pady=18)

result_label = tk.Label(
    result_box,
    text="Your result will appear here.",
    font=("Segoe UI", 11, "bold"),
    bg="#E0F2FE",
    fg=PURPLE,
    wraplength=320,
    justify="center"
)
result_label.pack()


# ---------- Check Function ----------

def check_level():

    try:
        hb = float(hb_entry.get())
        selected_category = category.get()

        if hb < 0:
            raise ValueError

        result = check_hemoglobin(selected_category, hb)

        result_box.config(bg="#DCFCE7")
        result_label.config(
            text=result,
            bg="#DCFCE7",
            fg=GREEN
        )

    except LowHemoglobin as error:

        result_box.config(bg="#FFEDD5")
        result_label.config(
            text=str(error),
            bg="#FFEDD5",
            fg=ORANGE
        )

        messagebox.showwarning("Low Hemoglobin", str(error))

    except HighHemoglobin as error:

        result_box.config(bg="#FEE2E2")
        result_label.config(
            text=str(error),
            bg="#FEE2E2",
            fg=RED
        )

        messagebox.showerror("High Hemoglobin", str(error))

    except ValueError:

        result_box.config(bg="#FCE7F3")
        result_label.config(
            text="Please enter a valid positive number.",
            bg="#FCE7F3",
            fg=RED
        )

        messagebox.showwarning(
            "Invalid Input",
            "Please enter a valid hemoglobin value."
        )


# ---------- Reset Function ----------

def reset_form():

    hb_entry.delete(0, tk.END)
    category.set("Women")

    result_box.config(bg="#E0F2FE")
    result_label.config(
        text="Your result will appear here.",
        bg="#E0F2FE",
        fg=PURPLE
    )


# ---------- Action Buttons ----------

tk.Button(
    card,
    text="CHECK Hb LEVEL",
    font=("Segoe UI", 12, "bold"),
    bg=PURPLE,
    fg=WHITE,
    activebackground="#4338CA",
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    command=check_level,
    pady=10
).pack(fill="x", pady=(0, 9))

tk.Button(
    card,
    text="RESET FORM",
    font=("Segoe UI", 11, "bold"),
    bg=CYAN,
    fg=DARK,
    activebackground="#0891B2",
    relief="flat",
    cursor="hand2",
    command=reset_form,
    pady=8
).pack(fill="x")


# ---------- Footer ----------

tk.Label(
    root,
    text="LOW  |  NORMAL  |  HIGH",
    font=("Segoe UI", 11, "bold"),
    bg=BACKGROUND,
    fg=PURPLE
).pack(pady=(2, 5))

tk.Label(
    root,
    text="Custom Exceptions Demonstration",
    font=("Segoe UI", 9),
    bg=BACKGROUND,
    fg="#64748B"
).pack()


root.mainloop()