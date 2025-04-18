import tkinter as tk
from tkinter import messagebox


# root = tk.Tk()

# label = tk.Label(root, text="Hello World!", font=('Arial', 18))
# label.pack(padx=20, pady=20)

# textbox = tk.Text(root, height=3, font=('Arial', 16))
# textbox.pack(padx=10, pady=10)

# buttonFrame = tk.Frame(root)
# buttonFrame.columnconfigure(0, weight=1)
# buttonFrame.columnconfigure(1, weight=1)
# buttonFrame.columnconfigure(2, weight=1)

# btn1 = tk.Button(buttonFrame, text="1", font=('Arial', 18))
# btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

# btn2 = tk.Button(buttonFrame, text="2", font=('Arial', 18))
# btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

# btn3 = tk.Button(buttonFrame, text="3", font=('Arial', 18))
# btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

# btn4 = tk.Button(buttonFrame, text="4", font=('Arial', 18))
# btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

# btn5 = tk.Button(buttonFrame, text="5", font=('Arial', 18))
# btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

# btn6 = tk.Button(buttonFrame, text="6", font=('Arial', 18))
# btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

# buttonFrame.pack(fill='x')

# root.geometry("500x500")
# root.title("My First GUI")

# label = tk.Label(root, text="Hello World!", font=('Arial', 18))
# label.pack(padx=20, pady=20)

# textbox = tk.Text(root, height=3, font=('Arial', 16))
# textbox.pack(padx=10, pady=10)

# button = tk.Button(root, text="Click Me!", font=('Arial', 18))
# button.pack(padx=10, pady=10)

# root.mainloop()

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)
        
        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
    

MyGUI()