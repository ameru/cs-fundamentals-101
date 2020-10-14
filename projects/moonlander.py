def main() -> None:
    gravity = 1.62
    time = 0
#    fuel_rate = 0
#    acceleration = 0
    show_welcome()
    altitude = get_altitude()
    fuel = get_fuel()
    fuel_rate = get_fuel_rate(fuel)
    ml = Moonlander(altitude, fuel)
    ml.fuel = update_fuel(fuel, fuel_rate)
    ml.acceleration = update_acceleration(gravity, fuel_rate)
    ml.altitude = update_altitude(ml.altitude, ml.velocity, ml.acceleration)
    display_state(time, ml.altitude, ml.velocity, ml.fuel, fuel_rate)
    while ml.fuel > 0 and ml.altitude > 0.00:
        fuel_rate = get_fuel_rate(ml.fuel)
        ml.fuel = update_fuel(ml.fuel, fuel_rate)
        ml.altitude = update_altitude(ml.altitude, ml.velocity, ml.acceleration)
        ml.velocity = update_velocity(ml.velocity, ml.acceleration)
        display_state(time, ml.altitude, ml.velocity, ml.fuel, fuel_rate)
        time += 1
        if ml.fuel == 0:
            fuel_rate = 0
            time -= 1
            while ml.altitude > 0.00:
                time += 1
                display_state(time, ml.altitude, ml.velocity, ml.fuel, fuel_rate)
                ml.fuel = update_fuel(ml.fuel, fuel_rate)
                ml.acceleration = update_acceleration(gravity, fuel_rate)
                ml.altitude = update_altitude(ml.altitude, ml.velocity, ml.acceleration)
                ml.velocity = update_velocity(ml.velocity, ml.acceleration)
            time += 1
    display_landing_status(ml.velocity)

class Moonlander:
    """Moonlander
    Attributes:
    altitude (float): the distance from the surface of the moon.
    fuel (int): the fuel
    velocity (float): It is positive when the Moonlander is
    moving away from the moon.
    acceleration (float):  It is positive when the Moonlander is
    moving away from the moon.
    """
    def __init__(self, alt, fuel):
        self.altitude = alt
        self.fuel = fuel
        self.velocity = 0.00

def show_welcome() -> None:
    """ Shows welcome message.
    Arguments:
        None
    Returns:
        None: printed statement for LM
    """
    print("Welcome to the Moon Lander Simulation!")

def get_altitude() -> float:
    """ Receives user input for the altitude constraints of the LM.
    Arguments:
        None
    Returns:
        float: value of altitude from user input
    """    
    altitude = float(input("Please enter initial altitude [1, 9999]: "))
    while (altitude < 1) or (altitude > 9999):
        print("[ERROR] Altitude out of range")
        altitude = float(input("Please enter initial altitude [1, 9999]: "))
    return altitude

def get_fuel() -> int:
    """ Receives user input for the fuel constraints of the LM.
    Arguments:
        None
    Returns:
        float: amount of fuel from user input
    """    
    fuel = int(input("Please enter initial fuel amount" +
        "[a positive number]: "))
    while fuel < 0:
        print("[ERROR] Fuel amount must be positive")
        fuel = int(input("Please enter initial fuel amount" +
        "[a positive number]: "))
    return fuel

def display_state(time: int, altitude: float, velocity: float, \
    fuel: int, fuel_rate: int) -> None:
    """ Displays the time passed, altitude, velocity, fuel, and fuel rate
    Arguments:
        time (int): time elapsed since the LM has launched
        altitude (float): altitude of the LM
        velocity (float): velocity of the LM
        fuel (int): amount of fuel LM has left
        fuel_rate (int): fuel rate at which LM is operating
    Returns:
        None: LM display state stats
    """    
    print("time = %d, altitude = %.2f, " % (time, altitude), end = "")
    print("velocity = %.2f, fuel = %d, " % (velocity, fuel), end = "")
    print("fuel rate = %d" % (fuel_rate))

def get_fuel_rate(fuel: int) -> int:
    """ Prompts the user for an integer in the interval [0,9]
    Arguments:
        fuel (int): amount of fuel left on the LM
    Returns:
        int: return value of amount of fuel remaining on LM
    """   
    fuel_rate = int(input("Enter fuel rate in interval [0,9]: "))
    while (fuel_rate < 0) or (fuel_rate > 9):
        print("[ERROR] Fuel rate out of range")
        fuel_rate = int(input("Enter fuel rate in interval [0,9]: "))
    if fuel_rate > fuel:
        return fuel
    else:
        return fuel_rate 

def display_landing_status(velocity: float) -> None:
    """ Displays status of LM upon impact
    Arguments:
        velocity (float): speed at which LM is operating at impact
    Returns:
        float: LM display state stats at time of impact
    """    
    if (velocity > -1) and (velocity < 0):
        print("The Eagle has landed!")
    elif (velocity > -10) and (velocity < -1):
        print("Enjoy your oxygen while it lasts!")
    else:
        print("Ouch - that hurt!")

def update_acceleration(gravity: float, fuel_rate: int) -> float:
    """ updates acceleration stats of LM
    Arguments:
        gravity (float): gravity at which LM is at
        fuel_rate (int): fuel rate of LM
    Returns:
        float: returns new acceleration based on the inputs of given formula
    """    
    return 1.62 * ((fuel_rate/5) - 1)

def update_altitude(altitude: float, velocity: float, \
    acceleration: float) -> float:
    """ updates altitude stats of LM
    Arguments:
        altitude (float): altitude at which LM is at
        velocity (float): velocity at which LM is at
        acceleration (float): acceleration constant for LM
    Returns:
        float: returns new altitude based on the inputs of given formula
    """
    return altitude + velocity + (acceleration/2)

def update_velocity(velocity: float, acceleration: float) -> float:
    """ updates velocity stats of LM
    Arguments:
        velocity (float): velocity at which LM is at
        acceleration (float): acceleration constant for LM
    Returns:
        float: returns new velocity based on the inputs of given formula
    """    
    return velocity + acceleration

def update_fuel(fuel: int, fuel_rate: int) -> int:
    """ updates fuel stats of LM
    Arguments:
        fuel (int): amount of fuel left in LM
        fuel_rate (int): fuel rate of LM
    Returns:
        float: returns new fuel amount based on the inputs of given formula
    """    
    if fuel_rate <= fuel:
        return fuel - fuel_rate
    else:
        return 0

if __name__ == "__main__":
    main()
