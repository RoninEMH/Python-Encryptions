from tkinter import *
from tkinter import filedialog
import os
import RandomEncryption.Encrypt as Encrypt


def uploadContent():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")],
                                           title='Open File',
                                           initialdir=str(os.getcwd()))
    file = open(file_path, "r")

    content.configure(state="normal")
    content.delete("1.0", END)
    for line in file:
        content.insert(END, line)

    content.configure(state="disabled")
    file.close()


def createEncryptFile():
    text = content.get("1.0", END)
    path = os.getcwd() + "\.\Dictionaries"
    count = len(os.listdir(path))
    print(path, count)
    etext = Encrypt.encrypt(text, "Dictionaries\dictionary" + str(count + 1) + ".txt")
    file_path = filedialog.asksaveasfile(filetypes=[("text files", "*.txt")])
    file = open(file_path.name, "w")
    file.write(etext)


if __name__ == '__main__':
    root = Tk()
    root.geometry("750x750")

    content = Text(root, height=20, width=20)
    content.configure(state="disabled")
    content.grid(row=0, column=0)

    uploadButton = Button(root, command=uploadContent, text="upload")
    uploadButton.grid(row=0, column=450)

    createButton = Button(root, command=createEncryptFile, text="create")
    createButton.grid(row=20, column=450)

    root.mainloop()
