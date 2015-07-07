ref = {}

print "1.Add 2.Delete 3.Check"

while True:

    a = input()

    if a == 1:
        b = raw_input()
        c = input()
        if b in ref:
            ref[b] += c
        else:
            ref[b] = c
    elif a == 2:
        d = raw_input()
        e = input()
        if d in ref:
            if ref[d] < e:
                print "Error!"
            elif ref[d] == e:
                del ref[d]
            else:
                ref[d] -= e
        else:
            print "Not exist"
    elif a == 3:
        print ref.items()
    else:
        break
