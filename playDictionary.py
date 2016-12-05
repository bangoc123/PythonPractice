# 1 buoi javascript

# 1 buoi python -> an soi -> domain, server, dua duoc web len tren web cua minh, quan tri

person1 = {"id":1,"name":"Ngoc", "password":"12345", "email":"ngoc@gmail.com", "balance":10000}

person2 = {"id":2,"name":"Hoa", "password":"123", "email":"hoa@gmail.com", "balance": 20000}

person3 = {"id":3,"name":"Quang", "password":"345", "email":"quang@gmail.com", "balance": 300000}

people = [person1, person2, person3]

def login():
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
                        print "Chao: %s"% person["name"]
                        isauthenticated = True
                        currentUser = person
                        return isauthenticated, currentUser
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


def save(currentUser):
    for i in range(len(people)):
        if people[i]["id"] == currentUser["id"]:
            people[i] = currentUser


def transfer(currentUser):
    for person in people:
        if person["name"] is not currentUser["name"]:
            print "%i. %s" % (person["id"],person["name"])
    transferChoice = raw_input("Ban muon chuyen tien cho: ")

    for i in range(len(people)):
        if str(people[i]["id"]) == transferChoice:
            if people[i]["name"] is not currentUser["name"]:
                print "Ban chuyen tien cho %s"% people[i]["name"]
                x = raw_input("So tien ban muon chuyen: ")
                if currentUser["balance"] > int(x):
                    currentUser["balance"] = currentUser["balance"] - int(x)
                    people[i]["balance"] = people[i]["balance"] + int(x)
                    save(currentUser)
                    print "So tien cua %s la %s"%(people[i]["name"], people[i]["balance"])
                    print currentUser["balance"]


def balance(currentUser):
    print "Chao %s. So du cua ban dang co la %f"%(currentUser["name"], currentUser["balance"])

def program():
    result = login()
    isAuthenticated = result[0]
    currentUser = result[1]
    if isAuthenticated:
        while True:
            print "1. Chuyen tien"
            print "2. So du"
            print "3. Dang xuat"
            choice = raw_input("Chon 1 chuc nang: ")
            if choice == "1":
                transfer(currentUser)
            if choice == "2":
                balance(currentUser)
            if choice == "3":
                program()
                # login()
program()



[1,2,3,4,9,3,0]


[90,60,100,300] -> [300,100,90,60]


#
# Tim so lon nhat trong day
#
# Tim so lon thu 2

# Machine Learning -> Thong Ke -> Prediction -> Data -> Exp

# Google Brain

# AlphaGo









