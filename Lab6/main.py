import os
from collections import deque    

def adding_new_book(temp_deque = deque()):
    new_book = input(str('Which book you want to add?\n'))
    print('In which place you want to add it\n 1) Begin of deque \t 2) End of deque')
    choose = int(0)
    while choose != 1 and choose != 2:
        try:
            choose = int(input("Choose place: "))
            break
        except(ValueError):
            print("You need to write a number!")
    if choose == 1:
        temp_deque.appendleft(new_book)
    else:
        temp_deque.append(new_book)    
    
    return(temp_deque)

def sorting_deque(temp_deque = deque()):
        sorted_books = []
        temp_deque = deque(sorted(temp_deque))

        while temp_deque:
            sorted_books.append(temp_deque.popleft())
        print('Books are sorted')
        return sorted_books

def deleting_deque_element(temp_deque = deque()):
    print('In which place you want to delete book\n 1) Begin of deque \t 2) End of deque')
    choose = int(0)
    while choose != 1 and choose != 2:
        try:
            choose = int(input("Choose place: "))
            break
        except(TypeError):
            print("You need to write a number!")
    if choose == 1:
        temp_deque.popleft()
    else:
        temp_deque.pop()    
    
    return(temp_deque)

def adding_to_file(sorted_books):
    if not sorted_books:
        print("Books are not sorted")
    else:
        file_name = os.getcwd() + '\\sorted_books.txt'
        with open(file_name, 'w+',encoding="utf-8") as f:
            for book in sorted_books:
                f.write(book + '\n')
        print("Books are added")
    
list_of_books = []
file_name = os.getcwd() 
file_name += '\\books.txt'
with open (file_name,'r',encoding="utf-8") as f:
    lines = f.readlines()
if not lines:
    print("this file is empty")
else:
    sorted_books = deque()
    temp_deque = deque()

    for line in lines:
        temp_deque.append(line.strip())
        choose = 0
    while choose!=6:
        print("""1) добавить элемент в дек
2) удалить элемент из дека
3) отсортировать дек
4) показать дек
5) записать дек в файл
6) выйти""")
        try:
            choose = int(input(''))
        except(ValueError):
            print("You need to write a number!")
        match(choose):
            
            case 1:
                temp_deque = adding_new_book(temp_deque)

            case 2:
                temp_deque = deleting_deque_element(temp_deque)
            
            case 3:
                sorted_books = sorting_deque(temp_deque)
            
            case 4:
                print(temp_deque)
            case 5:
                adding_to_file(sorted_books)
            case 6:
                print('exit')
  
            case _:
                print('No such part of menu')

print("end")