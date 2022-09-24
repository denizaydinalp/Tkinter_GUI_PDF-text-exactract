
"""
Very basic app for PDF text extraction. It can open a pfd fil end extracts the data.
"""

import tkinter
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import time

print("Initialized... " + time.asctime())


root = tkinter.Tk()
root.title("Lets roll... ")
root.geometry("600x700+2250+200")
canvas = tkinter.Canvas(root, width=600, height=700)
canvas.grid(columnspan=3, rowspan=20)


# Logo
logo = Image.open("logo.png")  # Open image file.
logo = ImageTk.PhotoImage(logo)  # Converts data to tkinter image.
logo_label = tkinter.Label(image=logo)
logo_label.grid(row=0, column=1)


# Instructions
instructions = tkinter.Label(root, text="Select a PDF file. ", font="Raleway")
instructions.grid(row=1, column=1)


def sys_browse():
    print("Browse button clicked ")
    browse_button.config(text="Loading... ")
    data = askopenfile(parent=root,
                       mode="rb",
                       title="Choose a file",
                       filetypes=[("Pdf file", "*.pdf")])
    if data is not None:
        print("File opened successfully ")
        read_pdf = PyPDF2.PdfReader(data)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        text_box.insert(1.0, page_content)
        instructions.config(text="Data Extracted ")
        browse_button.config(text="Browse")
        print("Extracted Data: ", "\n", page_content)
    else:
        print("Data problem/cancelled or sth else...")
        browse_button.config(text="Browse")


def sys_clear():
    text_box.delete(1.0, "end")
    instructions.config(text="Data Cleared")
    print("Data Cleared... ")
    return


# Textbox
text_box = tkinter.Text(root, height=10, width=50, pady=15, padx=15)
text_box.tag_configure("center", justify="center")  # Interesting statement!
text_box.tag_add("center", 1.0, "end")
text_box.grid(row=4, column=1)


# Browse button
browse_button = tkinter.Button(root,
                               text="Browse",
                               font="Raleway",
                               bg="#eb3535",  # Better for logo2:#eb3535//logo1:#20bebe
                               fg="white",
                               height=2, width=20,
                               command=sys_browse)
browse_button.grid(column=1, row=2)


# Clear Button
clear_button = tkinter.Button(root,
                              text="Clear",
                              font="Raleway",
                              bg="#eb3535",  # Better for logo2:#eb3535//logo1:#20bebe
                              fg="white",
                              height=2, width=20,
                              command=sys_clear)
clear_button.grid(row=16, column=1)


# Quit Button
quit_button = tkinter.Button(root,
                             text="Quit",
                             font="Raleway",
                             bg="#eb3535",  # Better for logo2:#eb3535//logo1:#20bebe
                             fg="white",
                             height=2, width=20,
                             command=root.destroy)
quit_button.grid(row=17, column=1)

root.mainloop()

print("Terminated... " + time.asctime())
