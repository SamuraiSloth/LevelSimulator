import math

#introduces variables
level = input("What level do you want to be: ")
level = int(level)
hp = 100
strength = 20
defence = 20
magicalstrength = 20
magicaldefence = 20
mp = 20
speed = 10
x = 0
i = level
i = math.ceil(i/100)
y = 0

#calculates stats
while i != 0:
  x += 1
  if x == 1:
    y = 1
  else:
    y = 100 * (x - 1)
  if level > (100 * x):
    hp += (100 * x - y) * x * x
  else:
    hp += (level - y) * x * x
  i -= 1
x = 0
i = level
i = math.ceil(i/100)
y = 0
while i != 0:
  x += 1
  if x == 1:
    y = 1
  else:
    y = 100 * (x - 1)
  if level > (100 * x):
    strength += math.ceil(((100 * x - y) * x * x) / 5)
  else:
    strength += math.ceil(((level - y) * x * x) / 5)
  i -= 1
x = 0
i = level
i = math.ceil(i/100)
y = 0
while i != 0:
  x += 1
  if x == 1:
    y = 1
  else:
    y = 100 * (x - 1)
  if level > (100 * x):
    defence += math.ceil(((100 * x - y) * x * x) / 5)
  else:
    defence += math.ceil(((level - y) * x * x) / 5)
  i -= 1
x = 0
i = level
i = math.ceil(i/100)
y = 0
while i != 0:
  x += 1
  if x == 1:
    y = 1
  else:
    y = 100 * (x - 1)
  if level > (100 * x):
    magicalstrength += math.ceil(((100 * x - y) * x * x) / 5)
  else:
    magicalstrength += math.ceil(((level - y) * x * x) / 5)
  i -= 1
x = 0
i = level
i = math.ceil(i/100)
y = 0
while i != 0:
  x += 1
  if x == 1:
    y = 1
  else:
    y = 100 * (x - 1)
  if level > (100 * x):
    magicaldefence += math.ceil(((100 * x - y) * x * x) / 5)
  else:
    magicaldefence += math.ceil(((level - y) * x * x) / 5)
  i -= 1
x = 0
i = level
i = math.ceil(i/100)
y = 0
while i != 0:
  x += 1
  if x == 1:
    y = 1
  else:
    y = 100 * (x - 1)
  if level > (100 * x):
    mp += math.ceil(((100 * x - y) * x * x) / 5)
  else:
    mp += math.ceil(((level - y) * x * x) / 5)
  i -= 1
x = 0
i = level
i = math.ceil(i/100)
y = 0
while i != 0:
  x += 1
  if x == 1:
    y = 1
  else:
    y = 100 * (x - 1)
  if level > (100 * x):
    speed += math.ceil(((100 * x - y) * x * x) / 10)
  else:
    speed += math.ceil(((level - y) * x * x) / 10)
  i -= 1

#states stats
print("Your stats are")
print("hp: " + str(hp))
print("strength: " + str(strength))
print("defence: " + str(defence))
print("magicalstrength: " + str(magicalstrength))
print("magicaldefence: " + str(magicaldefence))
print("mp: " + str(mp))
print("speed: " + str(speed))
