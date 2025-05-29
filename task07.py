text = input("matnni kiriting: ")
Last_word = input("oxirigi so'zni kiriting: ")
last_word = len(Last_word)
new_text = text[-last_word:]
print(new_text==Last_word)