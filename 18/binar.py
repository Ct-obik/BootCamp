from random import randint
x=randint(0,100)
count_perebor=0
#   метод последовательного перебора
for i in range(0,101):
    count_perebor+=1
    if i==x:
        print("Число найдено!")
        break
print("Загаданное число было", x , "и для его посика методом перебора потребовалось", count_perebor, "итераций")

count_random=1
#    метод последовательного перебора
y=randint(0,100)
while x!=y:
    y=randint(0,100)
    count_random+=1
print("Загаданное число было", x , "и для его посика угадыванием потребовалось", count_random, "итераций")

# Игра в угадайку. Компьютер загадывает, мы отгадываем. (Бинарный метод)
count_bin=1
print("Давай начнём игру: Угадай число от 0 до 100")
y=int(input('Введите число: '))
while x!=y:
    print(y)
    if x<y: print("меньше") 
    else: print("больше")
    y=int(input('Введите число: '))
    count_bin+=1
print("Загаданное число было", x , "и для его посика бинарным алгоритмом потребовалось", count_bin, "итераций")