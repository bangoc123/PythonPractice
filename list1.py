list = []

n = int(raw_input(""))

for i in range(0,n,1):
    demo = raw_input("")
    if demo.find("insert") == 0:
        list.insert(int(demo[7]), int(demo[9:]))
    elif demo.find("print") == 0:
        print list
    elif demo.find("remove") == 0:
        list.remove(int(demo[7:]))
    elif demo.find("append") == 0:
        list.append(int(demo[7:]))
    elif demo.find("sort") == 0:
        list.sort()
    elif demo.find("pop") == 0:
        list.pop()
    elif demo.find("reverse") == 0:
        list.reverse()



