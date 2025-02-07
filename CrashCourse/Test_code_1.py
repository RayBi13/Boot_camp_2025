# my_string = "i am shooting"
# # print (my_string.upper())

# new_string = "I AM SHOOTING" + my_tring[0:0]
# print(new_string)


# 1.
# Nom = "Alice"

# Age = 30

# Ville = "New York"

# print(f"Bonjour {Nom}. Vous avez {Age} et vivez à {Ville}.")


# age = int(input('Please state your age: '))
# years_until_100 = 100 - age
# print(f"Vous aurez 100 en {years_until_100} ans.")

# Demandez à l'utilisateur son âge en utilisant input()et le ranger à un âge variable.

# Convertir l'âge entré en nombre entier et calculer le nombre d'années jusqu'à ce qu'ils deviennent 100.

# Afficher un message: "Vous aurez 100 en X ans", où X est le nombre d'années calculés.
# Here is a table of prices for a wedding catering company:

# of guests	price
# Up to 50 people	$4,000
# Up to 100 people	$10,000
# Up to 200 people	$15,000
# More than 200 people	$20,000

# 📝 Instructions:

# Please write an program that asks the user for the number of people attending their wedding and prints the corresponding price in the console.
# For example, if the user says that 20 people are attending to the wedding, it must cost $4,000 dollars.
# Ask the user for the number of people attending their wedding
num_guests = int(input("Please enter the number of people attending the wedding: "))

# Determine the price based on the number of guests
if num_guests <= 50:
    price = 4000
elif num_guests <= 100:
    price = 10000
elif num_guests <= 200:
    price = 15000
else:
    price = 20000

# Print the corresponding price
print(f"The cost for catering the wedding is ${price}.")