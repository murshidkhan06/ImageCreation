import tkinter as tk
from tkinter import filedialog
import pandas as pd


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.browse_button = tk.Button(self, text="Browse", command=self.browse)
        self.browse_button.pack()
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def browse(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.result_label.config(text="File selected: " + self.file_path)
            self.read_csv()

    def read_csv(self):
        try:
            self.df = pd.read_csv(self.file_path)
            self.result_label.config(text="CSV file successfully read.")
            print(self.df.head(10))
        except:
            self.result_label.config(text="Error reading CSV file.")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
