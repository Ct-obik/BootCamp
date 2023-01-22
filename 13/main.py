print("Hello")
from Department import Department
from Worker import Worker
from DataBase import DataBase
dep1: Department = Department(0, "Информационные технологии")
dep2: Department = Department(1, "Отдел кадров")
dep3: Department = Department(2, "Бухгалтерия")

print(dep1)
print(dep2)
print(dep3)

worker1: Worker = Worker(0, "Мария Ивановна", 26, 1234, 1)
worker2: Worker = Worker(1, "Иванов Станислав", 32, 10234, 0)
worker3: Worker = Worker(2, "Зина Ивановна", 46, 4321, 2)
worker4: Worker = Worker(3, "Алёша Пупкин", 18, 10, 0)

db: DataBase =DataBase()
db.append_worker(worker1)
db.append_worker(worker2)
db.append_worker(worker3)
db.append_worker(worker4)

db.append_dep(dep1)
db.append_dep(dep2)
db.append_dep(dep3)

print(db.select_all_dep())
print('========')
print(db.select_all_worker())
print('========')
print(db.report())
print("=========") # можем указать, что нам показать из свойств
for item in db.report():
    print((item[0],item[2]))