


sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# Le charcuterie est à court de pastrami, utiliser une boucle de temps pour éliminer toutes les occurrences de Pastrami sandwich par les sandwich-orders.
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

# Créer une liste vide appelée finished_sandwiches
finished_sandwiches = []

# Un par un, enlever chaque sandwich de la sandwich_orders tout en les ajoutant au finished_sandwiches liste.
while sandwich_orders:
    new_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(new_sandwich)
# Après que tous les sandwichs ont été fabriqués, imprimez un message répertoriant chaque sandwich qui a été fabriqué, tel que:
    print(f"J'ai fais votre {new_sandwich}")




