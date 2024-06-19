import requests
import tkinter as tk
import io
from PIL import ImageTk, Image


root = tk.Tk()

root.title('SR Radio channel')
root.geometry('800x600')

API_LINK = 'http://api.sr.se/api/v2/channels'

lbl = tk.Label(root, text='channel id: ')
lbl.grid(column=0, row=0)

txt = tk.Entry(root)
txt.grid(column=1, row=0)

imagelab = tk.Label(root)
imagelab.grid(column=2, row=2)

present = tk.Label(root)
present.grid(column=2, row=3)


def get_tag_data(text, tag):
    """
    Extract the data that is within a tag.
    If more than one tag has the same name, it will take the first one
    """
    list = text.split("\n")
    for row in list:
        if tag in row:
            info = row.strip().replace('<' + tag + '>', '').replace('</' + tag + '>', '')
            return info


def click():
    num = txt.get()
    link = API_LINK + "/" + num
    response = requests.get(link)
    r = response.text
    image_url = get_tag_data(r, 'image')
    # image = requests.get(image_url).content

    img = Image.open(io.BytesIO(requests.get(image_url).content))
    img = ImageTk.PhotoImage(img)

    imagelab.config(image=img)
    imagelab.image = img

    present.config(text=response.text)


btn = tk.Button(root, text = 'Fetch channel', foreground='blue', command=click)
btn.grid(column=1, row=1)

root.mainloop()
