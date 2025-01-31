import csv
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), 'items.csv')


class InstantiateCSVErrorException(Exception):
    def __init__(self):
        self.message = 'Файл поврежден'


class InstantiateCSVError:
    def __init__(self, file_content):
        row_keys_set = set()

        for row in file_content:
            for key in row.keys():
                row_keys_set.add(key)

        if len(row_keys_set) != 3:
            raise InstantiateCSVErrorException

        if 'name' and 'price' and 'quantity' not in row_keys_set:
            raise InstantiateCSVErrorException


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError(f'Складывать можно только объекты Item и дочерние')
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = f'{name[:10]}...'
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, filepath=FILE_PATH):
        """
        Инициализирует экземпляры класса Item из csv файла.
        """
        cls.all.clear()

        try:
            with open(filepath, 'r', newline='', encoding='windows-1251') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                try:
                    InstantiateCSVError(csv_reader)

                except InstantiateCSVErrorException as ex:
                    print(ex.message)

                else:
                    with open(filepath, 'r', newline='', encoding='windows-1251') as csv_file:
                        csv_reader = csv.DictReader(csv_file)

                        for row in csv_reader:
                            name, price, quantity = row['name'], row['price'], row['quantity']
                            cls(name, float(price), int(quantity))

        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(string):
        """
        Преобразует строку в число.

        :param string: Строка для преобразования в число.
        :return: Число.
        """
        return int(float(string))
