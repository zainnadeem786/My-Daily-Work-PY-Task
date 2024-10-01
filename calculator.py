import tkinter as tk
from tkinter import font as tkfont

class ColorfulCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Colorful Calculator")
        master.configure(bg='#2C3E50')

        self.display = tk.Entry(master, width=20, font=('Arial', 24), justify='right', bg='#ECF0F1')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

        self.create_buttons()

        for i in range(4):
            master.grid_columnconfigure(i, weight=1)
        for i in range(6):
            master.grid_rowconfigure(i, weight=1)

    def create_buttons(self):
        button_params = [
            ('7', 1, 0, '#3498DB'), ('8', 1, 1, '#3498DB'), ('9', 1, 2, '#3498DB'), ('/', 1, 3, '#E74C3C'),
            ('4', 2, 0, '#3498DB'), ('5', 2, 1, '#3498DB'), ('6', 2, 2, '#3498DB'), ('*', 2, 3, '#E74C3C'),
            ('1', 3, 0, '#3498DB'), ('2', 3, 1, '#3498DB'), ('3', 3, 2, '#3498DB'), ('-', 3, 3, '#E74C3C'),
            ('0', 4, 0, '#3498DB'), ('.', 4, 1, '#3498DB'), ('C', 4, 2, '#E67E22'), ('+', 4, 3, '#E74C3C'),
            ('=', 5, 0, '#2ECC71')
        ]

        for (text, row, col, color) in button_params:
            button = tk.Button(self.master, text=text, font=('Arial', 18), bg=color, fg='white',
                               command=lambda x=text: self.click(x))
            button.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
            if text == '=':
                button.grid(columnspan=4)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, key)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ColorfulCalculator(root)
    root.mainloop()