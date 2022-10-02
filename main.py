import random
print ("Hello this is a dice simulator")
goes = int(input("How many goes do you want to have?"))
counter = 0
throw_count = 1
dice = ["1", "2", "3", "4", "5", "6"]
while goes != counter:
    computer_action = random.choice(dice)
    print (throw_count, ":  ", computer_action)
    counter = counter + 1
    throw_count = throw_count + 1
