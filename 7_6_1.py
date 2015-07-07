ref = {}

def init():
    f = open('object.txt', 'r')
    while True:
        line = f.readline()
        if line == "":
            break
        name, quantity = line.split()
        ref[name] = int(quantity)
    f.close()

def add():
    name = raw_input()
    quantity = input()
    if name in ref:
        ref[name] += quantity
    else:
        ref[name] = quantity
def delete():
    name = raw_input()
    quantity = input()
    if name in ref:
        if ref[name] < quantity:
            print "Error!"
        elif ref[name] == quantity:
            del ref[name]
        else:
            ref[name] -= quantity
    else:
        print "Not exist"
def check():
    print ref.items()



print "1.Add 2.Delete 3.Check 4.Save and Quit"

while True:

    init()

    a = input()

    if a == 1:
        add()
    elif a == 2:
        delete()
    elif a == 3:
        check()
    elif a == 4:
        f = open('object.txt', 'w')

        output = ""
        for a in ref:
            output += a
            output += " "
            output += str(ref[a])
            output += "\n"
        f.write(str(output))
        f.close()
        break

f.close()