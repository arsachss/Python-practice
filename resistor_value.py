colors = ["black", "brown", "red", "orange", "yellow", "green", "blue",
          "violet", "grey", "white"]
print(colors)

n = colors.index(input("\nEnter the 1st color: ").lower())
m = colors.index(input("Enter the 2nd color: ").lower())
p = colors.index(input("Enter the 3rd color: ").lower())

q = ((n*10)+m)*(10**p)
r = q/1000

print("\nThe resistor value is: ")
print(f"{q}Ω")
print("OR")
print(f"{r}kΩ")
