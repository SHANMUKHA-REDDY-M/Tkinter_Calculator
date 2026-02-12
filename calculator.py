import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x400")
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
        for j in range(4):
            button_frame.columnconfigure(j, weight=1)

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        for text, row, col in buttons:
            if text == "=":
                command = self.calculate
            else:
                command = lambda value=text: self.append_value(value)

            button = tk.Button(
                button_frame,
                text=text,
                font=("Arial", 16),
                command=command
            )

            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        clear_button = tk.Button(
            button_frame,
            text="C",
            font=("Arial", 16),
            command=self.clear
        )
        clear_button.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

    def append_value(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)

    def calculate(self):
        try:
            result = eval(self.expression, {"__builtins__": None}, {})
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
