def vriska():
    print('Please enter your favorite three digit number')
    age = input()
    try:
        print('Your favorite number is ' + str(int(age))+'? That is so cool.....')
    except:
        print('Idiot. Do it again.')
        return vriska()
vriska()
