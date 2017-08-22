from tkinter import *
import Backend

def get_selected(event):
    global selected_row
    index=lb1.curselection()[0]
    selected_row=lb1.get(index)
    print(selected_row)
    e1.delete(0,END)
    e1.insert(END,selected_row[1])
    e2.delete(0,END)
    e2.insert(END,selected_row[2])
    e3.delete(0,END)
    e3.insert(END,selected_row[3])
    e4.delete(0,END)
    e4.insert(END,selected_row[4])

def view_command():
    lb1.delete(0,END)
    for row in Backend.view():
        lb1.insert(END,row)

def insert_command():
    Backend.insert(title_data.get(),author_data.get(),year_data.get(),isbn_data.get())
    lb1.delete(0,END)
    lb1.insert(END,(title_data.get(),author_data.get(),year_data.get(),isbn_data.get()))

def search_command():
    lb1.delete(0,END)
    for row in Backend.search(title_data.get(),author_data.get(),year_data.get(),isbn_data.get()):
        lb1.insert(END,row)

def delete_command():
    Backend.delete(selected_row[0])
    view_command()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def update_command():
    Backend.update(selected_row[0],title_data.get(),author_data.get(),year_data.get(),isbn_data.get())
    view_command()

window=Tk()

window.vm_title("Books Database Manager")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_data = StringVar()
e1=Entry(window,textvariable=title_data)
e1.grid(row=0,column=1)

author_data = StringVar()
e2=Entry(window,textvariable=author_data)
e2.grid(row=0,column=3)

year_data = StringVar()
e3=Entry(window,textvariable=year_data)
e3.grid(row=1,column=1)

isbn_data = StringVar()
e4=Entry(window,textvariable=isbn_data)
e4.grid(row=1,column=3)

lb1=Listbox(window,height=6,width=35)
lb1.grid(row=2,column=0,rowspan=6,columnspan=2)
lb1.bind("<<ListboxSelect>>",get_selected)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)

b1=Button(window,text="View All",width=20,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=20,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=20,command=insert_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update Selected",width=20,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Selected",width=20,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=20,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
