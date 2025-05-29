word = input("so'zni kiriting: ")
a = word.ljust(15, "0")
print(a)

word = input("sozni kiriting: ")
uzunlik = 15
abdurauf = len(word)
a = "0"*(uzunlik-abdurauf)
print(f"{a}{word}")