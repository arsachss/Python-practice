import pyshorteners
long_url = input("Enter the URL here.\n")

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print("The shortened URL: " + short_url)
