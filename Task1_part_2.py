
zeros = 0
pointer = 50
with open("Task_1_input") as f:
    password = f.read().split()

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

print(zeros)