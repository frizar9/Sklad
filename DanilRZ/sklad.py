import random

from products import *

class Warehouse:
    def __init__(self, name):
        self.arr_things = []
        self.arr_paint = []
        self.name = name
        self.arr_nails = []
        self.known_diluents = ['Вода','Растворитель']
        self.not_used = []

    def add_nails(self,nail):
        self.arr_nails.append(nail)

    def generate_nails(self):
        conversion_factors = {
    "mm": 1,
    "cm": 0.1,
    "m": 0.001
  }
        size = random.randint(1, 6)
        count = random.randint(10, 20000)
        name_size = f"M{random.randint(1, 6)}"
        nail = Nail(
            conversion_factors=conversion_factors,
            name_size=name_size,
            count=count,
            name="Гвозди",
            size=size,
            unit_of_measurement="mm"
        )
        self.set_nails([nail, *self.arr_nails])

    def generate_paint(self):
        conversion_factors = {
            "mm": 1,
            "cm": 0.1,
            "m": 0.001
        }
        paint_name = ["Маслянная краска", "Нитроэмалевая краска"][random.randint(0, 1)]
        color = ["Красный", "Зеленый", "Белый", "Синий", "Розовый"][random.randint(0, 4)]
        unit = ["литры", "мл"][random.randint(0, 1)]
        count = random.randint(10, 1000)
        volume = random.randint(1, 5)
        paint_type = ["Oil", "Nitro"][random.randint(0, 1)]
        if paint_name == "Нитроэмалевая краска":
            diluents = ["Вода", "Разбавитель"]
            paint = NitroPaint(name=paint_name, unit=unit, color=color, count=count, diluents=diluents, volume=volume)
        else:
            paint = Paint(name=paint_name, unit=unit, color=color, paint_type=paint_type, count=count, volume=volume)
        self.set_paints([paint, *self.arr_paint])

    def generate_events(self):
        for i in range(random.randint(2, 6)):
            self.generate_nails()
        for i in range(random.randint(2, 6)):
            self.set_thing([*self.arr_paint, *self.arr_nails])

    def set_nails(self, value):
        self.arr_nails = value

    def get_nails(self):
        return self.arr_nails

    def add_thing(self, item):
        self.arr_things.append(item)

    def set_thing(self, value):
        self.arr_things = value

    def add_paints(self, paint):
        self.arr_paint.append(paint)

    def set_paints(self, value):
        self.arr_paint = value

    def get_paints(self):
        return self.arr_paint

    def print_thing(self):
        print(self.arr_things)

    def print_paints(self):
        print(self.arr_paint)

    def print_nails(self):
        print(self.arr_nails)
    #Количество краски заданного цвета, в том числе с разбивкой на масляные и нитроэмали.
    def print_colors(self):
        color_counts = {}
        for paint in self.arr_paint:
            color = paint.getColor()
            paint_type = paint.paint_type
            if color not in color_counts:
                color_counts[color] = {'Oil': 0, 'Nitro': 0}
            if paint_type == 'Oil':
                color_counts[color]['Oil'] += paint.getCount()
            elif paint_type == 'Nitro':
                color_counts[color]['Nitro'] += paint.getCount()


        print("Количество красок заданного цвета:")
        for color, counts in color_counts.items():
            print(f"Цвет: {color}")
            print(f"Масляные: {counts['Oil']} шт.")
            print(f"Нитроэмали: {counts['Nitro']} шт.")

    # Список всех товаров на складе с указанием их количества и единиц измерения. У всех товаров, единица измерения которых приводится к базовой, количество должно быть выведено в базовых единицах измерения. Список может быть отсортирован по наименованию товаров, по типам товаров
    def list_goods(self,sort_by='name'):
        goods_list = self.arr_things
        if sort_by == 'name':
            goods_list.sort(key=lambda x: x.getName())
        elif sort_by == 'type':
            goods_list.sort(key=lambda x: type(x).__name__)
        else:
            print("Ошибка", "Невозможно отсортировать.")

        base_units_conversion = {
            "литры": 1,
            "мл": 0.001,
            'mm': 1
        }
        print('Список товаров\n')
        for good in goods_list:
            try:
                base_qty = good.getCount() * base_units_conversion.get(good.getUnit(), 1)
                if isinstance(good, NitroPaint) or isinstance(good, Paint):
                    color = good.getColor()
                    paint_type = good.getPaint_type()
                    if good.getUnit() == "мл":
                        total_volume_liters = good.calculate_total_volume() * base_units_conversion["мл"]
                        print(
                            f"{good.getName()} ({good.getCount()} банки(ок)), по {good.getVolume()} {good.getUnit()}, Общий объем {total_volume_liters} л, Цвет: {color}, Тип: {paint_type}")  # Замена на print
                    else:
                        total_volume_liters = good.calculate_total_volume()
                        print(
                            f"{good.getName()} ({good.getCount()} банки(ок)), по {good.getVolume()} {good.getUnit()}, Общий объем {total_volume_liters} {good.getUnit()}, Цвет: {color}, Тип: {paint_type}")  # Замена на print
                elif isinstance(good, Nail):
                    converted_size = good.convert_size('mm')
                    if converted_size is not None:
                        print(
                            f"{good.getName()} ({converted_size}), {good.getUnit()}, Размер: {good.getSize()}, Название размера: {good.getName_size()}")  # Замена на print
                    else:
                        print(f"{good.getName()} ({base_qty} шт.), {good.getUnit()}")
                else:
                    print(f"{good.getName()} ({base_qty} единиц), {good.getUnit()}")
            except AttributeError as e:
                print(f"Ошибка при обработке товара {good.getName()}: {e}")



    #Список цветов красок, имеющихся на складе, в том числе с разбивкой на масляные и нитроэмали.
    def print_list_colors(self):
        color_counts = {}
        for paint in self.arr_paint:
            color = paint.getColor()
            if color not in color_counts:
                color_counts[color] = {'Oil': 0, 'Nitro': 0}
            if paint.paint_type == 'Oil':
                color_counts[color]['Oil'] += paint.getCount()
            elif paint.paint_type == 'Nitro':
                color_counts[color]['Nitro'] += paint.getCount()

        print("Список цветов красок на складе:")
        for color, counts in color_counts.items():
            print(f"Цвет: {color}")
            print(f"Масляные: {counts['Oil']} шт.")
            print(f"Нитроэмали: {counts['Nitro']} шт.")

    # количество гвоздей данного размера
    def print_nails_by_size(self, name_size):
        size_count = {}
        for nail in self.arr_nails:
            if nail.name_size == name_size:
                if name_size not in size_count:
                    size_count[name_size] = 0
                size_count[name_size] += nail.getCount()
        print(f"Количество гвоздей размера {name_size}: {size_count.get(name_size, 0)} шт.")

    # Список нитроэмалей, для которых на складе есть нужные разбавители.
    def list_nitro_paints_with_diluents(self):
        nitro_paints_with_diluents = []
        for paint in self.arr_paint:
            if type(paint) is NitroPaint:
                has_all_diluents = True
                for diluent in paint.getDiluents():
                    if diluent not in self.known_diluents:
                        has_all_diluents = False
                        break
                if has_all_diluents:
                    nitro_paints_with_diluents.append(paint)
        print("Список нитроэмалей, для которых на складе есть нужные разбавители:")
        for paint in nitro_paints_with_diluents:
            print(f"Название: {paint.getName()}, Цвет: {paint.getColor()}, Количество: {paint.getCount()}")

    # Список разбавителей, которые не используются в красках, находящихся на складе.
    def collect_unused_diluents(self):
        unused_diluents_set = set()
        for paint in self.arr_paint:
            if isinstance(paint, NitroPaint):
                for diluent in paint.getDiluents():
                    unused_diluents_set.add(diluent)
        unused_diluents = list(unused_diluents_set - set(self.known_diluents))
        self.unused_diluents = unused_diluents
        print("Список разбавителей, которые не используются в красках на складе:")
        for diluent in self.unused_diluents:
            print(diluent)

    def show_converted_nail_size_by_name(self, name_size):
        matching_nails = [nail for nail in self.arr_nails if nail.getName_size() == name_size]
        if matching_nails:
            for nail in matching_nails:
                converted_size_cm = nail.convert_size("cm")
                converted_size_m = nail.convert_size("m")
                print(f"Конвертированный размер гвоздя '{name_size}':")
                print(f"Сантиметры: {converted_size_cm} см")
                print(f"Метры: {converted_size_m} м")
        else:
            print(f"Гвозди с названием размера '{name_size}' не найдены.")
