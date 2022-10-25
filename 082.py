# Show the user a line of text from your favourite poem and ask for a starting and ending point. Display the
# characters between those two points.

poem = 'Once upon a time a orning far away from town there has been this amzing person sitting on a bench chatting with the birds'
print(poem)
print(len(poem))
start = int(input('Start point: '))
end = int(input('End point: '))
print(poem[start:end])