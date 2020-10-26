spam = 99
print('Spam = ' + str(spam)) #defining spam the global value of 99
def karkat():
    print('Please input a value')
    spam = int(input())
    print('This is Karkat spam value')
    print(spam)
karkat()
print('This is global spam value')
print(spam)
