#Royce Daniel, 3/6/2026, "Knowing the distance"
import math

def distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return dist

def main():
    try:
        print("Enter the first coordinate:")
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        z1 = float(input("z1: "))

        print("Enter the second coordinate:")
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        z2 = float(input("z2: "))
        point1 = (x1, y1, z1)
        point2 = (x2, y2, z2)
        dist = distance(point1, point2)
        print("The distance between the points is", dist)
        if dist >400:
            print("That's awful far")

    except ValueError:
        print("Invalid input. Only numbers are accepted >:(")

if __name__ == "__main__":
    main()