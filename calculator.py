import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create entry field for user input
        self.entry_field = tk.Entry(master, width=20)
        self.entry_field.grid(row=0, column=0, columnspan=4)

        # Create number buttons
        self.button_7 = tk.Button(master, text="7", command=lambda: self.append_to_entry("7"))
        self.button_7.grid(row=1, column=0)
        self.button_8 = tk.Button(master, text="8", command=lambda: self.append_to_entry("8"))
        self.button_8.grid(row=1, column=1)
        self.button_9 = tk.Button(master, text="9", command=lambda: self.append_to_entry("9"))
        self.button_9.grid(row=1, column=2)
        self.button_divide = tk.Button(master, text="/", command=lambda: self.append_to_entry("/"))
        self.button_divide.grid(row=1, column=3)

        self.button_4 = tk.Button(master, text="4", command=lambda: self.append_to_entry("4"))
        self.button_4.grid(row=2, column=0)
        self.button_5 = tk.Button(master, text="5", command=lambda: self.append_to_entry("5"))
        self.button_5.grid(row=2, column=1)
        self.button_6 = tk.Button(master, text="6", command=lambda: self.append_to_entry("6"))
        self.button_6.grid(row=2, column=2)
        self.button_multiply = tk.Button(master, text="*", command=lambda: self.append_to_entry("*"))
        self.button_multiply.grid(row=2, column=3)

        self.button_1 = tk.Button(master, text="1", command=lambda: self.append_to_entry("1"))
        self.button_1.grid(row=3, column=0)
        self.button_2 = tk.Button(master, text="2", command=lambda: self.append_to_entry("2"))
        self.button_2.grid(row=3, column=1)
        self.button_3 = tk.Button(master, text="3", command=lambda: self.append_to_entry("3"))
        self.button_3.grid(row=3, column=2)
        self.button_subtract = tk.Button(master, text="-", command=lambda: self.append_to_entry("-"))
        self.button_subtract.grid(row=3, column=3)

        self.button_0 = tk.Button(master, text="0", command=lambda: self.append_to_entry("0"))
        self.button_0.grid(row=4, column=0)
        self.button_decimal = tk.Button(master, text=".", command=lambda: self.append_to_entry("."))
        self.button_decimal.grid(row=4, column=1)
        self.button_equals = tk.Button(master, text="=", command=self.calculate)
        self.button_equals.grid(row=4, column=2)
        self.button_add = tk.Button(master, text="+", command=lambda: self.append_to_entry("+"))
        self.button_add.grid(row=4, column=3)

    def append_to_entry(self, text):
        self.entry_field.insert(tk.END, text)

    def calculate(self):
        try:
            result = eval(self.entry_field.get())
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, result)
        except Exception as e:
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, "Error")

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()

