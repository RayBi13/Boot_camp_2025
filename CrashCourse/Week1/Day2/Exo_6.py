
def make_shirt(size="large", text="I love Python"):
    """..."""
    print(f"La taille de la chemise est {size} et le texte est '{text}'.")

# appel de la fonction large shirt avec message par defaut
make_shirt()

# appel de la fonction medium shirt avec message par defaut
make_shirt(size="medium")

# appel de la fonction pour nimporte quelle taille de chemises
make_shirt(size="small", text="Python is awesome")

# Bonus: appel de la fonction pour une taille de chemise extra large
make_shirt(text="Custom message", size="extra large")
