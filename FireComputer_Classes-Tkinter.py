from tkinter import *


class App(Frame):
    def __init__(self, master=None):
        super(App, self).__init__(master)
        self.grid()
        self.MM()

    def MM(self):
        self._SS_button = Button(self, text="Shell Statistics",command=self.SS_click)
        self._FOS_button = Button(self, text="Calculate Angle", command=self.FOS_click)
        self._EXIT_button = Button(self, text="OFF", command=self.EXIT_click)

        self._SS_button.grid(row=0, column=0)
        self._FOS_button.grid(row=0, column=1)
        self._EXIT_button.grid(row=0, column=2)

    def SS_click(self):
        self._p_mass_str = Label(self, text='Powder Mass (Kg):')
        self._p_mass_str.grid(sticky='w',row=1,column=0)
        self._sh_mass_str = Label(self,text='Shell Mass (Kg):')
        self._sh_mass_str.grid(sticky='w',row=2,column=0)

        self._p_mass = Entry(self)
        self._p_mass.grid(sticky='w',row=1,column=1)
        self._sh_mass = Entry(self)
        self._sh_mass.grid(sticky='w',row=2,column=1)

        self._calc_button = Button(self, text='Calculate',command=self.SS_calculate)
        self._calc_button.grid(sticky='w',row=3,column=0)

    def SS_calculate(self):
        try:
            p_mass = int(self._p_mass.get())
            sh_mass = int(self._sh_mass.get())

        except ValueError:
            self._error_message = Label(self,text='You can only calculate numbers.')
            self._error_message.grid(sticky='n',row=4,column=1)




    def FOS_click(self):
        pass

    def FOS_calculate(self):
        pass

    def EXIT_click(self):
        quit()


app = App()
app.master.title("Projectile Motion Computer")
app.mainloop()