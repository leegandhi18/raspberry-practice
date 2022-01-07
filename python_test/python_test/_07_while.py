sum = 0
i = 1

while i < 11:  # i가 11보다 작을때 까지만 아래 코드를 실행한다.
    sum = sum+i
    print("i= ", i)
    if(i == 5):
        break
    i = i+1

print("sum = ", sum)
