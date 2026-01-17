# ============================================
#         MY SPACE SHOOTER SETTINGS
# ============================================
#
# WORKSHOP 1: This is YOUR game! Customize it!
#
# Change these values to make the game your own.
# Save the file and run the game to see your changes!
#
# ============================================

# ----- GAME INFO -----
GAME_TITLE = "Space Shooter"  # Change this to your game's name!

# ----- WINDOW SIZE -----
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# ----- COLOR PALETTE -----
# Base colors (Red, Green, Blue) each 0-255
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Nice game colors (feel free to tweak!)
SPACE_BLUE = (8, 12, 30)           # Dark blue space background
STAR_WHITE = (220, 230, 255)       # Slightly blue-white stars
STAR_YELLOW = (255, 250, 200)      # Warm yellow stars
NEON_CYAN = (0, 255, 255)          # Bright cyan
NEON_PINK = (255, 50, 150)         # Hot pink
NEON_GREEN = (50, 255, 100)        # Bright green
LASER_BLUE = (100, 200, 255)       # Light blue for bullets
ENEMY_RED = (255, 60, 60)          # Bright red for enemies
ENEMY_ORANGE = (255, 150, 50)      # Orange enemy variant
ENEMY_PURPLE = (180, 80, 255)      # Purple enemy variant
HUD_GREEN = (100, 255, 150)        # HUD text color
EXPLOSION_YELLOW = (255, 220, 100) # Explosion particles
EXPLOSION_ORANGE = (255, 150, 50)  # Explosion particles

# Create your own color!
MY_COLOR = (100, 200, 255)  # Change these numbers!


# ============================================
# PLAYER SETTINGS
# ============================================

PLAYER_COLOR = NEON_CYAN           # Main ship color
PLAYER_ACCENT = WHITE              # Ship accent/cockpit color
PLAYER_ENGINE = ORANGE             # Engine glow color

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 40
PLAYER_SPEED = 6

# Where does the player start?
PLAYER_START_X = 325
PLAYER_START_Y = 420


# ============================================
# GAME RULES
# ============================================

STARTING_LIVES = 3
STARTING_HEALTH = 100
POINTS_PER_ENEMY = 10


# ============================================
# BULLET SETTINGS
# ============================================

BULLET_SPEED = 10
BULLET_WIDTH = 4
BULLET_HEIGHT = 12
BULLET_COLOR = LASER_BLUE
BULLET_GLOW = (150, 220, 255)      # Outer glow color
FIRE_DELAY = 150                   # Milliseconds between shots


# ============================================
# ENEMY SETTINGS
# ============================================

ENEMY_WIDTH = 40
ENEMY_HEIGHT = 35
ENEMY_SPEED = 3
ENEMY_COLOR = ENEMY_RED
ENEMY_SPAWN_RATE = 0.025           # 2.5% chance each frame


# ============================================
# VISUAL EFFECTS
# ============================================

# Background
BG_COLOR = SPACE_BLUE

# Stars (layered parallax)
STAR_COUNT_FAR = 40                # Distant stars (slow)
STAR_COUNT_MID = 25                # Medium stars
STAR_COUNT_NEAR = 15               # Close stars (fast)

# Particles
PARTICLE_COUNT = 12                # Particles per explosion
PARTICLE_LIFETIME = 30             # Frames particles last
PARTICLE_SPEED = 4                 # How fast particles spread


# ============================================
# OTHER SETTINGS
# ============================================

FPS = 60  # Frames per second (game speed)


# ============================================
#   FUN EXPERIMENTS TO TRY:
#
#   1. Change GAME_TITLE to something epic
#   2. Try PLAYER_COLOR = NEON_PINK
#   3. Set ENEMY_SPEED = 5 for harder game
#   4. Set BULLET_SPEED = 15 for faster lasers
#   5. Change BG_COLOR to (20, 0, 40) for purple space
#   6. Set STARTING_LIVES = 10 for easier testing
#
# ============================================
