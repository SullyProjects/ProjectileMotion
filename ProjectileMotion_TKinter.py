from tkinter import *

def SS_click():
    line = Label(root, text="Enter powder mass:")
    line.grid(row=2)
    p_mass = Entry(root)
    sting_mass = p_mass.get()
    int_mass = int(sting_mass)
    p_mass.grid(row=2, column=1)
    print(int_mass)


def FOS_click():
    FOS_window = Tk()
    line = Label(FOS_window, text="Enter Velocity in m/s")
    line.grid()
    vel = Entry(FOS_window)
    vel.grid()
    FOS_window.mainloop()

def EXIT_click():
    quit()


root = Tk()

SS_button = Button(root, text="Shell Statistics", command=SS_click)
FOS_button = Button(root, text="Calculate Angle", command=FOS_click)
EXIT_button = Button(root, text="OFF", command=EXIT_click)

SS_button.grid(row=0, column=0)
FOS_button.grid(row=0, column=1)
EXIT_button.grid(row=0, column=2)

root.mainloop()