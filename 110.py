# Using the Names.txt file you created earlier, display the list of names in Python. Ask the user to type in one of the names and then
# save all the names except the one they entered into a new file called Names2.txt.
f = open('Names.txt', 'r')
print(f.read())
f.close
f = open('Names.txt', 'r')
name = input('Enter a name to remove: ') + '\n'
for row in f:
    if row != name:
        file = open ('Names2.txt', 'a')
        file.write(row)
        file.close

f.close