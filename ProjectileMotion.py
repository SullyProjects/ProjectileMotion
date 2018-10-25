import math as m


def home_screen():
    print("{:^15s}{:^15s}{:^10s}".format("Shell Stats", "Fire Comp.", "OFF"))
    print("{:^15s}{:^15s}{:^10s}".format("(   1   )", "(   2   )", "(   3   )"))
    choice = int(input())
    return choice


def calc_shell_stats():
    BP = int(input("Input powder mass (kg):"))
    Proj_mass = int(input("Input shell mass (kg):"))

    Vel = (1500 * m.pow((BP/Proj_mass), 0.45))

    return round(Vel, 2)


def calc_fos():
    G = 9.81

    velocity = int(input("Enter predicted shell velocity (m/s):"))
    distance = int(input("Enter desired range of projectile (m):"))

    angle = (0.5 * m.asin((G * distance) / (m.pow(velocity, 2))))
    angle_deg = m.degrees(angle)
    return round(angle_deg, 2)


def calc_fos_vel(vel):
    G = 9.81

    print("Calculated velocity: ", vel, "m/s")
    distance = int(input("Enter desired range of projectile (m):"))

    angle = (0.5 * m.asin((G * distance) / (m.pow(vel, 2))))
    angle_deg = m.degrees(angle)
    return round(angle_deg, 2)


def main():
    choice = 0

    while choice != 3:
        choice = home_screen()
        print()
        if choice == 1:
            save_vel = " "
            saved_velocity = calc_shell_stats()
            print(saved_velocity, "m/s")
            print()
            while save_vel.lower != "y" and save_vel.lower() != "n":
                save_vel = input("Would you like to save Velocity? (Y)(N)")
                if save_vel.lower() != "y" and save_vel.lower() != "n":
                    print("Not a correct input. Try again.")
                else:
                    print()
                    break

        if choice == 2:
            try:
                if save_vel.lower() == "y":

                    print(calc_fos_vel(saved_velocity), "Degrees")
                if save_vel.lower() == "n":
                    print(calc_fos(), "Degrees")
                    print()

            except UnboundLocalError:
                print(calc_fos(), "Degrees")
                print()

        if choice == 3:
            print("Quitting")
            break


if __name__ == '__main__':
    main()
