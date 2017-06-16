#!/usr/bin/python
# coding=utf-8

# 好吧，运算符

a = 21
b = 10
c = 0
print "a: ", a
print "b: ", b

c = a + b
print "a + b = ",
print c

c = a - b
print "\na - b = ",
print c

c = a * b
print "\na * b = ",
print c

c = a / b
print "\na / b = ",
print c

c = a % b
print "\na % b = ",
print c

# 修改变量
print "\n----"
a = 2
b = 3
c = a**b
print "a: ", a
print "b: ", b
print "a ** b = ",
print c

print "\n----"
a = 9
b = 2
c = a // b
print "a: ", a
print "b: ", b
print "a // b = ",
print c


print "\n\n---- 比较运算符 ----"
a = 21
b = 10
c

if a == b:
    print "1. a == b"
else:
    print "1. a != b"

if a != b:
    print "2. a != b"
else:
    print "2. a == b"

if a <> b:
    print "3. a <> b"
else:
    print "3. a == b"

if a < b:
    print "4. a < b"
else:
    print "4. a > b"

if a > b:
    print "5. a > b"
else:
    print "5. a < b"


a = 5
b = 20
print "\n\na: ", a
print "b: ", b

if a <= b:
    print "6. a <= b"
else:
    print "6. a > b"

if b >= a:
    print "7. b >= a"
else:
    print "7. b < a"


print "\n\n---- 赋值运算符 ----"
a = 21
b = 10
c = 0
c = a + b
print "c = a + b = ", c

c += a
print "c += a = ", c

c *= a
print "c *= a = ", c

c /= a
print "c /= a = ", c

c = 2
print "c = ", c
c %= a
print "c %= a = ", c

print "c: ", c
print "a: ", a
c **= a
print "c **= a = ", c

c //= a
print "c //= a = ", c


print "\n\n---- 位运算符 ----"
a = 60
b = 13
c = 0
print "a: %10s" % (bin(a))
print "b: %10s" % (bin(b))
print "----"

c = a & b
print "c: %10s" % bin(c),
print " c = a & b"

c = a | b
print "c: %10s" % bin(c),
print " c = a | b"

c = a ^ b
print "c: %10s" % bin(c),
print " c = a ^ b"

c = ~a
print "c: %10s" % bin(c),
print " c = ~a"

c = a << 2
print "c: %10s" % bin(c),
print " c = a << 2"

c = a >> 2
print "c: %10s" % bin(c),
print " c = a >> 2"


print "\n\n---- 逻辑运算符 ----"
a = 10
b = 20

if a and b:
    print "1. a and b are true"
else:
    print "1. a or b is false"

if a or b:
    print "2. a or b is ture"
else:
    print "2. a and b are false"

print "---- a = 0"
a = 0
if a and b:
    print "3. a and b are ture"
else:
    print "3. a or b is false"

if a or b:
    print "4. a or b is ture"
else:
    print "4. a and b are false"

if not a and b:
    print "5. a or b is false"
else:
    print "5. a and b are ture"


print "\n\n---- 成员运算符 ----"
a = 10
b = 20
list = [1, 2, 3, 4, 5]

if a in list:
    print "1. a is in the list"
else:
    print "1. a is not in the list"

if b in list:
    print "2. b is in the list"
else:
    print "2. b is not in the list"

print "---- a = 2"
a = 2
if a in list:
    print "3. a is in the list"
else:
    print "3. a is not in the list"


print "\n\n---- 身份运算符 ----"
a = 20
b = 20

if a is b:
    print "1. a and b have same identifier"
else:
    print "1. a and b dont have same identifier"

if a is not b:
    print "2. a and b dont have same identifier"
else:
    print "2. a and b have same identifier"

print "b = 30"
b = 30

if a is b:
    print "3. a and b have same identifier"
else:
    print "3. a and b dont have same identifier"

if a is not b:
    print "4. a and b dont have same identifier"
else:
    print "4. a and b have same identifier"


print "\n\n---- 运算符优先级 ----"
a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d
print "e = (a + b) * c / d = ", e

e = ((a + b) * c) / d
print "e = ((a + b) * c) / d = ", e

e = (a + b) * (c / d)
print "e = (a + b) * (c / d) = ", e

e = a + (b * c) / d
print "e = a + (b * c) / d = ", e
