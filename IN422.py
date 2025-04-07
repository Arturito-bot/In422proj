# -*- coding: utf-8 -*-
import pygame
import sys

# Initialisation de Pygame
pygame.init()
WIDTH, HEIGHT = 900, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scheduling Algorithm Visualizer")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (212, 178, 252)
PURPLE_HOVER = (230, 200, 255)
PURPLE_CLICK = (180, 150, 220)

# Police
FONT = pygame.font.SysFont("cambria", 28)
BIG_FONT = pygame.font.SysFont("cambria", 40)

# Algorithmes
algorithms = [
    "Round Robin",
    "Rate Monotonic",
    "Earliest Deadline First",
    "First-Come-First Serve",
    "Shortest Job Next"
]
selected_algorithms = set()

# État global de l'écran
current_screen = "start"
pressed_button = None

# Création des boutons
def create_buttons():
    buttons = {}
    buttons["start"] = pygame.Rect(300, 300, 300, 60)

    algo_buttons = []
    for i, name in enumerate(algorithms):
        rect = pygame.Rect(250, 80 + i * 80, 400, 50)
        algo_buttons.append((rect, name))
    buttons["algorithms"] = algo_buttons

    buttons["select_all"] = pygame.Rect(180, 550, 250, 50)
    buttons["start_simulation"] = pygame.Rect(480, 550, 250, 50)
    return buttons

buttons = create_buttons()

# Écran d’accueil
def draw_start_screen():
    SCREEN.fill(WHITE)
    title = BIG_FONT.render("Comparaison d'algorithmes", True, BLACK)
    SCREEN.blit(title, (WIDTH // 2 - title.get_width() // 2, 200))

    rect = buttons["start"]
    color = PURPLE_CLICK if pressed_button == "start" else PURPLE
    pygame.draw.rect(SCREEN, color, rect, border_radius=12)
    pygame.draw.rect(SCREEN, BLACK, rect, 2, border_radius=12)
    text = FONT.render("Commencer la comparaison", True, BLACK)
    SCREEN.blit(text, (rect.x + 25, rect.y + 15))

# Écran de sélection
def draw_selection_screen():
    SCREEN.fill(WHITE)
    header = BIG_FONT.render("Sélectionnez les algorithmes à comparer :", True, BLACK)
    SCREEN.blit(header, (WIDTH // 2 - header.get_width() // 2, 20))

    mouse_pos = pygame.mouse.get_pos()
    for rect, name in buttons["algorithms"]:
        if name in selected_algorithms:
            color = PURPLE
            border = 4
        elif rect.collidepoint(mouse_pos):
            color = PURPLE_HOVER
            border = 1
        else:
            color = PURPLE
            border = 1

        if pressed_button == name:
            color = PURPLE_CLICK

        pygame.draw.rect(SCREEN, color, rect, border_radius=12)
        pygame.draw.rect(SCREEN, BLACK, rect, border, border_radius=12)
        txt = FONT.render(name, True, BLACK)
        SCREEN.blit(txt, (rect.x + 15, rect.y + 10))

    # Bouton "Comparer tous les algorithmes"
    select_all_btn = buttons["select_all"]
    color = PURPLE_CLICK if pressed_button == "select_all" else PURPLE
    pygame.draw.rect(SCREEN, color, select_all_btn, border_radius=10)
    pygame.draw.rect(SCREEN, BLACK, select_all_btn, 1, border_radius=10)
    all_txt = FONT.render("Comparer tous les algorithmes", True, BLACK)
    SCREEN.blit(all_txt, (select_all_btn.x + 10, select_all_btn.y + 10))

    # Bouton "Lancer la simulation"
    start_sim_btn = buttons["start_simulation"]
    color = PURPLE_CLICK if pressed_button == "start_simulation" else PURPLE
    pygame.draw.rect(SCREEN, color, start_sim_btn, border_radius=10)
    pygame.draw.rect(SCREEN, BLACK, start_sim_btn, 1, border_radius=10)
    start_txt = FONT.render("Lancer la simulation", True, BLACK)
    SCREEN.blit(start_txt, (start_sim_btn.x + 30, start_sim_btn.y + 10))

# Écran de simulation
def draw_simulation_screen():
    SCREEN.fill(WHITE)
    txt = BIG_FONT.render("Comparaison en cours...", True, BLACK)
    SCREEN.blit(txt, (WIDTH // 2 - txt.get_width() // 2, HEIGHT // 2 - 30))

# Boucle principale
def main_loop():
    global current_screen, pressed_button
    clock = pygame.time.Clock()

    while True:
        pressed_button = None
        mouse_down = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_down = True
                if current_screen == "start":
                    if buttons["start"].collidepoint(mouse_pos):
                        pressed_button = "start"
                elif current_screen == "selection":
                    for rect, name in buttons["algorithms"]:
                        if rect.collidepoint(mouse_pos):
                            pressed_button = name
                    if buttons["select_all"].collidepoint(mouse_pos):
                        pressed_button = "select_all"
                    if buttons["start_simulation"].collidepoint(mouse_pos):
                        pressed_button = "start_simulation"

        # Affichage
        if current_screen == "start":
            draw_start_screen()
        elif current_screen == "selection":
            draw_selection_screen()
        elif current_screen == "simulation":
            draw_simulation_screen()

        pygame.display.flip()

        # Gestion des clics après affichage pour effet visuel
        if mouse_down and pressed_button:
            pygame.time.delay(120)

            if current_screen == "start" and pressed_button == "start":
                current_screen = "selection"

            elif current_screen == "selection":
                if pressed_button in algorithms:
                    if pressed_button in selected_algorithms:
                        selected_algorithms.remove(pressed_button)
                    else:
                        selected_algorithms.add(pressed_button)
                elif pressed_button == "select_all":
                    selected_algorithms.update(algorithms)
                elif pressed_button == "start_simulation":
                    if len(selected_algorithms) >= 2:
                        current_screen = "simulation"

        clock.tick(60)

main_loop()
