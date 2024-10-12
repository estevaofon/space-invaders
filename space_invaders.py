import curses
import random
import time

# Initialize the screen
screen = curses.initscr()
curses.start_color()  # Enable color functionality
curses.curs_set(0)  # Hide the cursor
screen.keypad(True)  # Enable special keys
screen.nodelay(True)  # Non-blocking input
screen.timeout(30)  # Faster refresh rate for smoother input

# Initialize color pairs
curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Magenta for alien
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)    # White for text and bullets
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)    # Green for player ship

# Get screen dimensions
height, width = screen.getmaxyx()

# Player position (starting centered)
player_x = width // 2
player_y = height - 3  # Adjusted for multi-line ship

# Bullets and Invaders
bullets = []
invaders = [[random.randint(2, width - 12), 2]]  # Random invader starting point

score = 0
game_over = False

# Control enemy movement frequency
enemy_speed = 15  # Higher means slower
frame_count = 0

# Control shooting cooldown
last_shot_time = 0
shot_cooldown = 0.3  # 300 ms between shots

# Symbols for game objects
BULLET = "|"

# Alien invader shape (ASCII art)
ALIEN_SHAPE = [
    "  ▄     ▄  ",
    "  ▄█▄▄▄█▄  ",
    "▄██▄███▄██▄",
    "█ ▀▄▄ ▄▄▀ █",
]
ALIEN_WIDTH = len(ALIEN_SHAPE[0])  # Width of the alien ASCII art

# Player ship shape (ASCII art)
PLAYER_SHIP = [
    "  ▄       ",
    "█████",
]
PLAYER_WIDTH = len(PLAYER_SHIP[1])  # Width of the second line of the ship

def draw_player():
    """Draw the player's ship in green."""
    screen.attron(curses.color_pair(3))  # Use green color for the player ship
    for i, line in enumerate(PLAYER_SHIP):
        screen.addstr(player_y + i, player_x, line)
    screen.attroff(curses.color_pair(3))

def draw_invaders():
    """Draw the invaders in magenta."""
    screen.attron(curses.color_pair(1))
    for invader in invaders:
        for i, line in enumerate(ALIEN_SHAPE):
            screen.addstr(invader[1] + i, invader[0], line)
    screen.attroff(curses.color_pair(1))

def move_invaders():
    """Move invaders downward every few frames."""
    global frame_count
    if frame_count % enemy_speed == 0:  # Move only every 'enemy_speed' frames
        for invader in invaders:
            invader[1] += 1

def draw_bullets():
    """Draw bullets in white."""
    screen.attron(curses.color_pair(2))
    for bullet in bullets:
        screen.addstr(bullet[1], bullet[0], BULLET)
    screen.attroff(curses.color_pair(2))

def move_bullets():
    """Move bullets upward."""
    global bullets
    bullets = [bullet for bullet in bullets if bullet[1] > 0]
    for bullet in bullets:
        bullet[1] -= 1

def check_collisions():
    """Check if any bullet hit an invader."""
    global bullets, invaders, score
    new_invaders = []

    for invader in invaders:
        hit = False
        for bullet in bullets:
            # Check if bullet hits any part of the alien's area
            if invader[0] <= bullet[0] < invader[0] + ALIEN_WIDTH and \
               invader[1] <= bullet[1] < invader[1] + len(ALIEN_SHAPE):
                score += 1
                hit = True  # Bullet hit the invader
                screen.addstr(invader[1], invader[0], " BOOM! ")  # Explosion effect
                break
        if not hit:
            new_invaders.append(invader)
        else:
            # Remove the bullet that hit the invader
            bullets = [b for b in bullets if not (
                invader[0] <= b[0] < invader[0] + ALIEN_WIDTH and
                invader[1] <= b[1] < invader[1] + len(ALIEN_SHAPE)
            )]

    invaders = new_invaders

def spawn_invader():
    """Spawn a new invader within screen boundaries."""
    x_position = random.randint(2, width - ALIEN_WIDTH - 1)  # Ensure within screen
    invaders.append([x_position, 2])

# Game loop
while not game_over:
    screen.clear()

    # Draw objects
    draw_player()
    draw_invaders()
    draw_bullets()

    # Display score
    screen.attron(curses.color_pair(2))
    screen.addstr(0, 2, f"Score: {score}")
    screen.attroff(curses.color_pair(2))

    # Handle input
    key = screen.getch()
    current_time = time.time()

    if key != -1:  # A key was pressed
        if key == curses.KEY_LEFT and player_x > 1:
            player_x -= 1
        elif key == curses.KEY_RIGHT and player_x < width - PLAYER_WIDTH - 1:
            player_x += 1
        elif key == ord(' ') and current_time - last_shot_time >= shot_cooldown:
            # Shoot a bullet from the center of the second line of the ship
            bullet_x = player_x + PLAYER_WIDTH // 2
            bullets.append([bullet_x, player_y - 1])  # Fire bullet
            last_shot_time = current_time

    # Move objects
    move_bullets()
    move_invaders()

    # Check collisions
    check_collisions()

    # Spawn new invader randomly
    if random.randint(1, 50) == 1:  # Reduced spawn rate
        spawn_invader()

    # Check for game over
    if any(invader[1] + len(ALIEN_SHAPE) >= height - 2 for invader in invaders):
        game_over = True

    # Increment the frame counter
    frame_count += 1

    screen.refresh()
    time.sleep(0.03)  # Faster loop for smoother gameplay

# Game over screen
screen.clear()
screen.addstr(height // 2, width // 2 - 5, "GAME OVER")
screen.addstr(height // 2 + 1, width // 2 - 10, f"Final Score: {score}")
screen.refresh()
time.sleep(3)

# End the game
curses.endwin()
