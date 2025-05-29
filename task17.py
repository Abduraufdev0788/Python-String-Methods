word = input("sozni kiriting: ")
uzunlik = 15
abdurauf = len(word)
a = "0"*(uzunlik-abdurauf)
print(f"{word}{a}")

word = input("so'zni kiriting: ")
a = word.rjust(15, "0")
print(a)
