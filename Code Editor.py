from tkinter import *
from tkinter.font import Font
from tkinter.filedialog import askopenfilename, asksaveasfilename


root = Tk()
root.title("Code Editor")
root.state("zoomed")
root.iconbitmap("icon.ico")
menu_1 = Menu(root)
root.config(menu=menu_1)


def save_as():
    filepath = asksaveasfilename(filetypes=[("Text File", "*.txt"), ("Python File", "*.py"),
                                            ("Java", "*.java"), ("C", "*.c"), ("C++", "*.cpp"), ("C#", "*.cs"), ("JavaScript", "*.js"), ("HTML", "*.html"), ("CSS", "*.css"), ("PHP", "*.php"), ("Ruby", "*.rb"), ("Swift", "*.swift"), ("Kotlin", "*.kt"), ("Perl", "*.pl"), ("SQL", "*.sql"), ("R", "*.r"), ("Matlab", "*.m"), ("GO", "*.go"), ("Assembly", "*.asm"), ("Scala", "*.scala"), ("TypeScript", "*.ts"), ("Rust", "*.rs"), ("Haskell", "*.hs"), ("Dart", "*.dart"), ("All Files", "*.*")], defaultextension=".txt")
    if filepath:
        with open(filepath, "w") as file:
            content = text.get("1.0", END) 
            file.write(content)


def open_o():
    filepath = askopenfilename(filetypes=[("Text File", "*.txt"), ("Python File", "*.py"),
                                            ("Java", "*.java"), ("C", "*.c"), ("C++", "*.cpp"), ("C#", "*.cs"), ("JavaScript", "*.js"), ("HTML", "*.html"), ("CSS", "*.css"), ("PHP", "*.php"), ("Ruby", "*.rb"), ("Swift", "*.swift"), ("Kotlin", "*.kt"), ("Perl", "*.pl"), ("SQL", "*.sql"), ("R", "*.r"), ("Matlab", "*.m"), ("GO", "*.go"), ("Assembly", "*.asm"), ("Scala", "*.scala"), ("TypeScript", "*.ts"), ("Rust", "*.rs"), ("Haskell", "*.hs"), ("Dart", "*.dart"), ("All Files", "*.*")], defaultextension=".txt")
    if filepath:
        with open(filepath,"r") as file:
            content = file.read()
            text.delete("1.0", "end")
            text.insert("1.0", content)


yscrollbar = Scrollbar(root, orient=VERTICAL)
yscrollbar.pack(side=RIGHT, fill=Y)
xscrollbar = Scrollbar(root, orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)


font_1 = Font(root, family="san_serif", weight="bold", size=16)


filemenu =  Menu(menu_1, tearoff=0)
menu_1.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=open_o)
filemenu.add_command(label="Save as", command=save_as)
filemenu.add_command(label="Exit", command=root.quit)


text = Text(root, font=font_1, selectbackground="sky blue",selectforeground="black",background="light yellow",
            yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set, wrap="none")
text.pack(fill=BOTH, expand=True)
yscrollbar.config(command=text.yview)
xscrollbar.config(command=text.xview)
root.mainloop()
