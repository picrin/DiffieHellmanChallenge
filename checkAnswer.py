import sys

exponentiation = int(sys.argv[2])
toDo = []

filenameWithPrime = sys.argv[1]
with open(filenameWithPrime, "r") as f:
    p = int(f.readlines()[0])

g = 101


while exponentiation != 1:
    if exponentiation % 2 == 0:
        exponentiation /= 2
        toDo.append("s")
    else:
        exponentiation -= 1
        toDo.append("m")

toDo = toDo[::-1]
currentNumber = g
for operation in toDo:
    if operation == "s":
        currentNumber = (currentNumber + currentNumber) % p
    if operation == "m":
        currentNumber = (currentNumber + g) % p
print currentNumber
