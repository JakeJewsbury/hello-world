def statue(word):
    print('"' +word+'"'+' has ' + str(len(word)) + ' letters in it')
def ask():
    print('Tpye what word you would like to know the charcter count of')
    word = input()
    statue(word)
while True:
    ask()
