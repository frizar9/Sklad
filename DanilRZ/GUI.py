import tkinter as tk
from tkinter import ttk
from main import *
from tkinter import simpledialog
from tkinter import messagebox
import random

warehouse = Warehouse('Склад товаров')

config = load_config(path_file='config.json')
warehouse.set_paints(config['paints'])
warehouse.set_nails(config['nails'])
warehouse.set_thing([*config['paints'], *config['nails']])

root = tk.Tk('250x700')
root.title("Управление складом")
root.configure(bg='lightblue')
root.columnconfigure(0, weight=1)
root.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
for col in range(5):
    root.grid_columnconfigure(col, weight=1)




# def add_oil_paint():
#     name = simpledialog.askstring(title="Добавить Масляную Краску", prompt="Введите название:", parent=root)
#     unit = simpledialog.askstring(title="Добавить Масляную Краску", prompt="Введите единицы измерения(литры,мл):",
#                                   parent=root)
#     color = simpledialog.askstring(title="Добавить Масляную Краску", prompt="Введите цвет(с большой буквы):",
#                                    parent=root)
#     count = simpledialog.askinteger(title="Добавить Масляную Краску", prompt="Введите количество:", minvalue=1,
#                                     parent=root)
#     volume = simpledialog.askfloat(title="Добавить Масляную Краску", prompt="Введите объем 1 банки краски:", minvalue=0,
#                                    parent=root)
#     oil_paint = OilPaint(name, unit, color, count, volume=volume)
#     warehouse.add_paints(oil_paint)
#
#
# def add_nitro_paint():
#     name = simpledialog.askstring(title="Добавить Нитроэмалевую Краску", prompt="Введите название:", parent=root)
#     unit = simpledialog.askstring(title="Добавить Нитроэмалевую Краску", prompt="Введите единицы измерения(литры,мл):",
#                                   parent=root)
#     color = simpledialog.askstring(title="Добавить Нитроэмалевую Краску", prompt="Введите цвет(с большой буквы):",
#                                    parent=root)
#     count = simpledialog.askinteger(title="Добавить Нитроэмалевую Краску", prompt="Введите количество:", minvalue=1,
#                                     parent=root)
#     diluents_input = simpledialog.askstring(title="Добавить Нитроэмалевую Краску",
#                                             prompt="Введите разбавители через запятую с большой буквы:", parent=root)
#     diluents = diluents_input.split(",") if diluents_input else ["Вода", "Растворитель"]
#     volume = simpledialog.askfloat(title="Добавить Нитроэмалевую Краску", prompt="Введите объем 1 банки краски:",
#                                    minvalue=0, parent=root)
#     nitro_paint = NitroPaint(name, unit, color, count, diluents=diluents, volume=volume)
#     warehouse.add_paints(nitro_paint)
#
#
# def add_nails():
#     name = simpledialog.askstring(title="Добавить Гвозди", prompt="Введите название:", parent=root)
#     unit = simpledialog.askstring(title="Добавить Гвозди", prompt="Введите единицы измерения (mm):", parent=root)
#     size = simpledialog.askstring(title="Добавить Гвозди", prompt="Введите размер (mm):", parent=root)
#     count = simpledialog.askinteger(title="Добавить Гвозди", prompt="Введите количество:", minvalue=1, parent=root)
#     name_size = simpledialog.askstring(title="Добавить Гвозди", prompt="Введите название размера:", parent=root)
#     nail = Nail(name, unit, size, config["data"]["conversion_factors"], count, name_size)
#     warehouse.add_nails(nail)

def generate_nails():
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
    warehouse.set_nails([nail, *warehouse.arr_nails])

def generate_paint():
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
    if paint_name == "Маслянная краска":
        diluents = ["Лимонад", "Сок"]
        paint = NitroPaint(name=paint_name, unit=unit, color=color, count=count, diluents=diluents, volume=volume)
    else:
        paint = Paint(name=paint_name, unit=unit, color=color, paint_type=paint_type, count=count, volume=volume)
    warehouse.set_paints([paint, * warehouse.arr_paint])

