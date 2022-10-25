# Open the Names.txt file. Ask the user to input a new name. Add this to the end of the file and display the entire file.


f = open('Names.txt', 'a')
name = input('Enter a new name: ') + '\n'
f.write(name)
f.close
f = open('Names.txt', 'r')
print(f.read())
f.close