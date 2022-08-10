print("Enter a 2 words.")
input = str(input())
count = 0

for x in input:
    #replace x with any letter of your choice
    if(x == 'a' or x == 'A'):
        count+= 1
print(count)