def generate_events():
    for i in range(random.randint(1, 2)):
        warehouse.generate_nails()
    for i in range(random.randint(1, 2)):
        warehouse.generate_paint()
    for i in range(random.randint(1, 2)):
        warehouse.set_thing([*warehouse.arr_paint, *warehouse.arr_nails])

def update_text_area(text):
    text_area.insert(tk.END, text)


# #Количество краски заданного цвета, в том числе с разбивкой на масляные и нитроэмали.
def print_colors():
    color_counts = {}
    for paint in warehouse.arr_paint:
        color = paint.getColor()
        paint_type = paint.paint_type
        if color not in color_counts:
            color_counts[color] = {'Oil': 0, 'Nitro': 0}
        if paint_type == 'Oil':
            color_counts[color]['Oil'] += paint.getCount()
        elif paint_type == 'Nitro':
            color_counts[color]['Nitro'] += paint.getCount()

    result_text = "Количество красок заданного цвета:\n"
    for color, counts in color_counts.items():
        result_text += (f"Цвет: {color}\n")
        result_text += (f"Масляные: {counts['Oil']} шт.\n")
        result_text += (f"Нитроэмали: {counts['Nitro']} шт.\n")
    update_text_area(result_text)


# #Список цветов красок, имеющихся на складе, в том числе с разбивкой на масляные и нитроэмали.
def print_list_colors():
    color_counts = {}
    for paint in warehouse.arr_paint:
        color = paint.getColor()
        if color not in color_counts:
            color_counts[color] = {'Oil': 0, 'Nitro': 0}
        if paint.paint_type == 'Oil':
            color_counts[color]['Oil'] += paint.getCount()
        elif paint.paint_type == 'Nitro':
            color_counts[color]['Nitro'] += paint.getCount()

    result_text = "Список цветов красок на складе:\n"
    for color, counts in color_counts.items():
        result_text += (f"Цвет: {color}\n")
        result_text += (f"Масляные: {counts['Oil']} шт.\n")
        result_text += (f"Нитроэмали: {counts['Nitro']} шт.\n")
    update_text_area(result_text)


#количество гвоздей данного размера
def print_nails_by_size():
    name_size = simpledialog.askstring(title="Выберите размер гвоздя", prompt="Введите размер гвоздя:")
    size_count = {}
    for nail in warehouse.arr_nails:
        if nail.name_size == name_size:
            if name_size not in size_count:
                size_count[name_size] = 0
            size_count[name_size] += int(nail.getCount())

    result_text = f"Количество гвоздей размера {name_size}: {size_count.get(name_size, 0)} шт.\n"
    update_text_area(result_text)


#Список нитроэмалей, для которых на складе есть нужные разбавители.
def list_nitro_paints_with_diluents():
    nitro_paints_with_diluents = []
    for paint in warehouse.arr_paint:
        if isinstance(paint, NitroPaint):
            has_all_diluents = True
            for diluent in paint.getDiluents():
                if diluent not in warehouse.known_diluents:
                    has_all_diluents = False
                    break
            if has_all_diluents:
                nitro_paints_with_diluents.append(paint)
    result = "Список нитроэмалей, для которых на складе есть нужные разбавители:\n"
    for paint in nitro_paints_with_diluents:
        result += f"Название: {paint.getName()}, Цвет: {paint.getColor()}, Количество: {paint.getCount()}\n"
    update_text_area(result)


#Список разбавителей, которые не используются в красках, находящихся на складе.
def collect_unused_diluents():
    unused_diluents_set = set()
    for paint in warehouse.arr_paint:
        if isinstance(paint, NitroPaint):
            for diluent in paint.getDiluents():
                unused_diluents_set.add(diluent)
    unused_diluents = list(unused_diluents_set - set(warehouse.known_diluents))
    warehouse.unused_diluents = unused_diluents
    result_text = "Список разбавителей, которые не используются в красках на складе:\n"
    for diluent in warehouse.unused_diluents:
        result_text += (diluent + "\n")
    update_text_area(result_text)


