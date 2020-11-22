from random import uniform
from math import pi, pow
try:
    lowBound: float = float(input("Please input a small decimal.\n"))
    highBound: float = float(input("Please input a larger decimal.\n"))

    if (lowBound > highBound) or (lowBound == highBound):
        raise Exception("highBound must be larger than lowBound")
    else:
        radius: float = uniform(lowBound, highBound)
        volume: float = (((4 / 3) * pi) * pow(radius, 3))
        print(f"The volume of a sphere with the radius: {radius} is {volume}")
except:
    print("Something went wrong while converting inputs to floats.")
