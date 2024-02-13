import os
from collections import deque

list_of_books = []
file_name = os.getcwd() 
file_name += '\\Lab6\\books.txt'
with open (file_name,'r') as f:
    lines = f.readlines()

if not lines:
    print("this file is empty")
else:
    sorted_books = deque()
    temp_deque = deque()

    for line in lines:
        temp_deque.append(line.strip())

    temp_deque = deque(sorted(temp_deque))

    while temp_deque:
        sorted_books.append(temp_deque.popleft())

    for book in sorted_books:
        print(book)
