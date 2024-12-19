height = int(input("Please enter the height: "))
check = 0
for x in range(height):
    check+= 1
    print(' '*(height-x-1)+'#'*(check), ' ', '#'*check)
