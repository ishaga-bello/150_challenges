# Create a new file called “Names.txt”. Add five names to the document, which are stored on separate lines. Once you have
# run the program, look in the location where your program is stored and check that the file has been created properly.


f = open('Names.txt', 'w')
f.write('Bello\n')
f.write('Sam\n')
name = 'Jimmy' + '\n'
f.write(name)
f.write('Orelsan\n')
f.write('Dinos\n')
f.close