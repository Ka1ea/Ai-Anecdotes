from typing import List
import random

chorus = "have you \never wondered why \ndisney tales \nare end in \nlies"
chorusL = list(chorus.split("\n"))

random_part1 = random.randint(0,len(chorusL))
random_part2 = random.randint(0,len(chorusL))
while random_part1 == random_part2:
    random_part2 = random.randint(0,len(chorusL))
random_part3 = random.randint(0,len(chorusL))
while random_part3 == random_part2 or random_part3 == random_part1:
    random_part3 = random.randint(0,len(chorusL))
print(str(random_part3))
print(str(random_part1))
print(str(random_part2))