# Список всех товаров на складе с указанием их количества и единиц измерения. У всех товаров, единица измерения которых приводится к базовой, количество должно быть выведено в базовых единицах измерения. Список может быть отсортирован по наименованию товаров, по типам товаров
def list_goods(sort_by='name'):
    goods_list = warehouse.arr_things
    if sort_by == 'name':
        goods_list.sort(key=lambda x: x.getName())
    elif sort_by == 'type':
        goods_list.sort(key=lambda x: type(x).__name__)
    else:
        messagebox.showerror("Ошибка", "Невозможно отсортировать.")

    base_units_conversion = {
        "литры": 1,
        "мл": 0.001,
        'mm': 1
    }
    result_text = 'Список товаров\n'
    for good in goods_list:
        try:
            base_qty = good.getCount() * base_units_conversion.get(good.getUnit(), 1)

            if isinstance(good, NitroPaint) or isinstance(good, Paint):
                color = good.getColor()
                paint_type = good.getPaint_type()
                if good.getUnit() == "мл":
                    total_volume_liters = good.calculate_total_volume() * base_units_conversion["мл"]
                    result_text += (f"{good.getName()} ({good.getCount()} банки(ок)), по {good.getVolume()} {good.getUnit()}, Общий объем {total_volume_liters} л, Цвет: {color}, Тип: {paint_type}\n")
                    result_text+='\n'
                else:
                    total_volume_liters = good.calculate_total_volume()
                    result_text += (
                        f"{good.getName()} ({good.getCount()} банки(ок)), по {good.getVolume()} {good.getUnit()}, Общий объем {total_volume_liters} {good.getUnit()}, Цвет: {color}, Тип: {paint_type}\n")
                    result_text += '\n'
            elif isinstance(good, Nail):
                converted_size = good.convert_size('mm')
                if converted_size is not None:
                    result_text += (
                        f"{good.getName()} ({converted_size}), {good.getUnit()}, Размер: {good.getSize()}, Название размера: {good.getName_size()}\n")
                    result_text += '\n'
                else:
                    result_text += (f"{good.getName()} ({base_qty} шт.), {good.getUnit()}\n")
                    result_text += '\n'
            else:
                result_text += (f"{good.getName()} ({base_qty} единиц), {good.getUnit()}\n")
                result_text += '\n'
        except AttributeError as e:
            result_text += (f"Ошибка при обработке товара {good.getName()}: {e}")
            result_text += '\n'

    update_text_area(result_text)


#конвертация размера гвоздей
def show_converted_nail_size_by_name():
    name_size = simpledialog.askstring(title="Введите название размера гвоздя(M1-M6)", prompt="Название размера:", parent=root)
    if name_size:
        matching_nails = [nail for nail in warehouse.arr_nails if nail.getName_size() == name_size]
        if matching_nails:
            for nail in matching_nails:
                converted_size_cm = nail.convert_size("cm")
                converted_size_m = nail.convert_size("m")
                result_text = f"Конвертированный размер гвоздя '{name_size}':\n"
                result_text += f"Сантиметры: {converted_size_cm} см\n"
                result_text += f"Метры: {converted_size_m} м\n"
                update_text_area(result_text)
        else:
            update_text_area(f"Гвозди с названием размера '{name_size}' не найдены.\n")
    else:
        update_text_area("Название размера не было введено.\n")


def load_config(path_file: str) -> dict:
    return {
        "data": (data := json.load(open(path_file, "r", encoding="utf-8"))),
        "paints": list(map(lambda x: NitroPaint(**x) if x.get("diluents") else Paint(**x), data.get('paints', []))),
        "nails": list(map(lambda x: Nail(**x, conversion_factors=data.get('conversion_factors')), data.get('nails', []))),
    }


text_area = tk.Text(root, height=15, width=100)
text_area.grid(row=1, column=0, columnspan=6, sticky='ew', padx=10, pady=2)
def a():
    nails = generate_nails()
    text_area.insert(tk.END, "\n"* 1)
def b():
    paint = generate_paint()
    text_area.insert(tk.END, "\n" * 1)

