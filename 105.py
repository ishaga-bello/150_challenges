# Write a new file called “Numbers.txt”. Add five numbers to the document which are stored on the same lineand only
# separated by a comma. Once you have run the program, look in the location where your program is stored and you
# should see that the file has been created. The easiest way to view the contents of the new text file on a Windows
# system is to read it using Notepad.


f = open('Numbers.txt', 'w')
f.write('43, 53, 89, 34,75')
f.close