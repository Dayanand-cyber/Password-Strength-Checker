import tkinter,math,re
from tkinter import PhotoImage,messagebox

def entropy(password):
    length=len(password)
    entropy=math.log(94**length,2)
    return entropy

def regx(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$&*$%^])(?!.*\s).{8,}$'
    return bool(re.match(pattern, password))

def check_password():
    password=password_box.get()
    if password:
        if entropy(password)>60 and regx(password)==True:
            string="Your Password Is Strong"
            output.config(text=string)
            output.pack(pady=10)
        elif regx(password)==False:
            if len(password)<8:
                messagebox.showwarning("warning","Password Must Have 8 Character")
            else:
                messagebox.showwarning("warning","Your Password Must Atleast Have One\nUpper,Lower Case Letter,\nNumber And A Special Character ")

        else:
            string="Your Password Is weak"
            output.config(text=string)
            output.pack(pady=10)

    else:
        messagebox.showwarning("warning","Plase Enter The Password")



root=tkinter.Tk()

root.title("Password Strenght checker")
root.geometry("540x360")
root.resizable(False, False)

background_path=PhotoImage(file=r"C:\Users\ASUS\Desktop\vscode\skill high\password checker\360_F_119115529_mEnw3lGpLdlDkfLgRcVSbFRuVl6sMDty.png")
background_image=tkinter.Label(root,image=background_path)
background_image.place(x=0,y=0,relheight=1,relwidth=1)

header=tkinter.Label(root,text="Password Strength Checker",font=("georgia",24),fg="red",highlightbackground="dark blue",highlightthickness=5)
header.pack(pady=10)

text_box_header=tkinter.Label(root,text="Enter Your Password",font=("georgia",13),highlightbackground="dark blue",highlightthickness=5)
text_box_header.pack(pady=10)

password_box=tkinter.Entry(root,highlightbackground="black",highlightthickness=2)
password_box.pack(pady=10)

check=tkinter.Button(root,text="Check",command=check_password)
check.pack(pady=5)

output=tkinter.Label(root,text="",font=("Helvetica",13),highlightbackground='black',highlightthickness=2)



root.mainloop()