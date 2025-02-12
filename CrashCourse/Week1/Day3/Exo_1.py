class Cat:
    def __init__(self, cat_name, cat_age):
        self.age = cat_age
        self.name = cat_name

cat_1 = Cat("Mika", 23)
cat_2 = Cat("Sara", 31)
cat_3 = Cat("Olga", 38)


def oldest_cat(cats):
        oldest_age = 0
        for cat in cats:
            if cat.age > oldest_age:
               oldest_age = cat.age        
               oldest_cat = cat
        return oldest_cat

oldest = oldest_cat([cat_1, cat_2, cat_3])
print(f"The oldest cat is {oldest.name}, aged {oldest.age}.")
        
        
        

        