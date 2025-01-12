from arcade_display import (
    show_loading_screen,
    transition_animation,
    draw_leaderboard,
    draw_player_turn,
    show_current_leaderboard, 
    screen,
    BACKGROUND_GAME,
    clock,
)
import pygame
import sys


def get_player_names():
    """Prompt for player names and return a list of players."""
    players = []
    num_players = int(input("Enter the number of players (1-10): "))
    for i in range(num_players):
        name = input(f"Enter the name of player {i + 1}: ")
        players.append({"name": name, "score": 0})
    return players


def simulate_input():
    """Simulate sensor input for testing."""
    return int(input("Enter a sensor input (1-10, or 0 to quit): "))


def main():
    # Show the loading screen
    show_loading_screen()

    # Transition animation
    transition_animation()

    # Example Players
    players = get_player_names()
    target_score = int(input("Set the target score to win the game: "))
    round_num = 1
    winner = None

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for player in players:
            # Clear screen and draw background
            screen.blit(BACKGROUND_GAME, (0, 0))

            # Show player turn
            draw_player_turn(player['name'])

            # Simulate sensor input (or replace with hardware input later)
            input_id = simulate_input()
            if input_id == 0:
                print("Exiting game.")
                pygame.quit()
                sys.exit()

            # Update score (simulate logic for bonus points)
            player['score'] += input_id * 10
            if input_id == 10:
                player['score'] += 500

            # Check for winner
            if player['score'] >= target_score:
                winner = player['name']
                break

            # Update leaderboard
                waiting = True
            show_current_leaderboard(players)
            pygame.display.flip()
            clock.tick(60)

        if winner:
            print(f"🎉 {winner} wins the game! 🎉")
            break

        round_num += 1

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
