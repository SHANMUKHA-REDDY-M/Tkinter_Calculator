import tkinter as tk
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("520x450")
        self.root.resizable(True, True)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_display()
        self.create_buttons()

    def create_display(self):
        display_frame = tk.Frame(self.root)
        display_frame.pack(fill="both", padx=10, pady=10)

        self.entry = tk.Entry(
            display_frame,
            textvariable=self.input_text,
            font=("Arial", 20),
            justify="right",
            bd=8,
            relief=tk.RIDGE
        )
        self.entry.pack(fill="both", ipadx=8, ipady=15)

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both", padx=10, pady=5)

        for i in range(6):
            button_frame.rowconfigure(i, weight=1)
        for j in range(6):
            button_frame.columnconfigure(j, weight=1)

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3), ('sin', 0, 4), ('log', 0, 5),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3), ('cos', 1, 4), ('π', 1, 5),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3), ('tan', 2, 4), ('e', 2, 5),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3), ('√', 3, 4), ('^', 3, 5),
            ('(', 4, 4), (')', 4, 5),
        ]

        for text, row, col in buttons:
            if text == "=":
                command = self.calculate
            else:
                command = lambda value=text: self.append_value(value)

            button = tk.Button(
                button_frame,
                text=text,
                font=("Arial", 14),
                command=command
            )

            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        backspace_button = tk.Button(
            button_frame,
            text="⌫",
            font=("Arial", 14),
            command=self.backspace
        )
        backspace_button.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

        clear_button = tk.Button(
            button_frame,
            text="C",
            font=("Arial", 14),
            command=self.clear
        )
        clear_button.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=2, pady=2)

    def append_value(self, value):
        if value == '√':
            self.expression += 'sqrt('
        elif value == 'sin':
            self.expression += 'sin(radians('
        elif value == 'cos':
            self.expression += 'cos(radians('
        elif value == 'tan':
            self.expression += 'tan(radians('
        elif value == 'log':
            self.expression += 'log10('
        elif value == 'π':
            self.expression += 'pi'
        elif value == 'e':
            self.expression += 'e'
        elif value == '^':
            self.expression += '**'
        else:
            self.expression += str(value)

        self.input_text.set(self.expression)

    def backspace(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

    def calculate(self):
        try:
            allowed_names = {
                "sqrt": math.sqrt,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log10": math.log10,
                "radians": math.radians,
                "pi": math.pi,
                "e": math.e,
            }

            result = eval(self.expression, {"__builtins__": None}, allowed_names)
            self.expression = str(result)
            self.input_text.set(self.expression)
        except Exception:
            self.input_text.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.input_text.set("")


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
