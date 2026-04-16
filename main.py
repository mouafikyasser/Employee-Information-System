from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
db = Database("Employee.db")




#interface
root = Tk()
root.title('Employee Information System')
root.geometry('1240x615+0+0')
root.resizable(False,False)
root.configure(bg='#2c3e50')


#logo setting
logo = PhotoImage(file='logo.png')
lbl_logo = Label(root ,image=logo , bg='#2c3e50')
lbl_logo.place(x=10 ,y=390)


#inputs varianles
name = StringVar()
age = StringVar()
job = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()


#mini interface
entries_frame = Frame(root , bg='#2c3e50')
entries_frame.place(x=1,y=1 ,width=360 ,height=510)
title = Label(entries_frame , text='Employee Company',font =('calbiri',18,'bold') , bg='#2c3e50', fg='white')
title.place(x=10 ,y=1)


#input employee information
lbl_name = Label(entries_frame , text="Name",font =('calbiri',16) , bg='#2c3e50', fg='white')
lbl_name.place(x=10 ,y=50)
txt_name = Entry(entries_frame ,textvariable=name ,width=20 , font =('calbiri',16))
txt_name.place(x=120 ,y=50)

lbl_job = Label(entries_frame , text="Job",font =('calbiri',16) , bg='#2c3e50', fg='white')
lbl_job.place(x=10 ,y=90)
txt_job = Entry(entries_frame ,textvariable=job ,width=20 , font =('calbiri',16))
txt_job.place(x=120 ,y=90)

lbl_gender = Label(entries_frame , text="Gneder",font =('calbiri',16) , bg='#2c3e50', fg='white')
lbl_gender.place(x=10 ,y=130)
combo_gender = ttk.Combobox(entries_frame ,textvariable=gender ,state='readonly' ,width=18 ,font =('calbiri',16) ,)
combo_gender['values'] = ("Male","Female")
combo_gender.place(x=120 ,y=130)

lbl_age = Label(entries_frame , text="Age",font =('calbiri',16) , bg='#2c3e50', fg='white')
lbl_age.place(x=10 ,y=170)
txt_age = Entry(entries_frame ,textvariable=age ,width=20 ,font =('calbiri',16))
txt_age.place(x=120 ,y=170)

lbl_Email = Label(entries_frame , text="Email",font =('calbiri',16) , bg='#2c3e50', fg='white')
lbl_Email.place(x=10 ,y=210)
txt_Email = Entry(entries_frame ,textvariable=email ,width=20 , font =('calbiri',16))
txt_Email.place(x=120 ,y=210)

lbl_contact = Label(entries_frame , text="Contact",font =('calbiri',16) , bg='#2c3e50', fg='white')
lbl_contact.place(x=10 ,y=250)
txt_contact = Entry(entries_frame ,textvariable=contact ,width=20 , font =('calbiri',16))
txt_contact.place(x=120 ,y=250)

lbl_address = Label(entries_frame , text="Address :",font =('calbiri',16) , bg='#2c3e50', fg='white')
lbl_address.place(x=10 ,y=290)
txt_address = Text(entries_frame ,width=30 ,height=2 ,font =('calbiri',16) )
txt_address.place(x=10, y=330)


#hide and show button
def hide():
    root.geometry("360x515+0+0")
def show():
    root.geometry('1240x615+0+0')

btn_hide = Button(entries_frame ,text='HIDE' ,bg='white' ,bd=1 ,relief=SOLID ,cursor='hand2' ,command=hide)
btn_hide.place(x=270 ,y=10)

btn_show = Button(entries_frame ,text='SHOW' ,bg='white' ,bd=1 ,relief=SOLID ,cursor='hand2',command=show)
btn_show.place(x=310 ,y=10)


