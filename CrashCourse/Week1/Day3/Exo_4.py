class Zoo:
    def __init__ (self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)      
    def get_animals(self):
        print (self.animals)
    def sell_animal(self, animal_sold):
        self.animals.remove(animal_sold)
    def sort_animals(self):
        self.animals.sort()
        grouped_animals = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)
        return grouped_animals
zoo = Zoo("my_zoo")
animals_list = ["Zebra", "Antelope", "Lion", "Tiger", "Leopard", "Elephant", "Giraffe"]
for animal in animals_list:
    zoo.add_animal(animal)
print(zoo.sort_animals())