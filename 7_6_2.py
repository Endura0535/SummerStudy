sub = {}
a = []
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



    f.close()

def check():
    print sub.items()
    print a

def application():
    print "who?"
    user = raw_input()
    print "code?"
    list = input()

init()
check()
