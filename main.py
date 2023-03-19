import random

# Liste des mots à trouver pour chaque difficulté
easy_words = ['chat', 'chien', 'lion', 'oiseau', 'lapin', 'souris']
medium_words = ['girafe', 'tortue', 'elephant', 'rhinoceros', 'crocodile', 'hippopotame']
hard_words = ['caméléon', 'ornithorynque', 'okapi', 'kangourou', 'cacatoes', 'pélican']

# Fonction pour générer une grille de lettres aléatoire
def generate_grid(rows, cols):
    # Liste de toutes les lettres possibles
    letters = 'abcdefghijklmnopqrstuvwxyz'
    # Création de la grille vide
    grid = [[' ' for c in range(cols)] for r in range(rows)]
    # Ajout de lettres aléatoires dans chaque case de la grille
    for r in range(rows):
        for c in range(cols):
            grid[r][c] = random.choice(letters)
    return grid

def print_grid(grid):
    # En-tête de colonnes (abscisses)
    header = '  '
    for c in range(len(grid[0])):
        header += str(c) + ' '
    print(header)
    # Lignes de la grille avec numéros d'ordonnées et lettres
    for r in range(len(grid)):
        row_str = str(r) + ' '
        for c in range(len(grid[0])):
            row_str += grid[r][c] + ' '
        print(row_str)
# Fonction pour afficher la grille de lettres
def display_grid(grid):
    for row in grid:
        print(' '.join(row))

# Fonction pour trouver les mots dans la grille
def find_words(grid, words):
    found_words = []
    rows = len(grid)
    cols = len(grid[0])
    # Parcours de chaque mot dans la liste des mots
    for word in words:
        word_found = False
        # Parcours de chaque case de la grille
        for r in range(rows):
            for c in range(cols):
                # Si la première lettre du mot est trouvée dans la case de la grille
                if grid[r][c] == word[0]:
                    # Vérification des lettres suivantes dans les cases voisines
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == dc == 0:
                                continue
                            # Concaténation des lettres voisines pour former un mot potentiel
                            potential_word = grid[r][c]
                            nr, nc = r + dr, c + dc
                            while 0 <= nr < rows and 0 <= nc < cols:
                                potential_word += grid[nr][nc]
                                # Si le mot potentiel correspond au mot cherché
                                if potential_word == word:
                                    found_words.append(word)
                                    word_found = True
                                    break
                                # Sinon, on continue avec les lettres suivantes
                                nr += dr
                                nc += dc
                            if word_found:
                                break
                        if word_found:
                            break
                if word_found:
                    break
    return found_words

# Fonction pour afficher la liste des mots à trouver
def display_words(words):
    print('Mots à trouver:')
    for word in words:
        print('- ' + word)


def main_menu():
    # Affichage du menu
    print('=== Mot mêlé ===')
    print('1. Facile')
    print('2. Moyen')
    print('3. Difficile')
    print('4. Quitter')

    # Initialisation du choix de l'utilisateur
    choice = None

    while choice != '4':
        # Lecture du choix de l'utilisateur
        choice = input('Choisissez une difficulté (1-4): ')

        # Vérification du choix de l'utilisateur
        if choice == '1':
            # Difficulté facile
            grid = generate_grid(5, 10)
            words = easy_words
        elif choice == '2':
            # Difficulté moyenne
            grid = generate_grid(7, 15)
            words = medium_words
        elif choice == '3':
            # Difficulté difficile
            grid = generate_grid(15, 30)
            words = hard_words
        elif choice == '4':
            # Quitter
            return
        else:
            # Choix invalide
            print('Choix invalide. Veuillez choisir une difficulté entre 1 et 4.')
            continue

        # Affichage de la grille de lettres
        print('Grille de lettres:')
        display_grid(grid)

        # Affichage des mots à trouver
        display_words(words)

        # Recherche des mots dans la grille
        found_words = find_words(grid, words)
        # Test
        verif_mot(grid)
        # Affichage des mots trouvés
        print('Mots trouvés:')
        for word in found_words:
            print('- ' + word)

    # Sortie de la boucle while et fin de la fonction main_menu()


def verif_mot(grid):
    mot = input("rentrer votre mot: ")
    direction = input(" 'horizontal' ou 'vertical' ? ")
    x = int(input("rentrer votre coordonne x: "))
    y = int(input("rentrer votre coordonne y: "))

    rows = len(grid)
    cols = len(grid[0])

    if direction == 'horizontal':
        if y + len(mot) > cols:
            print('Le mot dépasse la grille')
            return

        for i in range(len(mot)):
            if grid[x][y+i] != mot[i]:
                print('Le mot n\'est pas dans la grille')
                return

        print('Le mot est dans la grille')

    elif direction == 'vertical':
        if x + len(mot) > rows:
            print('Le mot dépasse la grille')
            return

        for i in range(len(mot)):
            if grid[x+i][y] != mot[i]:
                print('Le mot n\'est pas dans la grille')
                return

        print('Le mot est dans la grille')

    else:
        print('Direction invalide')

    # On vérifie si les coordonnées sont valides
    if x < 0 or y < 0:
        return False

    # On vérifie si le mot dépasse la limite de la grille
    if (direction == 'horizontal' and y + len(mot) > len(grid[x])) or (
            direction == 'vertical' and x + len(mot) > len(grid)):
        return False

    # On vérifie si les lettres du mot correspondent à la liste
    for i in range(len(mot)):
        if direction == 'horizontal':
            if grid[x][y + i] != mot[i]:
                return False
        elif direction == 'vertical':
            if grid[x + i][y] != mot[i]:
                return False

    # Si toutes les vérifications ont été passées, le mot est valide
    return True


# Lancement du jeu
main_menu()
