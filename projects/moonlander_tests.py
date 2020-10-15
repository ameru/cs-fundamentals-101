import moonlander

# testing update_acceleration(gravity: float, fuel_rate: int) -> float:
assert moonlander.update_acceleration(1.62, 10) == 1.62
assert moonlander.update_acceleration(1.62, 0) == -1.62
assert moonlander.update_acceleration(1.62, 5) == 0

# testing update_altitude(altitude: float, velocity: float, 
# acceleration: float) -> float:
assert moonlander.update_altitude(100.0, -50, 20) == 60
assert moonlander.update_altitude(0.0, -20.0, 100.0) == 30
assert moonlander.update_altitude(500.0, -30.0, 4.0) == 472

# testing update_velocity(velocity: float, acceleration: float) -> float:
assert moonlander.update_velocity(10, 30) == 40
assert moonlander.update_velocity(-20, 40) == 20
assert moonlander.update_velocity(30, 0) == 30

# testing update_fuel(fuel_amount: int, fuel_rate: int) -> int:
assert moonlander.update_fuel(100, 9) == 91
assert moonlander.update_fuel(0, 0) == 0
assert moonlander.update_fuel(20, 0) == 20
