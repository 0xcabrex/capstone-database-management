from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
#creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(400, 200)
        self.minsize(400, 200)
        self.title("Delete Student")
        self.canvas = Canvas(width=1366, height=768, bg='gray')
        self.canvas.pack()
        a = StringVar()
        def ent():
            if len(a.get()) ==0:
                messagebox.showinfo("Error","Please Enter A Valid Id")
            else:
                d = messagebox.askyesno("Confirm", "Are you sure you want to delete the Student?")
                if d:
                    try:
                        self.conn = mysql.connector.connect(host='localhost',
                                         database='capstone',
                                         user='root',
                                         password='toor')
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from student where SRN = %s",[a.get()])
                        self.conn.commit()
                        if self.myCursor.rowcount == 0:
                            messagebox.showinfo("Message", f"Student with SRN '{a.get()}' not found.\nNo change has been done")
                        else:
                            messagebox.showinfo("Confirm","Student Deleted Successfully")
                        self.myCursor.close()
                        self.conn.close()
                        a.set("")
                    except Exception as e:
                        messagebox.showerror("Error",f"Something went wrong\n{e}")
                        raise e
        Label(self, text = "Enter SRN: ",bg='gray',fg='black',font=('Courier new', 15, 'bold')).place(x = 5,y = 40)
        Entry(self,textvariable = a,width = 20).place(x = 210,y = 44)
        Button(self, text='Delete', width=15, font=('arial', 10),command = ent).place(x=200, y = 90)



Rem().mainloop()