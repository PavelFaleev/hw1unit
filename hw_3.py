enter_numb = int(input("Введите порядное число: "))

count = 0

for i in range(enter_numb):
    number = int(input("Enter agine YOUR number"))
    if number > 1:
        for divider in range(2, number):
            if number % divider == 0:
                break
        else:
            count+=1
print (count)