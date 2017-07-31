myIn = raw_input("Enter I/P: ")
temp = ''
count = 1

for i in range(len(myIn)):
    if len(temp) == 0:
        temp += myIn[i]
    else:
        if temp[-1] == myIn[i]:
            count += 1
        elif temp[-1] != myIn[i]:
            temp += str(count)
            count = 1
            temp += myIn[i]
temp += str(count)
print temp
