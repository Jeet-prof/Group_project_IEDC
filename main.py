from tkinter import *
from tkinter import filedialog

from preprocess import preprocess

from ocr import extract_text

from cleaner import clean_text

from segment import segment

import os

os.makedirs("output",exist_ok=True)

def process():

    filename=filedialog.askopenfilename(

        filetypes=[("Images","*.jpg *.png *.jpeg")]

    )

    if filename=="":

        return

    clean_image=preprocess(filename)

    text=extract_text(clean_image)

    text=clean_text(text)

    with open("output/extracted_text.txt","w",encoding="utf-8") as f:

        f.write(text)

    answers=segment(text)

    with open("output/segmented_answers.txt","w",encoding="utf-8") as f:

        for q,a in answers:

            f.write(q+"\n")

            f.write(a+"\n")

            f.write("-"*40+"\n")

    textbox.delete("1.0",END)

    textbox.insert(END,text)

root=Tk()

root.title("OCR Answer Extraction")

root.geometry("700x600")

Button(

    root,

    text="Upload Answer Sheet",

    command=process,

    font=("Arial",14)

).pack(pady=15)

textbox=Text(root)

textbox.pack(fill=BOTH,expand=True)

root.mainloop()