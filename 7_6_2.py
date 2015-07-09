sub = {}
UserList = []
list = []

def init():
    f = open('subject.txt', 'r')
    while True:
        line = f.readline()
        if line == "":
            break
        name, code = line.split()
        sub[name] = int(code)
    f.close()

    f = open('user.txt', 'r')
    while True:
        line = f.readline()
        if line == "":
            break
        list = (line.split())
        UserList.append(list)
    f.close()

def PrintList():
    print sub.items()
    print UserList

def Add():
    print "who?"
    user = raw_input()
    i = 0
    j = 0
    while i < UserList.__len__:
         if UserList[i][0] == user:
            j = 1
            break
         i = i + 1
    if j == 0:
        print ("Not exist")
    print "code?"
    code = raw_input()
    k = 1
    j = 0
    while k < UserList[i].__len__():
         if UserList[i][k] == code:
            print "Already exist"
            j = 1
            break
         k = k + 1
    if j == 0:
        UserList[i].append(code)

def Delete():
    print "who?"
    user = raw_input()
    i = 0
    j = 0
    while i < UserList.__len__():
         if UserList[i][0] == user:
            j = 1
            break
         i = i + 1
    if j == 0:
        print ("Not exist")

    print "code?"
    code = raw_input()
    k = 1
    j = 0
    while k < UserList[i].__len__():
         if UserList[i][k] == code:
            del UserList[i][k]
            j = 1
            break
         k = k + 1
    if j == 0:
        print "Not exist"

def Check():
    print "User name: "
    user = raw_input()
    i = 0
    j = 0
    while i < UserList.__len__():
        if UserList[i][0] == user:
            print UserList[i]
            j = 1
            break
        i = i + 1
    if j == 0:
        print ("Not exist")

init()
PrintList()

while True:
    print "1. Print list 2. Add 3. Delete 4. Check 5. Exit"
    a = input()

    if a == 1:
        PrintList()
    elif a == 2:
        Add()
    elif a == 3:
        Delete()
    elif a == 4:
        Check()
    elif a == 5:
        break