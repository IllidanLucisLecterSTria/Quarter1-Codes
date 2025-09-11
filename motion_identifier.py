def convert_velocity(value, unit):
    if unit == "ft/s":
        return value * 0.3048
    elif unit == "km/s":
        return value * 1000
    elif unit == "mi/s":
        return value * 1609.34
    else:
        return value
def convert_acceleration(value, unit):
    if unit == "ft/s²":
        return value * 0.3048
    elif unit == "km/s²":
        return value * 1000
    elif unit == "mi/s²":
        return value * 1609.34
    else:
        return value
def motion_type(v, a):
    if v > 0 and a == 0:
        return "Uniform Motion"
    elif v > 0 and a > 0:
        return "Accelerated Motion"
    elif v > 0 and a < 0:
        return "Decelerated Motion"
    else:
        return "At Rest"
v_value = float(input("Enter velocity value: "))
v_unit = input("Enter velocity unit (m/s, ft/s, km/s, mi/s): ")
a_value = float(input("Enter acceleration value: "))
a_unit = input("Enter acceleration unit (m/s², ft/s², km/s², mi/s²): ")
v_si = convert_velocity(v_value, v_unit)
a_si = convert_acceleration(a_value, a_unit)
motion = motion_type(v_si, a_si)
print("\n--- Results ---")
print(f"Velocity = {v_si:.3f} m/s")
print(f"Acceleration = {a_si:.3f} m/s²")
print(f"Motion Type = {motion}")