ttk.Button(root, text="Добавить краску", command=b).grid(row=0, column=0, sticky='ew', padx=10,
                                                                              pady=5)
ttk.Button(root, text="Добавить гвозди", command=a).grid(row=0, column=2, sticky='ew', padx=10, pady=5)



ttk.Button(root, text="Конвертировать размер гвоздя по названию", command=show_converted_nail_size_by_name).grid(row=3,
                                                                                                                 column=2,
                                                                                                                 sticky='ew',
                                                                                                                 padx=10,
                                                                                                                 pady=5)
ttk.Button(root, text="Просмотреть список товаров", command=list_goods).grid(row=6, column=0,
                                                                            sticky='ew', columnspan=6,
                                                                            padx=10, pady=5)
ttk.Button(root, text="Сгенерировать поставку", command=generate_events).grid(row=7, column=0,
                                                                            sticky='ew', columnspan=6,
                                                                            padx=10, pady=5)

ttk.Button(root, text="Печать гвоздей", command=print_nails_by_size).grid(row=2, column=0, padx=10, sticky='ew', pady=5)
ttk.Button(root, text="Список цветов красок на складе", command=print_list_colors).grid(row=2, column=1, sticky='ew',
                                                                                        padx=10, pady=5)
ttk.Button(root, text="Печать цветов", command=print_colors).grid(row=2, column=2, padx=10, sticky='ew', pady=5)
ttk.Button(root, text='Список нитроэмалей с разбавителями', command=list_nitro_paints_with_diluents).grid(row=3,
                                                                                                          column=0,
                                                                                                          sticky='ew',
                                                                                                          padx=10,
                                                                                                          pady=5)
ttk.Button(root, text='Список неиспользующихся разбавителей', command=collect_unused_diluents).grid(row=3, column=1,
                                                                                                    sticky='ew',
                                                                                                    padx=10, pady=5)


style = ttk.Style()
style.theme_use('clam')

root.mainloop()


# def list_nitro_paints_with_diluents():
#     nitro_paints_with_diluents = []
#     for paint in warehouse.arr_paint:
#         if isinstance(paint, NitroPaint):
#             has_all_diluents = True
#             for diluent in paint.getDiluents():
#                 if diluent not in warehouse.known_diluents:
#                     has_all_diluents = False
#                     break
#             if has_all_diluents:
#                 nitro_paints_with_diluents.append(paint)
#     result = "Список нитроэмалей, для которых на складе есть нужные разбавители:\n"
#     for paint in nitro_paints_with_diluents:
#         result += f"Название: {paint.getName()}, Цвет: {paint.getColor()}, Количество: {paint.getCount()}\n"
#
#     return update_text_area(result)


# update_button = tk.Button(root,text='Печать гвоздей',command=print_nails_by_size)
# update_button.grid()
#
# update_button = tk.Button(root, text="Список цветов красок на складе", command=print_list_colors)
# update_button.grid()
#
# update_button = tk.Button(root, text="Печать цветов", command=print_colors)
# update_button.grid()
# button1 = tk.Button(root, text='Печать гвоздей', command=print_nails_by_size)
# button2 = tk.Button(root, text="Список цветов красок на складе", command=print_list_colors)
# button3 = tk.Button(root, text="Печать цветов", command=print_colors)
#
# # Размещаем кнопки в одной строке внизу окна
# button1.grid(row=0, column=0, padx=10, pady=10)
# button2.grid(row=0, column=1, padx=10, pady=10)
# button3.grid(row=0, column=2, padx=10, pady=10)
# add_oil_paint_button = ttk.Button(root, text="Добавить масляную краску", command=add_oil_paint)
# add_nitro_paint_button = ttk.Button(root, text="Добавить нитроэмалевую краску", command=add_nitro_paint)
# add_nails_button = ttk.Button(root, text="Добавить гвозди", command=add_nails)
#
#
# text_area = tk.Text(root, height=20, width=40)
# text_area.grid(row=1, column=0, columnspan=3, sticky='ew', padx=10, pady=10)
#
#
# button1 = tk.Button(root, text='Печать гвоздей', command=print_nails_by_size)
# button2 = tk.Button(root, text="Список цветов красок на складе", command=print_list_colors)
# button3 = tk.Button(root, text="Печать цветов", command=print_colors)
#
#
# add_oil_paint_button.grid(row=0, column=0, sticky='ew', padx=10, pady=10)
# add_nitro_paint_button.grid(row=0, column=1, sticky='ew', padx=10, pady=10)
# add_nails_button.grid(row=0, column=2, sticky='ew', padx=10, pady=10)
#
# button1.grid(row=2, column=0, padx=10, pady=10)
# button2.grid(row=2, column=1, padx=10, pady=10)
# button3.grid(row=2, column=2, padx=10, pady=10)


