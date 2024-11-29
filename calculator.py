import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x500")
        self.configure(bg="grey")
        self.equation = ""
        self.entry = tk.Entry(self, font=("Helvetica", 24), borderwidth=5, relief="sunken")
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]

        row, col = 1, 0
        for button in buttons:
            if button == '=':
                tk.Button(self, text=button, font=("Helvetica", 18), command=self.calculate).grid(row=row, column=col, columnspan=2, sticky="nsew")
                col += 1 
            else:
                tk.Button(self, text=button, font=("Helvetica", 18), command=lambda b=button: self.update_equation(b)).grid(row=row, column=col, sticky="nsew")
            
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def update_equation(self, char):
        self.equation += str(char)
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.equation)

    def calculate(self):
        try:
            result = str(eval(self.equation))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
            self.equation = result
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            self.equation = ""

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
