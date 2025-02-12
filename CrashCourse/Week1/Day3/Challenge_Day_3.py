class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}  # Dico
    def add_animal(self, animal, count=1):
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count
    def get_animal_types(self):
        return sorted(self.animals.keys())
    def get_short_info(self):
        animal_types = ", ".join(self.get_animal_types())
        return f"{self.name} is a farm with {animal_types}."
    def print_animals(self):
        print(f"Animals in {self.name}:")
        for animal, count in sorted(self.animals.items()):
            print(f"{animal}: {count}")
macdonald_farm = Farm("McDonald’s Farm")
macdonald_farm.add_animal("Cow", 5)
macdonald_farm.add_animal("Sheep", 2)
macdonald_farm.add_animal("Goat", 4)
macdonald_farm.add_animal("Cow", 2)
macdonald_farm.print_animals()
print(macdonald_farm.get_animal_types())
print(macdonald_farm.get_short_info())









