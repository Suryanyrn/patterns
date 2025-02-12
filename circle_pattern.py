import math

r = int(input("Enter radius: "))  # Radius of the circle
diameter = 2 * r + 1  # To fit the circle properly

for i in range(diameter):
    for j in range(diameter):
        # Distance from the center
        distance = math.sqrt((i - r) ** 2 + (j - r) ** 2)
        
        # Print '*' only for boundary points
        if r - 0.4 <= distance <= r + 0.4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
