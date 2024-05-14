"""Задание
1 Реализовать в Java класс в соответствии со своим вариантом.
Предусмотреть не менее 3 параметров, одним из которых является
объект другого класса, 2 методов и 2 конструкторов (включая
конструктор по умолчанию). Предусмотреть счетчик экземпляров
классов.
Предусмотреть для классов, являющихся полями не менее 2
параметров, 2 методов и 2 конструкторов (включая конструктор по
умолчанию).
2 Реализовать хранение объектов классов в виде списка.
Предусмотреть следующие операции над списком:
1) Добавления элемента (доп. нескольких элементов) в конец или в
определенное место списка;
2) Удаление элемента (доп. нескольких элементов) в конце или в
определенном месте списка;
3) Изменение определенного элемента списка;
4) Поиск и вывод номера и информации введенного элемента по
разным полям;
5) Вывод на экран всех объектов списка или определенного
элемента списка;
6) Вывод числа элементов в списке.
Варианты.
1
Класс кот.
"""
import os
class Cat():
    def __init__(self, name, age, breed):
        self.set_data(name, age, breed)
        self.get_data()


    def set_data(self, name = None, age = None, breed = None):
        self.name = name
        self.age = age
        self.breed = breed

    def get_data(self):
        print('Name: ' + self.name)
        print('Age: ' + str(self.age))
        print('Breed: ' + self.breed)

class New_cat(Cat):
    color = None
    name = None
    color = None
    def __init__(self, name, age, color, breed):
        super(New_cat, self).__init__(name,age,breed)
        self.color = color

    def change(self):
        self.name = input("Enter new name: ")
        self.age = input("Enter new age: ")
        self.breed = input("Enter new breed: ")
        self.color = input("Enter new color: ")

    def all_about_nc(self):
        print('Name: ' + self.name)
        print('Age: ' + str(self.age))
        print('Breed: ' + self.breed)
        print('Color: ' + self.color)

menu_point = 1
list_of_cats = []
while menu_point != 9:
    menu_point = -1
    print("""Main menu
    1) Create new cat
    2) Show all cats
    3) Change cat
    4) Delete cat
    5) Found cat
    6) Quantity of cats
    7) Put cats in file
    8) Get cats from file
    9) Exit
    """)
    while menu_point not in range(0,10):
        menu_point = int(input("Enter which element you want to choose: "))
        if (menu_point <= 0) or (menu_point > 10):
            print("tou got only 9 menu items")

        match menu_point:
            case 1:
                quantity_of_cats = int(input("How many cats you want to add: "))
                for i in range(quantity_of_cats):
                    print("Cat № " + str(i + 1))
                    name = input("Enter cat's name: ")
                    age = input("Enter cat's age: ")
                    color = input("Enter cat's color: ")
                    breed = input("Enter cat's breed: ")
                    cat = New_cat(name, age, color, breed)
                    choose = 0
                    while choose != 1:
                        choose = int(input("""do you what to save this cat?
        1) yes       2) No
        """))
                        if choose == 2:
                            cat.change()
                    cat_info = [cat.name, cat.age, cat.color, cat.breed]
                    list_of_cats.append(cat_info)
            case 2:
                for i in range(len(list_of_cats)):
                    print("Cat №" + str(i+1) + str(list_of_cats[i]))
            case 3:
                cat_for_change = int(input("Print number of cat you what to change: "))
                print("""1)Name
    2) Age
    3) Color
    4) Breed
    5) All""")
                choose = int(input("Which element you want to change: "))
                match choose:
                    case 1:
                        list_of_cats[cat_for_change-1][0] = input("Enter cat's name: ")
                    case 2:
                        list_of_cats[cat_for_change-1][1] = input("Enter cat's age: ")
                    case 3:
                        list_of_cats[cat_for_change-1][2] = input("Enter cat's color: ")
                    case 4:
                        list_of_cats[cat_for_change-1][3] = input("Enter cat's breed: ")
                    case 5:
                        list_of_cats[cat_for_change-1][0] = input("Enter cat's name: ")
                        list_of_cats[cat_for_change-1][1] = input("Enter cat's age: ")
                        list_of_cats[cat_for_change-1][2] = input("Enter cat's color: ")
                        list_of_cats[cat_for_change-1][3] = input("Enter cat's breed: ")
            case 4:
                choose = int(input("which cat you want to delete: "))
                list_of_cats.pop(choose-1)
            case 5:
                choose = input("which cat you want to found: ")
                print("""1)Name
    2) Age
    3) Color
    4) Breed
                """)
                k = int(input("By what element you want to find cat: "))
                this = 0
                for i in range(len(list_of_cats)):
                    if choose in list_of_cats[i][k-1]:
                        print(list_of_cats[i])
                        print("Is it that cat?")
                        print("1)Yes           2)No")
                        this = int(input())
                        if this == 1:
                            break

            case 6:
                print(len(list_of_cats))
            
            case 7:
                print("Choose file: ")
                choose = input(("1: Data1.txt         2: Data2.txt \n"))
                file_name = os.getcwd() + '\\Lab1_PEM\\Data' + str(choose) +'.txt'
                with open(file_name, 'w', encoding= "utf-8") as f:
                    for cat in list_of_cats:
                        f.write(f'name: {cat[0]}\n')
                        f.write(f'age: {cat[1]}\n')
                        f.write(f'color: {cat[2]}\n')
                        f.write(f'breed: {cat[3]}\n')
                        f.write('\n')  
                    print('Cats are added')
                

            case 8:
                print("Choose file: ")
                choose = input(("1: Data1.txt         2: Data2.txt \n"))
                file_name = os.getcwd() + '\\Lab1_PEM\\Data' + str(choose) +'.txt'
                cats_data = []

                with open(file_name, 'r') as file:
                    lines = file.readlines()
                    temp_cat = {}
                    for line in lines:
                        
                        if line.strip() == '':
                            cats_data.append(temp_cat)
                            temp_cat = {}  
                        else:
                            
                            key, value = line.strip().split(': ')
                            
                            temp_cat[key] = value

                
                for cat in cats_data:
                    print('Name:', cat['name'])
                    print('Age:', cat['age'])
                    print('Color:', cat['color'])
                    print('Breed:', cat['breed'])
                    print()
                    list_of_cats.append(list(cat.values()))
            case 9:
                print("exit")


