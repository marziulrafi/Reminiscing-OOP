# 1
num = 1

while num <= 5 :
    print(num)
    num+=1


# 2
num2 = 1

while num2 <= 10 :
    if num2%2 == 0 :
        print(num2, "is even")
    else :
        print(num2, "is odd")
    num2 += 1



# 3
num3 = 1

while num3 <= 5 :
    if num3 % 2 == 0 :
        num3 += 1
        continue
    print(num3)
    num3 += 1


# 4
num4 = 1

while True:
    print(num4)
    if num4 > 5:
        break
    num4 += 1