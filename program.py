username = "ngoc"

password = "123"

names = ["Uyen","Hoa","Huyen","Ha"]

isAuthenticated = False

def login():
    count = 0
    authenticatedResult = False
    while True:
        username_input = raw_input("Ten dang nhap cua ban: ")

        if username_input == username:
            while True:
                password_input = raw_input("Password cua ban: ")
                if password_input == password:
                    print "Dang nhap thanh cong!!!"
                    authenticatedResult = True
                    break
                else:
                    print "Mat khau chua chinh xac"
                    count = count + 1
                    if count == 5:
                        break
            break

        if authenticatedResult == True:
            break

        else:
            print "Username khong ton tai"
            count = count + 1
            if count == 5:
                break
    if count == 5:
        authenticatedResult = False

    return authenticatedResult

isAuthenticated = login()

if isAuthenticated:
    while True:
        print "--------------------"
        print "Hi" + username
        print "1. In danh sach"
        print "2. Them nguoi moi"
        print "3. Xoa"
        print "4. Thay doi Ten"
        print "5. Dang xuat"
        print "--------------------"
        choice = raw_input("Vui long chon mot chuc nang:")
        if choice == "1":
            print "Danh sach ten la: "
            for name in names:
                print "- " + name
        elif choice == "2":
            new_name = raw_input("Nhap ten ban muon them: ")
            names.append(new_name)
        elif choice == "3":
            for name in names:
                if name == deleteName:
                    names.remove(name)
        elif choice == "4":
            editname = raw_input("Ban muon thay doi ten nao?")
            for name in names:
                if editname == name:
                    changeName = raw_input("ban muon thay thanh gi?")
                    name = changeName
        elif choice == "5":
            isAuthenticated = False
            login()
        else:
            print "Khong co chuc nang nay"

