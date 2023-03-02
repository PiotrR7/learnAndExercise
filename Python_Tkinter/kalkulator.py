import tkinter as tk

root = tk.Tk()
root.geometry('400x480')
root.maxsize(400,480)
root.minsize(400,480)


tk.Label(root, text='text').grid(row=1, column=1)






root.mainloop()