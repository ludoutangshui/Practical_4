import random

MINIMUM = 1
MAXIMUM = 45
numbers = []

picks_times = int(input("How many quick picks? "))

for o in range(picks_times):
    for i in range(6):
        numbers.append(str(random.randint(MINIMUM, MAXIMUM)))
    print(format(" ".join(numbers)))
    numbers.clear()


