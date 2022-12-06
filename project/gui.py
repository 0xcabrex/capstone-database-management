from tkinter import *
from tkinter import messagebox
import os
import sys
from tkinter import ttk

import mysql.connector
from mysql.connector import Error

py=sys.executable

#creating window
class MainWin(Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='gray')
        self.canvas = Canvas(width=1366, height=768, bg='gray')
        self.canvas.pack()
        self.maxsize(1320, 768)
        self.minsize(1320,768)
        self.state('zoomed')
        self.title('CRUD Operation for "PROJECT" table')
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)
#calling scripts

        def ib():
            os.system('%s %s' % (py, 'project/Update.py'))

        def ret():
            os.system('%s %s' % (py, 'project/Delete.py'))

        def sea():
            os.system('%s %s' % (py,'project/Add.py'))


#creating table

        self.listTree = ttk.Treeview(self,height=14,columns=('Faculty Advisor','Project Name','Interdiciplinary','FID'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.hsb = ttk.Scrollbar(self,orient="horizontal",command=self.listTree.xview)
        self.listTree.configure(yscrollcommand=self.vsb.set,xscrollcommand=self.hsb.set)
        self.listTree.heading("#0", text='Group Number')
        self.listTree.column("#0", width=110,minwidth=50,anchor='center')
        self.listTree.heading("Faculty Advisor", text='Faculty Advisor')
        self.listTree.column("Faculty Advisor", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Project Name", text='Project Name')
        self.listTree.column("Project Name", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Interdiciplinary", text='Interdiciplinary')
        self.listTree.column("Interdiciplinary", width=125, minwidth=125,anchor='center')
        self.listTree.heading("FID", text='FID')
        self.listTree.column("FID", width=125, minwidth=125, anchor='center')
        
        self.listTree.place(x=200,y=360)
        self.vsb.place(x=955,y=363,height=287)
        self.hsb.place(x=200,y=650,width=770)
        ttk.Style().configure("Treeview",font=('Times new Roman',15))


        def ser():
             try:
                conn = mysql.connector.connect(host='localhost',
                                         database='capstone',
                                         user='root',
                                         password='toor')
                cursor = conn.cursor()

                cursor.execute("Select * from project")
                pc = cursor.fetchall()
                if pc:
                    self.listTree.delete(*self.listTree.get_children())
                    for row in pc:
                        self.listTree.insert("",'end',text=row[0] ,values = (row[1],row[2],row[3],row[4]))
                else:
                    messagebox.showinfo("Error", "No Student!")
             except Exception as e:
                #print(Error)
                messagebox.showerror("Error","Something went Wrong")
                raise e

        def check():

            #label and input box
            self.label3 = Label(self, text='CRUD Operation for "PROJECT" table',fg='black',bg="gray" ,font=('Courier new', 30, 'bold'))
            self.label3.place(x=350, y=22)
            self.label6 = Label(self, text="PROJECT INFORMATION DETAILS",bg="gray",  font=('Courier new', 15, 'underline', 'bold'))
            self.label6.place(x=560, y=300)
            self.button = Button(self, text='View Projects(s)', width=25,bg='blue', font=('Courier new', 10), command=ser).place(x=240,y=250)
            self.button = Button(self, text='Add Projects', width=25,bg='green', font=('Courier new', 10), command=sea).place(x=520,y=250)
            self.brt = Button(self, text="Update Projects", width=15,bg='orange', font=('Courier new', 10), command=ib).place(x=800, y=250)
            self.brt = Button(self, text="Delete Projects", width=15,bg='red', font=('Courier new', 10), command=ret).place(x=1000, y=250)

        check()

MainWin().mainloop()