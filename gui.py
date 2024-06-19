import tkinter as tk

root = tk.Tk()

root.title('Our first GUI')
root.geometry('800x600')

lbl = tk.Label(root, text='Hello World')
lbl.grid(column=1, row=0)

counter = 0

def click():
    global counter

    num = int(txt.get())
    if num > 0:
        counter = counter + num
    else:
        counter = counter + 1

    lbl.configure(text = f'Someone has clicked the button {counter} times!!!!')


btn = tk.Button(root, text = 'change text', foreground='blue', command=click)
btn.grid(column=0, row=1)

txt = tk.Entry(root)
txt.grid(column=1, row=1)

root.mainloop()