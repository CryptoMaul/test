from random import *

deck = ["A", "A", "2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]
list = sample(deck, 20)

sum = 0
total = 0
mean = 0
faceProp = 0

for i in list:
    if i.isnumeric():
        sum += int(i)
    elif i == "A":
        sum += 1
    else:
        sum += 10
        total += 1

mean = sum / 20
faceProp = total / 20

print("{ " + str(mean) + "  |  " + str(faceProp) + " }")