import random
import subprocess
import time
random.seed(time.time())

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

