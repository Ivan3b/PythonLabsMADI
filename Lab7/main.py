def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = []

    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Удаляем '(' из стека
        else:
            while stack and precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)


# Получаем инфиксное выражение от пользователя
infix_expression = input("Введите инфиксное выражение: ")

# Преобразуем инфиксное выражение в постфиксную нотацию
postfix_expression = infix_to_postfix(infix_expression)
print("Постфиксная запись:", postfix_expression)