#get data clicked
def get_data(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row 
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txt_address.delete(1.0,END)
    txt_address.insert(END ,row[7])


#show all information in table
def display_all():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("" ,END ,values=row)


#delete employee from database
def delete():
    db.remove(row[0])
    clear()
    display_all()


#clear 
def clear():
    name.set("")
    age.set("")
    job.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txt_address.delete(1.0,END)


#fonction for error (some information is missing)
def add_employee():
    if txt_name.get() == "" or txt_age.get() == "" or txt_job.get() == "" or txt_Email.get() == "" or combo_gender.get() == "" or txt_contact.get() == "" or txt_address.get(1.0,END) == "" :
        messagebox.showerror("Error"," Please Fill all the Entry")
        return
    db.insert(
        txt_name.get() ,
        txt_age.get() ,
        txt_job.get() ,
        txt_Email.get() ,
        combo_gender.get() ,
        txt_contact.get() ,
        txt_address.get(1.0 ,END))
    messagebox.showinfo("Success"," Added new Employee")
    clear()
    display_all()


#update information
def update():
    if txt_name.get() == "" or txt_age.get() == "" or txt_job.get() == "" or txt_Email.get() == "" or combo_gender.get() == "" or txt_contact.get() == "" or txt_address.get(1.0,END) == "" :
        messagebox.showerror("Error"," Please Fill all the Entry")
        return
    db.update(row[0] ,
        txt_name.get() ,
        txt_age.get() ,
        txt_job.get() ,
        txt_Email.get() ,
        combo_gender.get() ,
        txt_contact.get() ,
        txt_address.get(1.0 ,END))
    messagebox.showinfo('Success','The employee data is udpdate')
    clear()
    display_all()



#button for functions

#place of button
btn_frame = Frame(entries_frame ,bg='#2c3e50' ,bd=1 , relief=SOLID)
btn_frame.place(x=10 ,y=400 ,width=335 , height=100)

#add button
btn_add = Button(btn_frame ,
                 text='Add Details',
                 width=14 ,
                 height=1 ,
                 font=('calibri' ,16) ,
                 fg= 'white' ,
                 bg=('#16a085') ,
                 bd=0 ,
                 cursor='hand2',
                 command=add_employee
                 ).place(x=4 ,y=5)

#edit button
btn_edit = Button(btn_frame ,
                 text='Update Details',
                 width=14 ,
                 height=1 ,
                 font=('calibri' ,16) ,
                 fg= 'white' ,
                 bg=('#2980b9') ,
                 bd=0 ,
                 cursor='hand2' ,
                 command=update
                 ).place(x=4 ,y=50)

#delete button
btn_delete = Button(btn_frame ,
                 text='Delete Details',
                 width=14 ,
                 height=1 ,
                 font=('calibri' ,16) ,
                 fg= 'white' ,
                 bg=('#c0392b') ,
                 bd=0 ,
                 cursor='hand2',
                 command=delete
                 ).place(x=170 ,y=5)

#clear button
btn_clear = Button(btn_frame ,
                 text='Clear Details',
                 width=14 ,
                 height=1 ,
                 font=('calibri' ,16) ,
                 fg= 'white' ,
                 bg=("#f39c12") ,
                 bd=0 ,
                 cursor='hand2',
                 command=clear
                 ).place(x=170 ,y=50)



#view allinformation in the table
tree_frame = Frame(root ,bg='white')
tree_frame.place(x=365 ,y=1 , width=875 ,height=610 )
style = ttk.Style()
style.configure("mystyle.Treeview" ,font=('Calibri' ,13) ,rowheight=50)
style.configure("mystyle.Treeview.heading" ,font=('Calibri' ,13))

tv = ttk.Treeview(tree_frame ,columns=(1 ,2 ,3 ,4 ,5 ,6 ,7 ,8) ,style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1" ,width="40")

tv.heading("2", text="Name")
tv.column("2" ,width="140")

tv.heading("3", text="Age")
tv.column("3" ,width="50")

tv.heading("4", text="Job")
tv.column("4" ,width="120")

tv.heading("5", text="Email")
tv.column("5" ,width="150")

tv.heading("6", text="Gender")
tv.column("6" ,width="90")

tv.heading("7", text="Contact")
tv.column("7" ,width="150")

tv.heading("8", text="Address")
tv.column("8" ,width="150")

tv['show'] = 'headings'

tv.bind("<ButtonRelease-1>" ,get_data)

tv.place(x=1 ,y=1 , height=610 ,width=875)





display_all()
root.mainloop()