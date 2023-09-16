string = "Hello I am a Computer"
words = string.split(" ")
print(words)
for i in words:
    print(i[::-1],end = " ")