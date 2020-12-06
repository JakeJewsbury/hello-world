print('How many cats do you have?')
cats = input()
try:
    if int(cats) < 0:
        print('Enter a whole number please')
    elif int(cats) > 4:
        print('Wow you have a fuck ton of cats')
    else:
        print('You have 1-3 cats lol')
except:
    print('numbers dumbass')