# def add_nitro_paint():
#     # Создаем новое окно
#     new_window = Toplevel(root)
#     new_window.title("Добавить Масляную краску")
#     new_window.geometry("250x420")
#
#     # Добавляем виджеты в новое окно
#     ttk.Label(new_window, text="Название:").pack(pady=5)
#     name = ttk.Entry(new_window)
#     name.pack(pady=5)
#
#     ttk.Label(new_window, text="Единица измерения:").pack(pady=5)
#     unit= ttk.Combobox(new_window, values=["литры"])
#     unit.pack(pady=5)
#
#     ttk.Label(new_window, text="Цвет:").pack(pady=5)
#     color = ttk.Combobox(new_window,values = ['Красный','Синий','Желтый','Фиолетовый','Белый','Черный','Зеленый'])
#     color.pack(pady=5)
#
#     ttk.Label(new_window, text="Количество:").pack(pady=5)
#     count = ttk.Entry(new_window)
#     count.pack(pady=5)
#
#     ttk.Label(new_window,text='Разбавители').pack(pady=5)
#     diluent = ttk.Entry(new_window)
#     diluent.pack(pady=5)
#
#     def process_diluents():
#         # Получение введенной строки
#         entered_diluents = diluent.get()
#         # Разделение строки по запятой
#         diluent_list = entered_diluents.split(',')
#         # Здесь можно обработать список разбавителей, например, вывести его
#         print(diluent_list)
#
#     # Кнопка для вызова функции обработки
#     process_button = ttk.Button(new_window, text="Обработать", command=process_diluents)
#     process_button.pack(pady=10)
#
#
#     add_button = ttk.Button(new_window, text="Добавить краску")
#     add_button.pack(pady=20)
#
#     nitro_paint = NitroPaint(name,unit,color,count,diluent)
#     warehouse.add_paints(nitro_paint)


# def add_oil_paint():
#     # Создаем новое окно
#     new_window = Toplevel(root)
#     new_window.title("Добавить Масляную краску")
#     new_window.geometry("250x320")
#
#     # Добавляем виджеты в новое окно
#     ttk.Label(new_window, text="Название:").pack(pady=5)
#     name = ttk.Entry(new_window)
#     name.pack(pady=5)
#
#     ttk.Label(new_window, text="Единица измерения:").pack(pady=5)
#     unit= ttk.Combobox(new_window, values=["литры"])
#     unit.pack(pady=5)
#
#     ttk.Label(new_window, text="Цвет:").pack(pady=5)
#     color = ttk.Combobox(new_window,values = ['Красный','Синий','Желтый','Фиолетовый','Белый','Черный','Зеленый'])
#     color.pack(pady=5)
#
#     ttk.Label(new_window, text="Количество:").pack(pady=5)
#     count = ttk.Entry(new_window)
#     count.pack(pady=5)
#
#     add_button = ttk.Button(new_window, text="Добавить краску")
#     add_button.pack(pady=20)
#
#     oil_paint = OilPaint(name, unit, color, count)
#     warehouse.add_paints(oil_paint)

