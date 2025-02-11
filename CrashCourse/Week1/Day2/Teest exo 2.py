family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

    # si une personne est âgée de moins de 3 ans, le billet est gratuit.
    # s'ils sont entre 3 et 12, le billet est de 10 euros.
    # s'ils ont plus de 12 ans, le billet est de 15 dollars.

total_prix = 0
for key, value in family.items(): 
    print(f"{key} a {value} ans aujourd'hui")
    
    if value < 3:
        prix = 0
    elif value > 3 and value < 12:
        prix = 10
    else: 
        prix = 15

    # Combien chaque membre de la famille doit-il payer ?

        print(f"{key} doit payer {prix}")
    # Combien la famille doit-elle payer au total ? 
   
   
    total_prix += prix
    print(f"La famille doit payer {total_prix}")

    # Imprimez le coût total de la famille pour les films