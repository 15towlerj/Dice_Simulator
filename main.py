import random
print ("Hello this is a dice simulator")
play=1
counter = 0
throw_count = 1
while play == 1:
    goes = int(input("How many goes do you want to have?"))
    dice = ["1", "2", "3", "4", "5", "6"]
    while goes != counter:
        computer_action = random.choice(dice)
        print (throw_count, ":  ", computer_action)
        counter = counter + 1
        throw_count = throw_count + 1
    play = int(input("Would you like to play again? Press 1 for yes and 0 for no."))
    if (play == 1):
        counter = 0
        throw_count = 1
    else:
        print ("Thank you for playing!")
