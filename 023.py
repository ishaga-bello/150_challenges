# Ask the user to type in the first line of a nursery rhyme and
# display the length of the string.Ask for a starting number and an
# ending number and then displayjust that section of the text
# (remember Python startscounting from 0 and not 1)

line = input("nursery rhyme: ")
print(len(line) ,"\n")

startNb = int(input("starting number: "))
endNb = int(input("ending number: "))

print (line[startNb-1:endNb])
