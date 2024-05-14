class Item:
    def __init__(self):
        self._name = ""
        self._weight = 0
        self._cost = 0

    # Геттеры
    def get_name(self):
        return self._name

    def get_weight(self):
        return self._weight

    def get_cost(self):
        return self._cost

    # Сеттеры
    def set_name(self, name):
        self._name = name

    def set_weight(self, weight):
        self._weight = weight

    def set_cost(self, cost):
        self._cost = cost

class Backpack():
    max_weight = int()
    current_weight = int()
    item_list = str()
    
# Пример использования класса
if __name__ == "__main__":
    # Создаем объект класса Item
    item = Item()

    # Устанавливаем значения с помощью сеттеров
    item.set_name("Book")
    item.set_weight(1)
    item.set_cost(10)

    # Получаем значения с помощью геттеров и выводим их
    print("Name:", item.get_name())
    print("Weight:", item.get_weight())
    print("Cost:", item.get_cost())

