import time
import board
import busio
from adafruit_character_lcd.character_lcd_i2c import Character_LCD_I2C

# LCD configuration
lcd_columns = 16
lcd_rows = 2

# Initialize I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the LCD display
lcd = Character_LCD_I2C(i2c, lcd_columns, lcd_rows)

def clear_display():
    """Clear the LCD display."""
    lcd.clear()

def show_message(line1, line2=""):
    """
    Display a message on the LCD.

    Args:
        line1 (str): Text for the first line (max 16 characters).
        line2 (str): Text for the second line (max 16 characters).
    """
    lcd.clear()
    lcd.message = f"{line1[:16]}\n{line2[:16]}"
    time.sleep(1)  # Optional: Pause for readability

def display_round_info(round_num, current_player):
    """
    Display the current round and player on the LCD.

    Args:
        round_num (int): The current round number.
        current_player (str): Name of the current player.
    """
    line1 = f"Round: {round_num}"
    line2 = f"Player: {current_player}"
    show_message(line1, line2)

def display_leaderboard(players):
    """
    Display the leaderboard on the LCD.

    Args:
        players (list): List of player dictionaries with 'name' and 'score'.
    """
    for player in sorted(players, key=lambda x: x['score'], reverse=True):
        name = player['name'][:10]  # Limit to 10 characters
        score = player['score']
        show_message(name, f"Score: {score}")
        time.sleep(2)  # Display each player for 2 seconds
