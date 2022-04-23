from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()
root.maxsize(650,650)
root.minsize(650,650)

open_img = ImageTk.PhotoImage(Image.open("open.png"))
same_img = ImageTk.PhotoImage(Image.open("same.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.png"))

label_file_name = Label(root, text="Name")
label_file_name.place(relx=0.3,rely=0.1,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.5,rely=0.1, anchor= CENTER)

my_text= Text(root,height=5,width=40),,
my_text.place(relx=0.5,rely=0.4,anchor= CENTER)

name = ""
def openFile():
 global name 
my_text.delete(1.0, END)  
input_file_name.delete(0,END)
text_file = filedialog.askopenfilename(title = "open text file",filetypes = ((""Text Files", "*.txt""),))
print(text_file)
name = os.path.basename(text_file)
formated_name = name.spilt('.')[0]
input_file_name.insert(END,formated_name)
root.title(formated_name)
text_file = open(name,'r')
paragraph = text_file.read()
my_text.insert(END,paragraph)
text_file.close()

open_button=Button(root,image=open_imge,text="open file",command=openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
# Define clearInputFeild() function


# Define clearTextarea() function


# Define addData() function



open_button=Button(root,text="Clear Input field", command=clearInputFeild)
open_button.place(relx=0.25,rely=0.7,anchor=CENTER)
save_button=Button(root, text="Clear Textarea", command=clearTextarea)
save_button.place(relx=0.455,rely=0.7,anchor= CENTER)
exit_button=Button(root, text="Add data to input feild", command=addData)
exit_button.place(relx=0.7,rely=0.7,anchor= CENTER)

root.mainloop()

