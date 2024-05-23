

from products import Nail, OilPaint, NitroPaint, Paint
from sklad import Warehouse
import json
def load_config(path_file: str) -> dict:
    return {
        "data": (data := json.load(open(path_file, "r", encoding="utf-8"))),
        "paints": list(map(lambda x: NitroPaint(**x) if x.get("diluents") else Paint(**x), data.get('paints', []))),
        "nails": list(map(lambda x: Nail(**x, conversion_factors=data.get('conversion_factors')), data.get('nails', []))),
    }



warehouse = Warehouse('Cклад товаров')
config = load_config('config.json')
warehouse.set_paints(config['paints'])
warehouse.set_nails(config['nails'])
warehouse.set_thing([*config['paints'], *config['nails']])
warehouse.generate_events()



# #Количество краски заданного цвета, в том числе с разбивкой на масляные и нитроэмали.
warehouse.print_colors()
# #Список цветов красок, имеющихся на складе, в том числе с разбивкой на масляные и нитроэмали.
warehouse.print_list_colors()
# Список всех товаров на складе с указанием их количества и единиц измерения. У всех товаров, единица измерения которых приводится к базовой, количество должно быть выведено в базовых единицах измерения. Список может быть отсортирован по наименованию товаров, по типам товаров
warehouse.list_goods(sort_by='name')
#количество гвоздей данного размера
warehouse.print_nails_by_size('M2')
warehouse.print_nails_by_size('M1')
warehouse.print_nails_by_size('M4')
#Список нитроэмалей, для которых на складе есть нужные разбавители.
warehouse.list_nitro_paints_with_diluents()
#Список разбавителей, которые не используются в красках, находящихся на складе.
warehouse.collect_unused_diluents()
warehouse.list_goods()

# warehouse.show_converted_nail_size_by_name(warehouse.get_nails()[0].getName_size())