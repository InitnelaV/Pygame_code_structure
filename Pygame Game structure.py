"""
Template d'organisation pour un jeu sous Pygame
Ce fichier sert de trame pour structurer un projet avec des sections bien définies.
"""

# === Importation des modules ===
import pygame
import sys

# === Initialisation de Pygame ===
pygame.init()

# === Paramètres du jeu ===
WIDTH, HEIGHT = 800, 600  # Dimensions de la fenêtre
FPS = 60  # Fréquence d'images par seconde

# === Couleurs ===
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# === Création de la fenêtre ===
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mon Jeu Pygame")
clock = pygame.time.Clock()

# === Chargement des ressources ===
# Ex : images, sons, polices

def load_assets():
    """Charge les ressources du jeu (images, sons, polices, etc.)."""
    pass

# === Définition des classes ===
class Player(pygame.sprite.Sprite):
    """Classe représentant le joueur."""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))

    def update(self):
        """Met à jour la position et l'état du joueur."""
        pass

# === Initialisation des éléments du jeu ===
def setup():
    """Initialise les éléments du jeu (joueurs, ennemis, objets, etc.)."""
    global player, all_sprites
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

# === Boucle principale du jeu ===
def game_loop():
    """Boucle principale qui gère les événements, la mise à jour et l'affichage."""
    running = True
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mise à jour des éléments du jeu
        all_sprites.update()

        # Affichage
        screen.fill(BLACK)  # Fond d'écran
        all_sprites.draw(screen)
        pygame.display.flip()

        # Contrôle de la cadence
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# === Lancement du jeu ===
if __name__ == "__main__":
    load_assets()
    setup()
    game_loop()