# def add_nails():
#     conversion_factors = {
#         "mm": 1,  # Миллиметры
#         "cm": 0.1,  # Сантиметры
#         "m": 0.001,  # Меeters
#     }
#     new_window = Toplevel(root)
#     new_window.title("Добавить гвозди краску")
#     new_window.geometry("250x400")
#
#     # Добавляем виджеты в новое окно
#     ttk.Label(new_window, text="Введите название:").pack(pady=5)
#     name = ttk.Entry(new_window)
#     name.pack(pady=5)
#
#     ttk.Label(new_window, text="Единица измерения:").pack(pady=5)
#     unit= ttk.Combobox(new_window, values=["mm"])
#     unit.pack(pady=5)
#
#     ttk.Label(new_window, text="Введите размер (mm):").pack(pady=5)
#     size = ttk.Entry(new_window)
#     size.pack(pady=5)
#
#     ttk.Label(new_window, text="Количество:").pack(pady=5)
#     count = ttk.Entry(new_window)
#     count.pack(pady=5)
#
#     ttk.Label(new_window, text="Укажите наименование размера \n eng(M)+размер(mm):").pack(pady=5)
#     name_size= ttk.Entry(new_window)
#     name_size.pack(pady=5)
#
#     add_button = ttk.Button(new_window, text="Добавить гвозди")
#     add_button.pack(pady=20)
#
#     nail = Nail(name,unit,size,conversion_factors,count,name_size)
#     warehouse.add_nails(nail)


# def on_list_nitro_paints_button_click():
#     result = warehouse.list_nitro_paints_with_diluents()
#     messagebox.showinfo("Результат", "\n".join(result))
#
# def on_list_unused_diluents_button_click():
#     result = warehouse.list_unused_diluents()
#     messagebox.showinfo("Результат", "\n".join(result))

# Создание кнопок для каждой функции
# add_oil_paint_button = ttk.Button(root, text="Добавить масляную краску", command=add_oil_paint)
# add_nitro_paint_button = ttk.Button(root, text="Добавить нитроэмалевую краску", command=add_nitro_paint)
# add_nails_button = ttk.Button(root, text="Добавить гвозди", command=add_nails)
#
# # Расположение кнопок горизонтально с одинаковыми размерами и отступами
# add_oil_paint_button.grid(row=0, column=0, sticky='ew', padx=1, pady=5)
# add_nitro_paint_button.grid(row=0, column=1, sticky='ew', padx=1, pady=5)
# add_nails_button.grid(row=0, column=2, sticky='ew', padx=1, pady=5)
# text_area = tk.Text(root, height=20, width=40)
# text_area.grid(row=1, column=0, columnspan=3, sticky='ew', padx=10, pady=10)
# def show_converted_sizes():
#     selected_nail = simpledialog.askstring(title="Выберите гвоздь", prompt="Введите название гвоздя:", parent=root)
#     if selected_nail in [nail.getName() for nail in warehouse.arr_nails]:
#         for nail in warehouse.arr_nails:
#             if nail.getName() == selected_nail:
#                 sizes = nail.convert_sizes()
#                 result_text = f"Размер гвоздя {selected_nail}:\n"
#                 result_text += f"Миллиметры: {sizes['mm']} мм\n"
#                 result_text += f"Сантиметры: {sizes['cm']} см\n"
#                 result_text += f"Метры: {sizes['m']} м\n"
#                 update_text_area(result_text)
#     else:
#         update_text_area("Гвость не найден.")
#
# ttk.Button(root, text="Показать размеры гвоздя", command=show_converted_sizes).grid(row=4, column=0, padx=10, pady=10)
#
# def show_converted_nail_size():
#     size_mm = simpledialog.askfloat(title="Введите размер гвостя", prompt="Размер в миллиметрах:", parent=root)
#     if size_mm is not None:
#         converted_size_cm = nail.convert_size("cm")
#         converted_size_m = nail.convert_size("m")
#
#         result_text = f"Конвертированный размер гвостя:\n"
#         result_text += f"Сантиметры: {converted_size_cm} см\n"
#         result_text += f"Метры: {converted_size_m} м\n"
#         update_text_area(result_text)
#     else:
#         update_text_area("Размер не был введен.")
# ttk.Button(root, text="Конвертировать размер гвостя", command=show_converted_nail_size).grid(row=5, column=0, padx=10, pady=10)
