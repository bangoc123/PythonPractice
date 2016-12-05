import random

while True:
    x =  random.randint(0,5)

    y = random.randint(0,5)

    print "Tong cua " + str(x) + " + " + str(y) + " bang bao nhieu?"

    int("3")
    z = raw_input("")

    if z == str(x + y):
        print "Chinh xac"
    else:
        print "Khong chinh xac"
