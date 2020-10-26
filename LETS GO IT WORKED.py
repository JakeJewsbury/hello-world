def function(age):
    if age >= 18:
        print('Welcome to the club')
    elif age < 18:
        print('Maybe come back in ' + str(18 - yourAge) + ' years buddy')

print('Please enter your age')
yourAge = int(input())
function(yourAge)
