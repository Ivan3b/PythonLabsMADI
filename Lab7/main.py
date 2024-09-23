import math

# Функция для определения приоритета оператора
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op in ('^'):
        return 3
    if op in ('sin', 'cos', 'tan', 'cot', 'log', 'sqrt'):
        return 4
    return 0

# Проверка, является ли данный символ оператором
def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

# Проверка, является ли данная строка функцией
def is_function(s):
    return s in ['sin', 'cos', 'tan', 'cot', 'log', 'sqrt']

# Функция для вычисления постфиксного выражения
def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():  # если операнд
            stack.append(float(token))
        elif token == '+':
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
        elif token == '-':
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif token == '*':
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
        elif token == '/':
            b, a = stack.pop(), stack.pop()
            stack.append(a / b)
        elif token == '^':
            b, a = stack.pop(), stack.pop()
            stack.append(a ** b)
        elif token == 'sin':
            a = stack.pop()
            stack.append(math.sin(math.radians(a)))
        elif token == 'cos':
            a = stack.pop()
            stack.append(math.cos(math.radians(a)))
        elif token == 'tan':
            a = stack.pop()
            stack.append(math.tan(math.radians(a)))
        elif token == 'cot':
            a = stack.pop()
            stack.append(1 / math.tan(math.radians(a)))
        elif token == 'log':
            a = stack.pop()
            stack.append(math.log10(a))
        elif token == 'sqrt':
            a = stack.pop()
            stack.append(math.sqrt(a))

    return stack[0] if stack else None

# Функция для преобразования инфиксного выражения в постфиксное
def infix_to_postfix(expression):
    stack = []
    output = []
    i = 0

    while i < len(expression):
        if expression[i].isalnum():
            operand = ''
            while i < len(expression) and (expression[i].isalnum() or expression[i] == '.'):
                operand += expression[i]
                i += 1
            output.append(operand)
            i -= 1
        elif i < len(expression) - 2 and expression[i:i+3] in ['sin', 'cos', 'tan', 'cot']:
            stack.append(expression[i:i+3])
            i += 2
        elif i < len(expression) - 3 and expression[i:i+3] == 'log':
            stack.append('log')
            i += 2
        elif i < len(expression) - 4 and expression[i:i+4] == 'sqrt':
            stack.append('sqrt')
            i += 3
        elif expression[i] == '(':
            stack.append(expression[i])
        elif expression[i] == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif is_operator(expression[i]):
            while stack and precedence(stack[-1]) >= precedence(expression[i]):
                output.append(stack.pop())
            stack.append(expression[i])

        i += 1

    while stack:
        output.append(stack.pop())

    return ' '.join(output)

# Функция для преобразования инфиксного выражения в префиксное
def infix_to_prefix(expression):
    expression = expression[::-1]
    expression = expression.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    result = infix_to_postfix(expression)
    return result[::-1]

# Основная программа
if __name__ == "__main__":
    expression = input("Введите инфиксное выражение: ")
    print("Инфиксное выражение:", expression)
    
    postfix_expr = infix_to_postfix(expression)
    print("Постфиксное выражение:", postfix_expr)
    
    prefix_expr = infix_to_prefix(expression)
    print("Префиксное выражение:", prefix_expr)

    try:
        result = evaluate_postfix(postfix_expr)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка при вычислении: {e}")
