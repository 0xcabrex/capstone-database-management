from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import sys
import mysql.connector
from mysql.connector import Error
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(500,417)
        self.minsize(500,417)
        self.title('Add Project')
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
        self.label3 = Label(self, text='Insert project',fg='black',bg="gray" ,font=('Courier new', 30, 'bold'))
        self.label3.place(x=75, y=22)
        gno = StringVar()
        fAdv = StringVar()
        fID = StringVar()
        pName = StringVar()
        interDisc = StringVar()
        c = StringVar()
#verifying input
        def asi():
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='capstone',
                                                        user='root',
                                                        password='toor')
                    self.myCursor = self.conn.cursor()
                    first = gno.get()
                    SRN = fAdv.get()
                    grpid = fID.get()
                    try:
                        grpid = int(grpid)
                    except ValueError:
                        messagebox.showerror("Error","Faculty ID can only be an integer")
                        return
                    sec = pName.get()
                    yearOfGraduation = interDisc.get()
                    try:
                        yearOfGraduation = int(yearOfGraduation)
                        if yearOfGraduation not in [0, 1]:
                            messagebox.showerror("Error", "Interdisciplinary field can only be 0 or 1")
                            return
                    except ValueError:
                        messagebox.showerror("Error", "Interdisciplinary field can only be 0 or 1")
                        return

                    try:
                        result = self.myCursor.callproc("insertProject", (SRN, sec, yearOfGraduation, grpid, 0))
                        print(result)
                    except mysql.connector.errors.IntegrityError:
                        messagebox.showerror("Integrity constraint failed", f"There is no project with number {grpid}. Please insert one first")
                        return
                    
                    self.conn.commit()
                    if result[4] == 1:
                        messagebox.showinfo("Done","Project Inserted Successfully")
                    else:
                        messagebox.showerror("Error", "Could not insert. Check if FID exists, or Faculty has too many projects")
                    ask = messagebox.askyesno("Confirm","Do you want to add another project?")
                    if ask:
                     self.destroy()
                     os.system('%s %s' % (py, 'Add.py'))
                    else:
                     self.destroy()
                     self.myCursor.close()
                     self.conn.close()
                except Exception as e:
                    messagebox.showerror("Error",f"Something went wrong\n{e}")
                    print(e.args)
                    raise e

        # label and input box
        Label(self, text='Student Details',bg='gray', fg='white', font=('Courier new', 25, 'bold')).pack()
        Label(self, text='Faculty Advisor:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=150)
        Entry(self, textvariable=fAdv, width=30).place(x=250, y=152)
        Label(self, text='Project Name:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=200)
        Entry(self, textvariable=pName, width=30).place(x=250, y=202)
        Label(self, text='Interdisciplinary:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=250)
        Entry(self, textvariable=interDisc, width=30).place(x=250, y=250)
        Label(self, text='FID:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=300)
        Entry(self, textvariable=fID, width=30).place(x=250, y=300)
        Button(self, text="Save", bg='blue', width=15, command=asi).place(x=230, y=380)

Add().mainloop()