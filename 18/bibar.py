# отгадываем число компьютера с помощью бинарного метода

from random import randint
left=0
right=1000
x=randint(left,right)
count_bin=1
print("Давай начнём игру: Угадаем число")

mid=(left+right) // 2
while x!=mid:
    print(mid)
    if x<mid: 
        print("меньше") 
        right=mid-1
    else: 
        print("больше")
        left=mid+1
    mid=(left+right) // 2
    count_bin+=1
print("Загаданное число было", x , "и для его посика бинарным алгоритмом потребовалось", count_bin, "итераций")