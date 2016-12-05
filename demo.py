username = "ngoc"

password = "123"

names = ["Ngoc", "Giang", "Hoang"]


def program():

    if isAuthenticated:

        while True:
            print "-----------------------------"
            print "User: " + username

            print "1. Hien thi Danh Sach Hien co"

            print "2. Them mot nguoi moi"

            print "3. Xoa mot nguoi"

            print "4. Cap nhat ten"

            print "5. Thoat khoi chuong trinh"

            print "-----------------------------"

            choice = raw_input("Nhap option ban muon chon: ").strip()

            if choice == "1":
                print "Danh sach hien co la:"
                for name in names:
                    print "- " + name

            elif choice == "2":

                new_name = raw_input("Nhap mot ten moi: ")

                names.append(new_name)

                print "Ban da them thanh cong."

            elif choice == "3":

                input = raw_input("Nhap ten ban muon xoa: ")

                check = False

                for name in names:
                    if name == input:
                        names.remove(input)
                        check = True
                if check:
                    print "Da xoa"
                else:
                    print "Khong ton tai ten nay"

            elif choice == "4":

                input = raw_input("Nhap phan tu ban muon thay doi: ")

                check2 = False

                for i in range(len(names)):
                    if input == names[i]:
                        new_name = raw_input("Ten ban muon thay doi:")
                        names[i] = new_name
                        check2 = True

                if check2 is False:
                    print "Khong ton tai ten nay"

            elif choice == "5":
                break

            else:
                print "Khong co chuc nang nay. Vui long chong tu 1 -> 5"

while True:
    username_input = raw_input("Username:").strip()

    password_input = raw_input("Password:").strip()

    isAuthenticated = False
    if username_input == username:
        if password_input == password:
            isAuthenticated = True
            program()
        else:
            print "Sai mat khau. Vui long nhap lai"
    else:
        print "Khong ton tai username nay"




