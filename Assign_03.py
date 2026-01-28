# a) Develop a Python program that takes a voltage (V) and resistance (R) as inputs from the user and calculates the
# current (I) using Ohm’s Law.
# b) Modify the above program to display the nature of current:
# If current < 0.5 A, print “Low current”
# If 0.5 A ≤ current ≤ 2 A, print “Normal current”
# If current > 2 A, print “High current

# Ohm’s Law Program
# Formula: I = V / R

# Take input from user
V = float(input("Enter voltage (V): "))
R = float(input("Enter resistance (R): "))

# Calculate current
I = V / R

# Print current value
print("Current =", I, "Ampere")

# Check the nature of current
if I < 0.5:
    print("Low current")
elif I >= 0.5 and I <= 2:
    print("Normal current")
else:
    print("High current")