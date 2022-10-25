letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def getData():
    word = input('Enter a message: ')
    word = word.lower()
    num = int(input('ENter a number (1-26): '))
    if num > 26 or num == 0:
        while num > 26 or num == 0:
            num = int(input('out of range please try again: '))
    data = (word,num)
    return data


def code(word, num):
    for x in word:
        new = ''
        y = letter.index(x)
        y = y + num
        if y > 25:
            y = y - 26
        char = letter[y]
        new += char
    print(new)

def decode(word,num):
    for x in word:
        new = ''
        y = letter.index(x)
        y = y - num
        if y < 0:
            y = y + 27
        char = letter[y]
        new += char
        print(new)


def main():
    while select != 3:
        print('1) Make a code: ')
        print('2) Decode a message: ')
        print('3) Quit')
        print()
        select = input('Enter your selection: ')
        if select == 1:
            (word,num) = getData()
            code(word,num)
        if select == 2:
            (word,num) = getData()
            decode(word,num)
        else:
            select = input('Enter your selection (1-3): ')
