from tkinter import *
from tkinter import filedialog
import os
import RandomEncryption.Encrypt as Encrypt


def uploadContent(root):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")],
                                           title='Open File',
                                           initialdir=str(os.getcwd()))
    file = open(file_path, "r")

    print(root.winfo_children())
    content = root.winfo_children()[1]
    content.configure(state="normal")
    content.delete("1.0", END)
    for line in file:
        content.insert(END, line)

    content.configure(state="disabled")
    file.close()


def createEncryptFile(root):
    content = root.winfo_children()[1]
    text = content.get("1.0", END)
    if not os.path.exists(os.getcwd() + "\.\Dictionaries"):
        print("creating...")
        os.mkdir(os.getcwd() + "\.\Dictionaries")
    else:
        print("already have dir")
    path = os.getcwd() + "\.\Dictionaries"
    count = len(os.listdir(path))
    print(path, count)
    etext = Encrypt.encrypt(text, "Dictionaries\dictionary" + str(count + 1) + ".txt")
    file_path = filedialog.asksaveasfile(filetypes=[("text files", "*.txt")])
    file = open(file_path.name, "w")
    file.write(etext)

    file.close()
    content.configure(state="normal")
    content.delete("1.0", END)
    content.insert(END, etext)
    content.configure(state="disabled")


def createDecryptFile(root):
    content = root.winfo_children()[1]

    etext = content.get("1.0", END)

    file_path = filedialog.askopenfilename(filetypes=[("text files", "*.txt")],
                                           initialdir=str(os.getcwd() + "/./Dictionaries"))
    text = Encrypt.decrypt(etext, file_path)
    content.configure(state="normal")
    content.delete("1.0", END)
    content.insert(END, text)
    content.configure(state="disabled")


def openNewWindow():
    root = Toplevel(start)
    root.geometry("500x500")

    titleLabel = Label(root, height=0, width=0, text="Text of file here:", font=20)
    titleLabel.place(x=0, y=0)

    content = Text(root, height=30, width=30)
    content.configure(state="disabled")
    content.place(x=120, y=10)

    uploadButton = Button(root, command=lambda: uploadContent(root), text="Upload", height=2, width=10)
    uploadButton.place(x=400, y=85)

    encryptButton = Button(root, command=lambda: createEncryptFile(root), text="Encrypt", height=2, width=10)
    encryptButton.place(x=400, y=125)

    decryptButton = Button(root, command=lambda: createDecryptFile(root), text="Decrypt", height=2, width=10)
    decryptButton.place(x=400, y=165)

    root.mainloop()


if __name__ == '__main__':
    start = Tk()
    start.geometry("300x300")
    btn = Button(start,
                 text="Click to open a the encryption window",
                 command=openNewWindow,
                 height=2, width=30)
    btn.place(x=50, y=50)
    start.mainloop()
