from tkinter import *
import os
import sys

py=sys.executable


class StartingPoint(Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='gray')
        self.canvas = Canvas(width=1366, height=768, bg='gray')
        self.canvas.pack()
        self.maxsize(920,368)
        self.minsize(920,368)
        self.state('zoomed')
        self.title('Capstone Database management')
        self.mymenu = Menu(self)

        def fac():
            os.system('%s %s' % (py, 'faculty/gui.py'))
        
        def proj():
            os.system('%s %s' % (py, 'project/gui.py'))
        
        def student():
            os.system('%s %s' % (py, 'student/gui.py'))

        def main():
        
            self.label3 = Label(self, text='Capstone Database Management',fg='black',bg="gray" ,font=('Courier new', 20, 'bold'))
            self.label3.place(x=250, y=22)
            self.label3 = Label(self, text='Note: Insert in faculty first, then insert a project and then insert students for the project',fg='black',bg="gray" ,font=('Courier new', 10, 'bold')).place(x=70, y=150)
            self.button = Button(self, text='Faculty table', width=25,bg='blue', font=('Courier new', 10), command=fac).place(x=100,y=250)
            self.button = Button(self, text='Project table', width=25,bg='green', font=('Courier new', 10), command=proj).place(x=380,y=250)
            self.brt = Button(self, text="Student table", width=15,bg='orange', font=('Courier new', 10), command=student).place(x=660, y=250)
        
        main()

StartingPoint().mainloop()