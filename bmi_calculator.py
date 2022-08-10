print("Enter your weight in kg unit.")
w = float(input())
print("Enter your height in meter unit.")
h = float(input())

z = w/(h*h)
print(z)

if z < 18.5:
    print("Underweight")
elif 18.5 <= z < 25:
    print("Normal")
elif 25 <= z < 30:
    print("Overweight")
elif z >= 30:
    print("Obesity")

