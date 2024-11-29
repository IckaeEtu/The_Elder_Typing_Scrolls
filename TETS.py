import pygame as py
import random

py.init()

# Musique
py.mixer.init()
py.mixer.music.load("data/sound/Dragonborn.mp3")
py.mixer.music.play(-1)

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
win = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("TETS The Elder Typing Scroll")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Police
FONT = py.font.Font("data/font/MorrisRomanBlack.ttf", 50)
MENU_FONT = py.font.Font("data/font/MorrisRomanBlack.ttf", 70)
TITLE_FONT = py.font.Font("data/font/MorrisRomanBlack.ttf", 80)

BACKGROUND = py.image.load("data/background/fond_scroll.jpg")

# Variables globales
Mot_actuel = ""
Lettre_actuelle = ""
Liste_mots = list()
Score = 0

def init(chemin: str) -> None:
    global Liste_mots
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            Liste_mots = [line.strip() for line in fichier]
        print(f"{len(Liste_mots)} mots ont été chargés depuis {chemin}")
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
    except IOError:
        print("Erreur d'entrée/sortie.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

def new_word():
    global Mot_actuel, Lettre_actuelle
    Mot_actuel = random.choice(Liste_mots)
    Lettre_actuelle = ""

def draw_menu():
    win.fill(WHITE)
    win.blit(BACKGROUND, (0, 0))
    menu_text = MENU_FONT.render("The Elder Typing Scroll", True, BLACK)
    start_text = FONT.render("Press ENTER to Start", True, BLACK)
    win.blit(menu_text, (WIDTH//2 - menu_text.get_width()//2, HEIGHT//4))
    win.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT//2))
    py.display.flip()

def draw_game():
    win.blit(BACKGROUND, (0, 0))
    mot_surface = FONT.render(Mot_actuel, True, BLACK)
    saisie_surface = FONT.render(Lettre_actuelle, True, BLACK)
    score_surface = FONT.render(f"Score: {Score}", True, BLACK)
    win.blit(mot_surface, (WIDTH//2 - mot_surface.get_width()//2, HEIGHT//4))
    win.blit(saisie_surface, (WIDTH//2 - saisie_surface.get_width()//2, HEIGHT//2))
    win.blit(score_surface, (10, 10))
    py.display.flip()

def main():
    global Lettre_actuelle, Score
    init("data/mot_skyrim.txt")
    new_word()
    in_menu = True

    while in_menu:
        draw_menu()
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                return
            elif event.type == py.KEYDOWN:
                if event.key == py.K_RETURN:
                    in_menu = False

    running = True
    while running:
        draw_game()
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    running = False
                elif event.key == py.K_BACKSPACE:
                    if Lettre_actuelle:
                        Lettre_actuelle = Lettre_actuelle[:-1]
                elif event.key == py.K_RETURN:
                    if Lettre_actuelle == Mot_actuel:
                        Score += 1
                        new_word()
                        Lettre_actuelle = ""
                else:
                    Lettre_actuelle += event.unicode
                    if Lettre_actuelle == Mot_actuel:
                        Score += 1
                        new_word()
                        Lettre_actuelle = ""

    py.mixer.music.stop()
    py.quit()

if __name__ == "__main__":
    main()
