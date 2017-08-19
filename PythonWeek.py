import random 
print "I am thinking of a number 1 - 10"

randomNumber = random.randint(1, 10)
counter = 5
print randomNumber

playerNum = int(raw_input("What is the number?"))

#while playerNum =! random_number

while True and counter > 0:
    if playerNum > randomNumber:
        print "You guessed too high"
        counter -= 1
        playerNum = int(raw_input("What is the number?"))
        print counter
    elif playerNum < randomNumber:
        counter -= 1
        print "you guessed too low"
        playerNum = int(raw_input("What is the number?"))
        print counter
    else:
        print "correct"
        break
