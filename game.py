import random

# ============================================================================
# CONSTANTS
# ============================================================================

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 40
PLAYER_SPEED = 6

BULLET_WIDTH = 4
BULLET_HEIGHT = 10
BULLET_SPEED = 10

ENEMY_WIDTH = 40
ENEMY_HEIGHT = 30
ENEMY_SPEED = 2         # How fast they fall
ENEMY_SPAWN_RATE = 60   # Frames between spawns

STARTING_LIVES = 3
POINTS_PER_ENEMY = 10


def clamp_position(x):
    if x < 0:
        return 0
    if x > SCREEN_WIDTH - PLAYER_WIDTH:
        return SCREEN_WIDTH - PLAYER_WIDTH
    return x


def move_player_safe(x, direction, speed):
    if direction == "right":
        new_x = x + speed
    else:
        new_x = x - speed
    return clamp_position(new_x)


def move_bullet(bullet_y, speed):
    return bullet_y - speed


def is_bullet_off_screen(bullet_y):
    return bullet_y < 0



def update_all_bullets(bullets):
    # Move all bullets up (each bullet is a dict with 'x' and 'y')
    for b in bullets:
        b['y'] = move_bullet(b['y'], BULLET_SPEED)
    # Keep only on-screen bullets
    on_screen = []
    for b in bullets:
        if not is_bullet_off_screen(b['y']):
            on_screen.append(b)
    return on_screen


def should_spawn_enemy(frame_count, spawn_rate):
    return frame_count % spawn_rate == 0

 
# in class

def move_enemy_down(enemy_y, speed):
    """
    Move enemy DOWN (y increases).
    Opposite of bullets! Return new y position.
    """
    return enemy_y + speed


def is_enemy_off_screen(enemy_y):
    """
    Check if enemy reached the bottom.
    Return True if enemy_y > SCREEN_HEIGHT
    """
    return enemy_y > SCREEN_HEIGHT


def check_collision(x1, y1, w1, h1, x2, y2, w2, h2):
    """
    Rectangle collision detection.
    Return True if rectangles overlap, False otherwise.
    """
    if x1 > x2 + w2 or x1 + w1 < x2 or y1 > y2 + h2 or y1 + h1 < y2:
        return False
    return True


def calculate_score(points_per_enemy):
    """Return points for destroying enemy."""
    return points_per_enemy


def check_game_over(lives):
    """Check if game is over. Return True if lives <= 0"""
    return lives <= 0


def lose_life(current_lives):
    """Subtract one life. Don't go below 0."""
    return max(current_lives - 1, 0)


# fill these in for them

def create_enemy_at_top():
    """Create enemy at random x position at top of screen."""
    random_x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
    return {'x': random_x, 'y': -ENEMY_HEIGHT, 'alive': True}


def get_living_enemies(enemies):
    """Filter to only living enemies."""
    return [e for e in enemies if e['alive']]


def count_alive_enemies(enemies):
    """Count living enemies."""
    return len(get_living_enemies(enemies))


def remove_escaped_enemies(enemies):
    """
    Remove enemies that reached bottom.
    Returns: (filtered_enemies, number_that_escaped)
    """
    still_here = [e for e in enemies if not is_enemy_off_screen(e['y'])]
    num_escaped = len(enemies) - len(still_here)
    return still_here, num_escaped


def check_bullet_hits_enemies(bullets, enemies):
    """
    Check all bullet-enemy collisions.
    Returns: (updated_bullets, updated_enemies, hits_count)
    """
    remaining_bullets = []
    hits = 0

    for b in bullets:
        hit_something = False
        for e in enemies:
            if e['alive'] and check_collision(
                b['x'], b['y'],
                BULLET_WIDTH, BULLET_HEIGHT,
                e['x'], e['y'],
                ENEMY_WIDTH, ENEMY_HEIGHT
            ):
                e['alive'] = False
                hit_something = True
                hits += 1
                break
        if not hit_something:
            remaining_bullets.append(b)

    return remaining_bullets, enemies, hits


def check_player_hit_by_enemy(player_x, player_y, enemies):
    """
    Check if any living enemy hit the player.
    Returns: True if hit, False otherwise
    """
    for e in enemies:
        if e['alive'] and check_collision(
            player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT,
            e['x'], e['y'], ENEMY_WIDTH, ENEMY_HEIGHT
        ):
            return True
    return False
