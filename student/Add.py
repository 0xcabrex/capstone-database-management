from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import sys
import mysql.connector
from mysql.connector import Error
import datetime
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(500,417)
        self.minsize(500,417)
        self.title('Add Student')
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
        self.label3 = Label(self, text='Insert student',fg='black',bg="gray" ,font=('Courier new', 30, 'bold'))
        self.label3.place(x=75, y=22)
        fname = StringVar()
        srn = StringVar()
        cn = StringVar()
        section = StringVar()
        yog = StringVar()
        c = StringVar()
#verifying input
        def asi():
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='capstone',
                                                        user='root',
                                                        password='toor')
                    self.myCursor = self.conn.cursor()
                    first = fname.get()
                    SRN = srn.get()
                    if len(SRN) != 13:
                        messagebox.showerror("Error", "SRN should only be 13 characters long")
                        return
                    grpid = cn.get()
                    try:
                        grpid = int(grpid)
                    except ValueError:
                        messagebox.showerror("Error", "GroupID must be an integer")
                        return
                    sec = section.get()
                    yearOfGraduation = yog.get()
                    try:
                        yearOfGraduation = int(yearOfGraduation)
                        if yearOfGraduation not in [datetime.date.today().year + 1 , datetime.date.today().year + 2]:
                            messagebox.showerror("Error", f"{yearOfGraduation} Year of graduation is not valid")
                            return
                    except ValueError:
                        messagebox.showerror("Error", "year of graduation must be a number")
                        return
                    
                    try:
                        result = self.myCursor.execute("INSERT INTO STUDENT VALUES (%s, %s, %s, %s, %s)", [first, SRN, sec, yearOfGraduation, grpid])
                    except mysql.connector.errors.IntegrityError as e:
                        messagebox.showerror("Integrity constraint failed", e)
                        return
                    print(result)
                    self.conn.commit()
                    messagebox.showinfo("Done","Student Inserted Successfully")
                    ask = messagebox.askyesno("Confirm","Do you want to add another student?")
                    if ask:
                     self.destroy()
                     os.system('%s %s' % (py, 'Add.py'))
                    else:
                     self.destroy()
                     self.myCursor.close()
                     self.conn.close()
                except Exception as e:
                    messagebox.showerror("Error",f"Something goes wrong\n{e}")
                    print(e.args)
                    raise e

        # label and input box
        Label(self, text='Student Details',bg='gray', fg='white', font=('Courier new', 25, 'bold')).pack()
        Label(self, text='Name:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=102)
        Entry(self, textvariable=fname, width=30).place(x=200, y=104)
        Label(self, text='SRN:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=150)
        Entry(self, textvariable=srn, width=30).place(x=200, y=152)
        Label(self, text='Section:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=200)
        Entry(self, textvariable=section, width=30).place(x=200, y=202)
        Label(self, text='Year of Graduation:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=250)
        Entry(self, textvariable=yog, width=30).place(x=200, y=250)
        Label(self, text='Group ID:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=300)
        Entry(self, textvariable=cn, width=30).place(x=200, y=300)

        Button(self, text="Save", bg='blue', width=15, command=asi).place(x=230, y=380)

Add().mainloop()