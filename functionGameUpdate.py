1.Cong
2.tru
3.nhan

2 3






import random

score = 1

def score1(status):
    print "================="
    if status == 0:
        print "Ket qua dung"
    else:
        print "Ket qua sai"

    print "================="

while True:

    x = random.randint(1,5)
    y = random.randint(2,10)

    if score == 0:
        print "Het diem. Ban da thua"
        break

    print "Diem: " + str(score)

    print "---------------"
    print str(x) + " + " + str(y) + " = "

    list = [0,0]

    j = random.randint(0,1)

    right = x + y

    list[j] = right

    for i in range(len(list)):
        if j != i:
                list[i] = random.randint(1,14)
                if list[i] == right:
                    list[i] = random.randint(1,14)

    print "---------------"

    # for i in range(len(list)):
    #     if i == 0:
    #         print "A" + ". " + str(list[i])
    #         if i == position:
    #             rightchoice = "A"
    #     else:
    #         print "B" + ". " + str(list[i])
    #         if i == position:
    #             rightchoice = "B"

    for i in range(len((list))):
        if i == 0:
            print "A" + ". " + str(list[i])
            if i == j:
                rightchoice = "A"
        else:
            print "B" + ". " + str(list[i])
            if i == j:
                rightchoice = "B"
    break

    print "----------------"
    choice = raw_input("Ket qua dung la: ")

    if choice == rightchoice:
        score = score + 1
        score1(0)

    else:
        score = score - 1
        score1(1)

