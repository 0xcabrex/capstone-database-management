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
        self.title('Add Faculty')
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
        self.label3 = Label(self, text='Insert faculty',fg='black',bg="gray" ,font=('Courier new', 30, 'bold'))
        self.label3.place(x=75, y=22)
        fname = StringVar()
        designation = StringVar()
        domain = StringVar()
        yoe = StringVar()
        aoi = StringVar()
        acceptablegrps = StringVar()
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
                    des = designation.get()
                    dom = domain.get()
                    yearsOfExperience = yoe.get()
                    try:
                        yearsOfExperience = int(yearsOfExperience)
                    except ValueError:
                        messagebox.showerror("Error", "years of Experience must be a number")
                        return
                    areasOfInterest = aoi.get()
                    acceptableGrps = acceptablegrps.get()
                    try:
                        acceptableGrps = int(acceptableGrps)
                    except ValueError:
                        messagebox.showerror("Error", "acceptableGrps must be a number")
                        return

                    print(first, des, dom, yearsOfExperience, areasOfInterest, acceptableGrps)
                    try:

                        result = self.myCursor.callproc("InsertFaculty", (first, des, yearsOfExperience, areasOfInterest, dom, acceptableGrps, 0))
                    except mysql.connector.errors.IntegrityError as e:
                        messagebox.showerror("Integrity constraint failed", f"Somehow integrity constraint happened bro...\n {e}")
                        return
                    print(result)
                    self.conn.commit()
                    if result[6] == 1:
                        messagebox.showinfo("Done","Faculty Inserted Successfully")
                    else:
                        messagebox.showerror("Error", "Couldnt insert, faculty with same name already exists")
                    ask = messagebox.askyesno("Confirm","Do you want to add another faculty?")
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
        Label(self, text='Faculty Details',bg='gray', fg='white', font=('Courier new', 25, 'bold')).pack()
        Label(self, text='Name:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=102)
        Entry(self, textvariable=fname, width=30).place(x=200, y=104)
        Label(self, text='Designation:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=150)
        Entry(self, textvariable=designation, width=30).place(x=200, y=152)
        Label(self, text='Years of Exp:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=200)
        Entry(self, textvariable=yoe, width=30).place(x=200, y=202)
        Label(self, text='Areas of Interest:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=250)
        Entry(self, textvariable=aoi, width=30).place(x=200, y=250)
        Label(self, text='Domain:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=300)
        Entry(self, textvariable=domain, width=30).place(x=200, y=300)
        Label(self, text='Acceptable Grps:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=350)
        Entry(self, textvariable=acceptablegrps, width=30).place(x=200, y=350)
        
        Button(self, text="Save", bg='blue', width=15, command=asi).place(x=230, y=380)

Add().mainloop()