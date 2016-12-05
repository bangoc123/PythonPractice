list_user = []
["Ngoc", "ngoc@gmail.com", "123"]
["Uyen", "uyen@gmail.com", "123"]
list_user = [["Ngoc", "ngoc@gmail.com", "123"], ["Uyen", "uyen@gmail.com", "123"]]
# def none(input):
# 	while True:
# 		check=False
# 		username=input("username:")
# 		if username=="":
# 			print("Khong duoc de trong")
# 			check=True
# 		return check


while True:
    while True:
        check = False
        username = input("username:")
        if username == "":
            print("Khong duoc de trong")
            check = True
        else:
            break

    while True:
        check1 = False
        email = input("email:")
        if email == "":
            print("Khong duoc de trong")
            check1 = True
        else:
            check3 = False
            for char in email:
                if char == "@":
                    check3 = True
                    x = email
                    check4 = False
                    for i in range(len(email)):
                        if email[i] == "@":
                            domain = x[(i + 1):]
                            check4 = False
                            while True:
                                for char1 in domain:
                                    if char1 == ".":
                                        check4 = True
                                        break

                                if check4:
                                    break
                                if check4 == False:
                                    print("Email phai co dau cham")
            if check3:
                break

            if check3 == False:
                print("email phai co @")

    while True:
        check2 = False
        password = input("password:")
        if password == "":
            print("Khong duoc de trong")
            check = True
        else:
            password2 = input("password2:")
            if password == password2:
                print ("Dang ky thanh cong")
                break
            else:
                print ("Nhap lai password")

    user = [username, email, password]
    list_user.append(user)
    print(list_user)


