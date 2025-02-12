class Zoo:
    def __init__(self, name):
      self.name = name
      self.animal = []

    def add_animal(self, new_animal):
       if new_animal not in self.new_animal:
           self.animal.append(new_animal)


    def get_animals(self):
        print(self.animal)

    def sell_animal(self, animal_sold):
        self.animal.remove(animal_sold)
        

    def sort_animals(self):
        self.animal.sort()

        def sort_animals(animals):
            sorted_animals = sorted(animals)
    grouped_animals = {}
    
    for animal in sorted_animals:
        first_letter = animal[0].upper()
        if first_letter not in grouped_animals:
            grouped_animals[first_letter] = []
        grouped_animals[first_letter].append(animal)
    
     return grouped_animals

    def main():
            animals = ["elephant", "dog", "cat", "antelope", "bear", "alligator", "cheetah"]
            grouped_animals = sort_animals(animals)
    for letter, group in grouped_animals.items():
        print(f"{letter}: {group}")
