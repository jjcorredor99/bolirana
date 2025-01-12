import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bolirana Game Display")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Fonts
FONT_LARGE = pygame.font.Font(None, 72)
FONT_MEDIUM = pygame.font.Font(None, 48)
FONT_SMALL = pygame.font.Font(None, 36)

# Background Images
BACKGROUND_LOADING = pygame.image.load("../assets/imgs/loading.jpg")  # Replace with a proper loading screen image
BACKGROUND_LOADING = pygame.transform.scale(BACKGROUND_LOADING, (SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND_GAME = pygame.image.load("../assets/imgs/game.jpg")  # Replace with a game interface image
BACKGROUND_GAME = pygame.transform.scale(BACKGROUND_GAME, (SCREEN_WIDTH, SCREEN_HEIGHT))

LEADERBOARD_GAME = pygame.image.load("../assets/imgs/leaderboard.jpg")  # Replace with a game interface image
LEADERBOARD_GAME = pygame.transform.scale(LEADERBOARD_GAME, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Game Clock
clock = pygame.time.Clock()


def show_loading_screen():
    """
    Display the loading screen with a start button.
    """
    screen.blit(BACKGROUND_LOADING, (0, 0))
    title = FONT_LARGE.render("Welcome to Bolirana!", True, YELLOW)
    start_text = FONT_MEDIUM.render("Press SPACE to Start", True, WHITE)
    screen.blit(title, (200, 200))
    screen.blit(start_text, (250, 400))
    pygame.display.flip()

    # Wait for user to press the spacebar
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False


def show_current_leaderboard(players):
    """
    Display the current leaderboard on the screen.

    Args:
        players (list): List of player dictionaries with 'name' and 'score'.
    """
    screen.blit(LEADERBOARD_GAME, (0, 0))
    draw_leaderboard(players)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False
def transition_animation():
    """
    Display a vintage-style transition animation.
    """
    for alpha in range(0, 255, 10):  # Fade-in effect
        screen.fill(BLACK)
        background = LEADERBOARD_GAME.copy()
        background.set_alpha(alpha)
        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(30)



def draw_player_turn(player_name):
    """
    Display the message indicating it's a player's turn.

    Args:
        player_name (str): Name of the current player.
    """
    screen.blit(LEADERBOARD_GAME, (0, 0))
    turn_text = FONT_LARGE.render(f"{player_name}'s Turn", True, BLUE)
    screen.blit(turn_text, (200, 300))
    pygame.display.flip()


def draw_leaderboard(players):
    """
    Draw the leaderboard on the screen.

    Args:
        players (list): List of player dictionaries with 'name' and 'score'.
    """
    sorted_players = sorted(players, key=lambda x: x['score'], reverse=True)
    leaderboard_x = 50
    leaderboard_y = 100

    # Title
    title = FONT_LARGE.render("Leaderboard", True, YELLOW)
    screen.blit(title, (leaderboard_x, leaderboard_y - 50))

    # Player Scores
    for i, player in enumerate(sorted_players):
        player_text = FONT_MEDIUM.render(f"{i + 1}. {player['name']} - {player['score']} pts", True, WHITE)
        screen.blit(player_text, (leaderboard_x, leaderboard_y + i * 50))
