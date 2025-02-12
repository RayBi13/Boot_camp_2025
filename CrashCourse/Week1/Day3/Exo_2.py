class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self) :
      print(f"{self.name} goes woof!")
    def jump(self) :
        # for animal in self.animals :
        print(f"{self.name} jumps {self.height*2} cm high!")
    
    

david_dog = Dog("Rex", 50)
david_dog.bark()
david_dog.jump()

sara_dog = Dog("Teacup", 20)
sara_dog.bark()
sara_dog.jump()

if david_dog.height > sara_dog.height :
    print(f"{david_dog.name} is taller than {sara_dog.name}")

# cat_1 = Cat("Mika", 23)
# cat_2 = Cat("Sara", 31)
# cat_3 = Cat("Olga", 38)


# def oldest_cat(cats):
#         oldest_age = 0
#         for cat in cats:
#             if cat.age > oldest_age:
#                oldest_age = cat.age        
#                oldest_cat = cat
#         return oldest_cat