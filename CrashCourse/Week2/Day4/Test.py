import matplotlib.pyplot as plt
import numpy as np

# Definir le range de x
x = range(0, 11)

# Definir la fonction y = x^2
y = [i**2 for i in x]

# Créer le plot
plt.plot(x, y, color ='green', linestyle = '2', market = '0')

# Ajouter le labels et title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot of y = x^2')

# ajouter la légende

# Afficher le plot
plt.show()

Build a FacetGrid using the titanic dataset to compare survival rates by age across class and gender.