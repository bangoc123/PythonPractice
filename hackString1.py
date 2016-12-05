# z = "ABCDCDCDCDC"
# y = "CDC"
z = raw_input("")
y = raw_input("")
count = 0
if len(z)<=200 and len(z)>=1:
    for i in range(len(z)):
        if i <= len(z) - len(y):
            if z[i:(i+len(y))] == y:
                count = count + 1


print count
#
#
# i = "ABCABCA"
#
# k = "ABCA"