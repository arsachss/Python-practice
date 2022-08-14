def search(x,y):
    x = x.upper()
    x = x.split(' ')
    y = y.upper()
    if y in x:
        return("Word found")
    else:
        return("Word not found")

print("Insert a text:")    
text = str(input())
print("Word to search:")
word = str(input())

print(search(text, word))


