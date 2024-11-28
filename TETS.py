import pygame as py
import random

py.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
win = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Typing Game")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Police
FONT = py.font.SysFont('comicsans', 50)

# Variables globales
Mot_acuel = ""
Lettre_actuelle = ""
Liste_mots = list()

def init(chemin:str) -> None:
    global Liste_mots
    try:
        fichier = open(chemin, "r", encoding="utf-8")
        for line in fichier.readlines():
            Liste_mots.append(line.strip("\n"))
        fichier.close()
        
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
    except IOError:
        print("Erreur d'entrée/sortie.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

def new_word():
    global Mot_acuel, Lettre_actuelle
    Mot_acuel = random.choice(Liste_mots)
    Lettre_actuelle = ""

#def del_last_letter():

init("liste_mot_fr.txt")
new_word()

running = True
while running:
    win.fill(WHITE)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                running = False
            elif event.key == py.K_BACKSPACE:
                if Lettre_actuelle != None and len(Lettre_actuelle) >= 1:
                    Lettre_actuelle = Lettre_actuelle[:-1]
            elif event.key == py.K_RETURN:
                if Lettre_actuelle == Mot_acuel:
                    new_word()
            else:
                Lettre_actuelle += event.unicode
                print(Lettre_actuelle)
                print(Mot_acuel)
                if Lettre_actuelle == Mot_acuel:
                    new_word()

    # Affichage du mot actuel et de la saisie utilisateur
    mot_surface = FONT.render(Mot_acuel, True, BLACK)
    saisie_surface = FONT.render(Lettre_actuelle, True, BLACK)
    win.blit(mot_surface, (WIDTH//2 - mot_surface.get_width()//2, HEIGHT//4))
    win.blit(saisie_surface, (WIDTH//2 - saisie_surface.get_width()//2, HEIGHT//2))

    py.display.flip()

py.quit()
