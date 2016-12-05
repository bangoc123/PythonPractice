# user = []
# list_user = [["ngoc","ngoc@gmail.com","123"]]
#
# def login():
#     pass
#
# def register():
#     username = raw_input("username: ")
#     username = nullValidator(username, "username")
#
#     email = raw_input("email: ")
#     email = nullValidator(email, "email")
#
#
#     password= raw_input("password: ")
#     password = nullValidator(password, "password")
#
#     while True:
#         password2 = raw_input("Re-enter password: ")
#         if password == password2:
#             print "Dang ky thanh cong"
#             user.append(username)
#             user.append(email)
#             user.append(password)
#             list_user.append(user)
#             print list_user
#         else:
#             print "Password khong trung"
#
#
# def nullValidator(input, message):
#     while True:
#         if input == "":
#             print message + " khong duoc de null"
#             input = raw_input("Hay nhap lai " + message +" :")
#             return input
#         else:
#             break
#
#
# while True:
#     print "1.Dang ky"
#     print "2.Dang nhap"
#
#     choice = raw_input("Nhap lua chon cua ban: ")
#     if choice == "1":
#         register()
#     if choice == "2":
#         login()




while True:
    email = raw_input("")
    check = False
    for i in range(len(email)):
        if email[i] == "@":
            print "Dung"
            check = True
            domain = email[(i+1):]
            print domain
            while True:
                for char in domain:
                    check2 = False
                    if char == ".":
                        print "Co ."
                        check2 = True
                        break

                if check2:
                    break

                if not check2:
                    print "Phai co dau cham"
                    break
            if check2:
                break



    if not check:
        print "Not found"























