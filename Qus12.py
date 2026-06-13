"""2. Ask the user to input a color (red, yellow, green). Print:
 Red → Stop
 Yellow → Ready
 Green → Go
 Otherwise → Invalid color"""

Colour = input("Enter any colour :")

if "Red" in Colour:
    print("Stop")
elif "Yellow" in Colour:
    print("Ready")
elif "Green" in Colour:
    print("Go")
else:
    print("Invalid colour")