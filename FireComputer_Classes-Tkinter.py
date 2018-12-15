from tkinter import *
import math as m

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
        self._p_mass_str.grid(sticky='w', row=1, column=0)
        self._sh_mass_str = Label(self, text='Shell Mass (Kg):')
        self._sh_mass_str.grid(sticky='w', row=2, column=0)

        self._p_mass = Entry(self)
        self._p_mass.grid(sticky='w', row=1, column=1)
        self._sh_mass = Entry(self)
        self._sh_mass.grid(sticky='w', row=2, column=1)

        self._calc_button = Button(self, text='Calculate', command=self.SS_calculate)
        self._calc_button.grid(sticky='w', row=3, column=0)

    def SS_calculate(self):
        try:
            p_mass = int(self._p_mass.get())
            sh_mass = int(self._sh_mass.get())

        except ValueError:
            _error_message = Label(self, text='You can only calculate numbers.')
            _error_message.grid(sticky='n', row=4, column=1)

        vel = round((1500 * m.pow((p_mass/sh_mass), 0.45)), 2)
        vel_txt = "Calculated Velocity: " + str(vel)
        vel_str = Label(self, text=vel_txt)
        vel_str.grid(sticky='w', row=5)

    def FOS_click(self):
        self._vel_str = Label(self, text='Velocity (m/s):')
        self._vel_str.grid(sticky='w', row=1, column=0)
        self._dist_str = Label(self, text='Target Distance (m):')
        self._dist_str.grid(sticky='w', row=2, column=0)

        self._vel = Entry(self)
        self._vel.grid(sticky='w', row=1, column=1)
        self._dist = Entry(self)
        self._dist.grid(sticky='w', row=2, column=1)

        self._calc_button = Button(self, text='Calculate', command=self.FOS_calculate)
        self._calc_button.grid(sticky='w', row=3, column=0)

    def FOS_calculate(self):
        _G = 9.81

        try:
            vel = int(self._vel.get())
            dist = int(self._dist.get())

        except ValueError:
            _error_message = Label(self, text='You can only calculate numbers.')
            _error_message.grid(sticky='n', row=4, column=1)

        angle_rad = (0.5 * m.asin((_G * dist) / (m.pow(vel, 2))))
        angle_deg = round(m.degrees(angle_rad), 2)
        agl_txt = "Calculated Angle (deg): "+str(angle_deg)
        agl_str = Label(self, text=agl_txt)
        agl_str.grid(sticky='w', row=5)

        horz_vel = vel*m.cos(angle_rad)
        flight_time = horz_vel/dist
        flight_str = "Estimated Flight Time (S): " + str(round(flight_time,2))
        flight_txt = Label(self, text=flight_str)
        flight_txt.grid(sticky='w', row=6)

    def EXIT_click(self):
        quit()


app = App()
app.master.title("Projectile Motion Computer")
app.mainloop()