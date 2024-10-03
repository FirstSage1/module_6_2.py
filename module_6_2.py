# module_6_2.py сокрытие атрибутов
# ==================================================================

class Vehicle:  # любой транспорт
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white'] # список допустимых цветов

    # для окрашивания.
    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner  # - владелец транспорта. (владелец может меняться)
        self.__model = __model  # - модель транспорта. (мы не можем менять название модели)
        self.__engine_power = __engine_power  # - мощность двигателя. (мы не можем менять
                                                # мощность двигателя самостоятельно)
        self.__color = __color  # - название цвета. (мы не можем менять цвет автомобиля
                                        # своими руками)

    def get_model(self):
        return f"Модель: {self.__model}"


    def get_horsepower(self):
        return f"Мощность двигателя: мощность: {self.__engine_power}"


    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color:str):
        if new_color.lower() in self.__COLOR_VARIANTS: # если он есть в списке
                                # __COLOR_VARIANTS, меняет цвет __color на new_color
            self.__color = new_color
        # в противном случае выводит на экран надпись
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # (в седан может поместиться только 5 пассажиров)

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500,'blue')

# Изначальные свойства
vehicle1.print_info()

 # Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
