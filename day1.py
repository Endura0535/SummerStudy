# -*- coding:utf-8 -*-

a = raw_input()
b = input()
c = raw_input()
d = input()
e = raw_input()
f = input()

print a + ": " + str(b)
print c + ": " + str(d)
print e + ": " + str(f)

g = b + d + f

e = float(g)/float(3)

print "total sum: " + str(g)
print "average: " + str("%0.3f" % e)

