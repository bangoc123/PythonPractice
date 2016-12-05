name = raw_input("")

if len(name) > 0 & len(name) <= 100:
    for i in range(len(name)):
        if name[i].isupper():
            name = name[:i] + name[i].lower() + name[i+1:]
        else:
            name = name[:i] + name[i].upper() + name[i + 1:]
    print name