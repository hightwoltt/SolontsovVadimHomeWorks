import random

LIZT_SIZE = 100
MIN_NUM = 0
MAX_NUM = 100
DIVIDER = 2
LIST_CORRECT = 1

num_list = [0] * LIZT_SIZE
index = 0
temp = 0
low = 0
hight = 100
middle = (LIZT_SIZE + MIN_NUM) // DIVIDER

while index < LIZT_SIZE:
    num_list[index] = random.randint(MIN_NUM,MAX_NUM)
    index += 1
print('Список до сортировки ==>',num_list)

last_count = 99

for j in range (LIZT_SIZE):
    for i in range (last_count, j, -1):
        if num_list[i] < num_list[i-1]:
            temp =  num_list[i]
            num_list[i] = num_list[i-1]
            num_list[i-1] = temp

print ()
print ('Список после сортировки ==>',num_list)
print ()

find_num = int(input('Введите искомое число ==>'))
print ()

while num_list[middle] != find_num and low <= hight:
    if find_num > num_list[middle]:
        low = middle + LIST_CORRECT
        
    elif find_num < num_list[middle]:
        hight = middle - LIST_CORRECT
        
    middle = (low + hight) // DIVIDER
    a = low - hight

if low > hight:
    print('Искомое число не найдено :(')
else:
    print('Индекс искомого в списке ==>',middle)