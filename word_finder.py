def search(x,y):
    x = x.split(' ')
    if y in x:
        return("Word found")
    else:
        return("Word not found")

print("Insert a text:")    
text = str(input())
print("Word to search:")
word = str(input())

print(search(text, word))


