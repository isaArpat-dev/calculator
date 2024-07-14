import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Hesap Makinesi")
        
        self.entry = tk.Entry(root, width=20, font=('Arial', 18), bd=8, insertwidth=2, bg="aqua", justify='right')
        self.entry.grid(row=0, column=0, columnspan=5)

        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '←',
            '1', '2', '3', '-', '(',
            '0', '.', '=', '+', ')',
            '±', '%'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            self.create_button(button).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1
        
        self.bind_keys()
        
        # Geliştirici adı etiketi
        self.developer_label = tk.Label(root, text="Bu hesap makinesi İsa Arpat tarafından geliştirilmiştir.", font=('Arial', 10))
        self.developer_label.grid(row=row_val + 1, column=0, columnspan=5)

    def create_button(self, val):
        return tk.Button(self.root, text=val, padx=20, pady=20, font=('Arial', 18), command=lambda: self.click(val))

    def click(self, val):
        current = self.entry.get()
        if val == "=":
            try:
                result = str(eval(current))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Hata")
        elif val == "C":
            self.entry.delete(0, tk.END)
        elif val == "←":
            self.entry.delete(len(current)-1, tk.END)
        elif val == "±":
            if current:
                if current[0] == '-':
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, '-')
        elif val == "%":
            try:
                result = str(eval(current) / 100)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Hata")
        else:
            self.entry.insert(tk.END, val)

    def bind_keys(self):
        self.root.bind('<Return>', lambda event: self.click('='))
        self.root.bind('<BackSpace>', lambda event: self.click('←'))
        for key in '1234567890+-*/().':
            self.root.bind(key, lambda event, char=key: self.click(char))
        self.root.bind('<Escape>', lambda event: self.click('C'))

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
