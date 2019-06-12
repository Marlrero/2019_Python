import random

myList = [ "head", "tail" ]

while True:
    response = input("동전 던지기 계속? (yes, no) >> ")
    if response == 'yes':
        coin = random.choice(myList)
        print(coin)
    else:
        break