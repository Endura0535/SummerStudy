import random

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for j in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print str(i) + "*" + str(j) + "=" + str(i*j)

a = input();

for i in range(1, a+1):
    for j in range(1, 10):
        print str(i) + "*" + str(j) + "=" + str(i*j)

b = random.randrange(0, 10)
c = random.randrange(0, 10)
d = random.randrange(0, 10)

print str(b) + str(c) + str(d)



while True:
    if b == c:
        c = random.randrange(0, 10)
    else:
            if b == d:
                d = random.randrange(0, 10)
            else:
                if c == d:
                    d = random.randrange(0, 10)
                else:
                    break

print str(b) + str(c) + str(d)

while True:
    e = input()
    f = input()
    g = input()

    Ball = 0
    Strike = 0

    if e == b:
        Strike += 1
    if f == c:
        Strike += 1
    if g == d:
        Strike += 1

    if e == c or e == d:
        Ball += 1
    if f == b or f == d:
        Ball += 1
    if g == b or g == c:
        Ball += 1

    if Strike == 3:
        print "Clear!"
        break

    print str(Strike) + "Strike" + str(Ball) + "Ball"
