import math

#introduces variables
xp = input("How many EXP points do you want?: ")
xp = float(xp)
level = (math.floor(xp ** (1./2.25))) + 1
level = int(level)
hp = 100
strength = 20
defence = 20
magicalstrength = 20
magicaldefence = 20
mp = 20
speed = 10
specialstatuspoints = 0
x = 0
i = level
i = math.ceil(i/100)
y = 0
reply = ""
reply2 = 0

#calculates stats
while i != 0:
  x += 1
  if x == 1:
    y = 1
  else:
    y = 100 * (x - 1)
  if level > (100 * x):
    hp += (100 * x - y) * x * x * 2
  else:
    hp += (level - y) * x * x * 2
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
    strength += math.ceil(((100 * x - y) * x * x) / 5 * 2)
  else:
    strength += math.ceil(((level - y) * x * x) / 5 * 2)
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
    defence += math.ceil(((100 * x - y) * x * x) / 5 * 2)
  else:
    defence += math.ceil(((level - y) * x * x) / 5 * 2)
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
    magicalstrength += math.ceil(((100 * x - y) * x * x) / 5 * 2)
  else:
    magicalstrength += math.ceil(((level - y) * x * x) / 5 * 2)
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
    magicaldefence += math.ceil(((100 * x - y) * x * x) / 5 * 2)
  else:
    magicaldefence += math.ceil(((level - y) * x * x) / 5 * 2)
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
    mp += math.ceil(((100 * x - y) * x * x) / 5 * 2)
  else:
    mp += math.ceil(((level - y) * x * x) / 5 * 2)
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
    speed += math.ceil(((100 * x - y) * x * x) / 5)
  else:
    speed += math.ceil(((level - y) * x * x) / 5)
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
   specialstatuspoints += math.ceil(((100 * x - y) * x * x))
 else:
   specialstatuspoints += math.ceil(((level - y) * x * x))
 i -= 1

#states stats
print("Your stats are")
print("level: " + str(level))
print("hp: " + str(hp))
print("strength: " + str(strength))
print("defence: " + str(defence))
print("magicalstrength: " + str(magicalstrength))
print("magicaldefence: " + str(magicaldefence))
print("mp: " + str(mp))
print("speed: " + str(speed))
print("You have " + str(specialstatuspoints) + " status points you can use to upgrade any status you have!")

#calculates and prints status points
while specialstatuspoints != 0:
    reply = input("Which status would you like to upgrade?: ")
    reply2 = input("How many status points would you like to use?: ")
    reply2 = int(reply2)
    if str(reply) == "hp" and int(reply2) <= specialstatuspoints:
        hp += int(reply2)
        print("Your hp stat is now " + str(hp))
        specialstatuspoints -= reply2
        print("You now have " + str(specialstatuspoints) + " status points")
    if str(reply) == "strength" and int(reply2) <= specialstatuspoints:
        strength += int(reply2)
        print("Your strength stat is now " + zstr(strength))
        specialstatuspoints -= reply2
        print("You now have " + str(specialstatuspoints) + " status points")
    if str(reply) == "defence" and int(reply2) <= specialstatuspoints:
        defence += int(reply2)
        print("Your defence stat is now " + str(defence))
        specialstatuspoints -= reply2
        print("You now have " + str(specialstatuspoints) + " status points")
    if str(reply) == "magicalstrength" and int(reply2) <= specialstatuspoints:
        magicalstrength += int(reply2)
        print("Your magicalstrength stat is now " + str(magicalstrength))
        specialstatuspoints -= reply2
        print("You now have " + str(specialstatuspoints) + " status points")
    if str(reply) == "magicaldefence" and int(reply2) <= specialstatuspoints:
        magicaldefence += int(reply2)
        print("Your magicaldefence stat is now " + str(magicaldefence))
        specialstatuspoints -= reply2
        print("You now have " + str(specialstatuspoints) + " status points")
    if str(reply) == "mp" and int(reply2) <= specialstatuspoints:
        mp += int(reply2)
        print("Your mp stat is now " + str(mp))
        specialstatuspoints -= reply2
        print("You now have " + str(specialstatuspoints) + " status points")
    if str(reply) == "speed" and int(reply2) <= specialstatuspoints:
        speed += int(reply2)
        print("Your speed stat is now " + str(speed))
        specialstatuspoints -= reply2
        print("You now have " + str(specialstatuspoints) + " status points")
    elif int(reply2) > specialstatuspoints:
        print("You do not have enough status points to do this.")
