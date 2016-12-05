person1 = {"id":1,"name":"Ngoc", "password":"12345", "balance":1000}

person2 = {"id":2,"name":"Hoa", "password":"123", "balance":1000}

person3 = {"id":3,"name":"Quang", "password":"345","balance":100}


people = [person1, person2, person3]

def authenticate():
    isauthenticated = False
    while True:
        name = raw_input("Name: ")
        while True:
            checkUsername = False
            for person in people:
                if person["name"] == name:
                    checkUsername = True
                    password = raw_input("Password: ")
                    if person["password"] == password:
                        print "Found"
                        isauthenticated = True
                        currentUser = person
                        currentUserId = person["id"]
                        return(isauthenticated, currentUser, currentUserId)
                        break
                    else:
                        print "Mat khau sai"
            if not checkUsername:
                print "Khong ton tai username"
                break

            if isauthenticated:
                break
        if isauthenticated:
            break

def transfer(currentUser, currentUserId):
    for person in people:
        print "%i. %s"%(person["id"], person["name"])

    choiceTransfer = raw_input("Ban muon chuyen cho: ")

    for person in people:
        if int(choiceTransfer) == person["id"]:
            print "---------------------"
            print "Qua trinh chuyen tien cho %s" %person["name"]
            x = int(raw_input("Nhap so tien muon chuyen: "))
            if x < person["balance"]:
                person["balance"] = person["balance"] + x
                currentUser["balance"] = currentUser["balance"] - x
                save(currentId=currentUserId, currentUser= currentUser)
                print "Chuyen khoan thanh cong"



def balance(currentUser):
    print "Xin chao %s" %currentUser["name"]
    print "So du hien tai cua ban la %f"%currentUser["balance"]

def save(currentId, currentUser):
    for i in range(len(people)):
        if people[i]["id"] == currentId:
            people[i] = currentUser

    print "So du tai khoan cua ban la"


def program():
    result = authenticate()
    if result[0]:
        currentUser = result[1]
        currentUserId = result[2]
        while True:
            print "1. Chuyen tien"
            print "2. So du"
            print "3. Dang xuat"
            choice = raw_input("")
            if choice == "1":
                transfer(currentUser, currentUserId)
            if choice == "2":
                balance(currentUser)
            if choice == "3":
                program()



program()
