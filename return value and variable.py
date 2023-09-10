# ask the name of the user
name=input("what's your name? ").strip().title()
# removing space
#name = name.strip()
# capitalize the later the first name first letter
#name = name.capitalize()
# capitalize the first letter the text
#name = name.title()
# to capitalize and removing white space
#name = name.strip().title()
first , last = name.split(" ")

# say hello to the user
print("hello,", first)