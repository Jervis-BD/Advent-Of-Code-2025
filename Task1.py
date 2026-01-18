
## Instead of only counting the amount of zeros that the dial stops on (ie that are part of the password)
## This counts every time the dial would pass the Zero meaning that you dont need as long of a sequence of inputs 
## I think thats more interesting as it forces simulation of the dial as it would work in real world
## Also instead of reading in a sequence of turns and then executing this generates its own
## The length of the sequence generated can be changed by exchanging the "6" in line 14 for a variable which is taken as input


import random
password =  random.sample(range(0, 99), 6)
print(password)
for num in range(0, len(password)):
    print(num)
    if random.randint(0,1) == 1:
        password[num] = "L" + str(password[num])
    else:
        password[num] = "R" + str(password[num])
print(password, "Is the secret password")

zeros = 0
pointer = 50

for num in range(0, len(password)):
    dir = password[num][0]
    turns = int(password[num][1:])

    L, R = False, False
    if dir == "L":
        L = True
    else:
        R = True

    for i in range(0, turns):
        if L and pointer > 0:
            pointer -= 1
        elif L and pointer == 0:
            pointer = 99
        elif R and pointer < 99:
            pointer += 1
        elif R and pointer == 99:
            pointer = 0
        if pointer == 0:
            zeros += 1

scrt = int(input("Input Password\n"))

if scrt == zeros:
    print("You got in!")