import random

def get_random_temp(season):
    """Returns a random temperature based on the season."""
    if season == "hiver":
        return random.uniform(-10, 16)
    elif season == "printemps":
        return random.uniform(0, 23)
    elif season == "été":
        return random.uniform(24, 40)
    elif season == "automne":
        return random.uniform(0, 23)
    else:
        raise ValueError("Saison invalide. Veuillez entrer 'hiver', 'printemps', 'été' ou 'automne'.")

def main():
    """fonction pour temperature."""
    saison = input("Entrez une saison (hiver, printemps, été, automne): ").strip().lower()
    temp = get_random_temp(saison)
    print(f"La température actuelle est de {temp:.2f} degrés Celsius.")

    if temp < 0:
        print("Brrr, c’est gel. Porter quelques couches supplémentaires aujourd'hui.")
    elif 0 <= temp < 16:
        print("Très froid. N'oubliez pas votre manteau !")
    elif 16 <= temp < 24:
        print("Il fait frais. Une veste légère devrait suffire.")
    elif 24 <= temp < 32:
        print("Il fait chaud. Portez des vêtements légers.")
    elif 32 <= temp <= 40:
        print("Il fait très chaud. Restez hydraté et évitez de sortir pendant les heures les plus chaudes.")

if __name__ == "__main__":
    main()