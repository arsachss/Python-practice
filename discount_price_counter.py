print("Enter the discount value.")
discount = int(input())
cart = [15, 42, 120, 9, 5, 380]
total = 0

for C in cart:
    newC = C - (C*discount/100)
    total = total + newC
print(total)

"""
7.5
21
60
4.5
2.5
190
for discount 50% total 285.5
"""
