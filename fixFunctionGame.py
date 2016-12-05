import random
print random.randint(1,5)


print "Play random game"

while True:

    x = random.randint(1,5)
    y = random.randint(2,10)
    print str(x) + " + " + str(y) + " = "

    list = [0,0]

    position = random.randint(0,1)

    right = x + y

    list[position] = right

    for i in range(len(list)):
        if position != i:
                list[i] = random.randint(1,14)
                if list[i] == right:
                    list[i] = random.randint(1,14)

    print "--------------------------------"

    for i in range(len(list)):
        print str(i + 1) + ". " + str(list[i])

    choice = raw_input("Ket qua dung la: ")

    if choice == str(position + 1):
        print "Ket qua hoan toan dung"
    else:
        print "Ket qua sai"


