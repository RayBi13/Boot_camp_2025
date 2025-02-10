# Retirer Bananade la liste.
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Retirer Blueberriesde la liste
basket.remove("Blueberries")
print(basket)
# Ajouter Kiwijusqu'à la fin de la liste
print(basket + ["Kiwi"])
# Ajouter Applesau début de la liste
basket.insert(0,"Apples")
print(basket)
# Comptez combien de pommes se trouvent dans le panier.
count = basket.count('Apples')
print(count)
# Vader le panier.
clear_basket = basket.clear()
print(clear_basket)