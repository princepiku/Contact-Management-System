from tkinter import *
import sqlite3
import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Contact-List")
width = 635
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="pink")

#============================VARIABLES===================================

FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
AGE = StringVar()
ADDRESS = StringVar()
CONTACT = StringVar()

#============================METHODS=====================================

# METHODS

def Exit():
    wayOut = tkinter.messagebox.askyesno("Contact Management System", "Do you wants to exit!")
    if wayOut > 0:
        root.destroy()
        return

def Database():
    conn = sqlite3.connect("PythonAlex.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Member` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age INTEGER, address TEXT, contact INTEGER)")
    cursor.execute("SELECT * FROM `Member` ORDER BY `lastname` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SubmitData():
    if  FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or AGE.get() == "" or ADDRESS.get() == "" or CONTACT.get() == "":
        result = tkMessageBox.showwarning('', 'Please complete the required field!', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("PythonAlex.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `Member` (firstname, lastname, gender, age, address, contact) VALUES (?, ?, ?, ?, ?, ?)", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), int(AGE.get()), str(ADDRESS.get()), int(CONTACT.get())))
        conn.commit()
        tkMessageBox.showinfo("Message","Stored Successfully!")
        cursor.execute("SELECT * FROM `Member` ORDER BY `lastname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        ADDRESS.set("")
        CONTACT.set("")

def UpdateData():
    if GENDER.get() == "":
       result = tkMessageBox.showwarning('', 'Please complete the required field!', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("PythonAlex.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `Member` SET `firstname` = ?, `lastname` = ?, `gender` = ?, `age` = ?, `address` = ?, `contact` = ? WHERE `mem_id` = ?", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), int(AGE.get()), str(ADDRESS.get()), int(CONTACT.get()), int(mem_id)))
        conn.commit()
        tkMessageBox.showinfo("Message","Updated Successfully!")
        cursor.execute("SELECT * FROM `Member` ORDER BY `lastname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        ADDRESS.set("")
        CONTACT.set("")

def OnSelected(event):
    global mem_id, UpdateWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS.set("")
    CONTACT.set("")
    FIRSTNAME.set(selecteditem[1])
    LASTNAME.set(selecteditem[2])
    AGE.set(selecteditem[4])
    ADDRESS.set(selecteditem[5])
    CONTACT.set(selecteditem[6])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Contact-List")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width / 2) + 450) - (width / 2)
    y = ((screen_height / 2) + 20) - (height / 2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()

    #===================FRAMES==============================

    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male", font=('Lucida Fax', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female", font=('Lucida Fax', 14)).pack(side=LEFT)

    #===================LABELS==============================

    lbl_title = Label(FormTitle, text="Updating Contact", font=('Lucida Fax', 16), bg="orange", width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="First Name", font=('Lucida Fax', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Last Name", font=('Lucida Fax', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('Lucida Fax', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Age", font=('Lucida Fax', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="Address", font=('Lucida Fax', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="Contact", font=('Lucida Fax', 14), bd=5)
    lbl_contact.grid(row=5, sticky=W)

    #===================ENTRY===============================

    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('Lucida Fax', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('Lucida Fax', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(ContactForm, textvariable=AGE, font=('Lucida Fax', 14))
    age.grid(row=3, column=1)
    address = Entry(ContactForm, textvariable=ADDRESS, font=('Lucida Fax', 14))
    address.grid(row=4, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT, font=('Lucida Fax', 14))
    contact.grid(row=5, column=1)

    #==================BUTTONS==============================

    btn_updatecon = Button(ContactForm, text="Update", width=8, bg="orange", font=('Lucida Fax', 12), command=UpdateData)
    btn_updatecon.grid(row=6, columnspan=2, pady=10)

def DeleteData():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please select record first!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure!\nYou want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("PythonAlex.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `member` WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            tkMessageBox.showinfo("Message","Deleted Successfully!")
            cursor.close()
            conn.close()

def AddNewWindow():
    global NewWindow
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS.set("")
    CONTACT.set("")
    NewWindow = Toplevel()
    NewWindow.title("Contact-List")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width / 2) - 455) - (width / 2)
    y = ((screen_height / 2) + 20) - (height / 2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()

    #===================FRAMES==============================

    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male", font=('Lucida Fax', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female", font=('Lucida Fax', 14)).pack(side=LEFT)

    #===================LABELS==============================

    lbl_title = Label(FormTitle, text="Adding New Contact", font=('Lucida Fax', 16), bg="sky blue",  width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="First Name", font=('Lucida Fax', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Last Name", font=('Lucida Fax', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('Lucida Fax', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Age", font=('Lucida Fax', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="Address", font=('Lucida Fax', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="Contact", font=('Lucida Fax', 14), bd=5)
    lbl_contact.grid(row=5, sticky=W)

    #===================ENTRY===============================

    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('Lucida Fax', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('Lucida Fax', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(ContactForm, textvariable=AGE, font=('Lucida Fax', 14))
    age.grid(row=3, column=1)
    address = Entry(ContactForm, textvariable=ADDRESS, font=('Lucida Fax', 14))
    address.grid(row=4, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT, font=('Lucida Fax', 14))
    contact.grid(row=5, column=1)

    #==================BUTTONS==============================

    btn_addcon = Button(ContactForm, text="Save", width=8, bg="green", font=('Lucida Fax', 12), command=SubmitData)
    btn_addcon.grid(row=6, columnspan=2, pady=10)

#============================FRAMES======================================

Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500,  bg="sky blue")
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="sky blue")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)

#============================LABELS======================================

lbl_title = Label(Top, text="Contact Management System", font=('Lucida Bright', 18), width=500)
lbl_title.pack(fill=X)

#============================ENTRY=======================================

#============================BUTTONS=====================================

btn_add = Button(MidLeftPadding, text="+ ADD NEW", bg="gray", font=('Lucida Fax', 12), command=AddNewWindow)
btn_add.pack(side=LEFT)
btn_delete = Button(MidLeftPadding, text="DELETE", bg="brown", font=('Lucida Fax', 12), command=DeleteData)
btn_delete.pack(side=RIGHT)
btn_exit = Button(MidLeftPadding, text="Exit", bg="orange", font=('Lucida Fax', 12), command=Exit)
btn_exit.pack(side=TOP)

#============================TABLES======================================

scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("MemberID", "First Name", "Last Name", "Gender", "Age", "Address", "Contact"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MemberID', text="MemberID", anchor=W)
tree.heading('First Name', text="First Name", anchor=W)
tree.heading('Last Name', text="Last Name", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Age', text="Age", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Contact', text="Contact", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

#============================INITIALIZATION==============================

if __name__ == '__main__':
    Database()
    root.mainloop()

