class Thing:
    def __init__(self, name, unit_of_measurement, count):
        self.name = name
        self.unit_of_measurement = unit_of_measurement
        self.count = count

    def getName(self):
        return self.name

    def getUnit(self):
        return self.unit_of_measurement

    def getCount(self):
        return self.count


class Paint(Thing):
    def __init__(self, name, unit, color, paint_type, count, volume=0):
        super().__init__(name, unit, count)
        self.color = color
        self.paint_type = paint_type
        self.volume = volume

    def getColor(self):
        return self.color

    def getPaint_type(self):
        return self.paint_type

    def getVolume(self):
        return self.volume

    def setVolume(self, new_volume):
        self.volume = new_volume

    def setUnit(self, new_unit):
        self.unit_of_measurement = new_unit

    def setCount(self, new_count):
        self.count = new_count

    def calculate_total_volume(self):
        return self.volume * self.count

    def is_paint(self):
        return True


class OilPaint(Paint):
    def __init__(self, name, unit, color, count, volume=0):
        super().__init__(name, unit, color, "Oil", count, volume)

    def getColor(self):
        return self.color


class NitroPaint(Paint):
    def __init__(self, name, unit, color, count, diluents, volume=0):
        super().__init__(name, unit, color, "Nitro", count, volume)
        self.diluents = diluents

    def getDiluents(self):
        return self.diluents





class Nail(Thing):
    def __init__(self, name, unit_of_measurement, size, conversion_factors, count, name_size):
        super().__init__(name, unit_of_measurement, count)
        self.size = size
        self.conversion_factors = conversion_factors
        self.name_size = name_size

    def convert_size(self, target_unit):
        if target_unit in self.conversion_factors:
            size_float = float(self.size)
            return size_float * self.conversion_factors[target_unit]
        else:
            print(f"Перевод в {target_unit} невозможен.")
            return None

    def convert_sizes(self):
        sizes = {"mm": self.size, "cm": self.convert_size("cm"), "m": self.convert_size("m")}
        return sizes

    def getSize(self):
        return self.size

    def getName_size(self):
        return self.name_size

# class Diluent(Paint):
#     def __init__(self, name, unit, count):
#         super().__init__(name, unit, count, "Diluent", count)
#
#     def getName(self):
#         return self.name
#
#     def getCount(self):
#         return self.count
#
#     def getType(self):
#         return self.paint_type