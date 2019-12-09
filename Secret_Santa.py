import random
import subprocess
import time
random.seed(time.time())

names = []
name = input("Enter a name: ")
while name != "":
    names.append(name)
    name = input("Enter a name: ")
random.shuffle(names)
givers = names.copy()
getters = names.copy()
buddies = names.copy()
getters = getters[1:] + [getters[0]]
buddies = buddies[2:] + [buddies[0],buddies[1]]

tmp = subprocess.call("clear", shell=True)
for name in givers:
    print(str(givers.index(name)) + ":  " + name)
sel = input("Enter you number: ")
while sel != '':
    tmp = subprocess.call("clear", shell=True)
    print(str(givers[int(sel)]) + "'s Secret Santa assignment: ")
    print(getters[int(sel)])   
    print("\nYour Buddy is: ")
    print(buddies[int(sel)])
    time.sleep(5)
    tmp = subprocess.call("clear", shell=True)
    for name in givers:
        print(str(givers.index(name)) + ":  " + name)
    sel = input("Enter you number: ")
exit()


### RANDOM BRUTE FORCE ###
### GET NAMES ###
names = []
name = input("Enter a name: ")
while name != "":
    names.append(name)
    name = input("Enter a name: ")

### ASSIGN PEOPLE ###
givers = names.copy()
getters = names.copy()
while (not all(givers[i] != getters[i] for i in range(len(names))) or  
        not all(getters[givers.index(name)] != givers[getters.index(name)] for name in names)):
    random.shuffle(getters)

### Assign Buddy ### 
buddies = names.copy()
while (not all(buddies[i] == buddies[givers.index(buddies[i])] for i in range(len(names))) or 
       not all(buddies[i] != getters[i] for i in range(len(names))) or 
       not all(buddies[i] != givers[i] for i in range(len(names)))):
    random.shuffle(buddies)

print(givers)
print(getters)
print(buddies)
exit()
### GIVE ASSIGNMENT ###
tmp = subprocess.call("clear", shell=True)
for name in givers:
    print(str(givers.index(name)) + ":  " + name)
sel = input("Enter you number: ")
while sel != '':
    tmp = subprocess.call("clear", shell=True)
    print(str(givers[int(sel)]) + "'s Secret Santa assignment: ")
    print(getters[int(sel)])   
    time.sleep(3)
    tmp = subprocess.call("clear", shell=True)
    for name in givers:
        print(str(givers.index(name)) + ":  " + name)
    sel = input("Enter you number: ")

