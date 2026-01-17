# ============================================
#           SPACE SHOOTER
#          Saturdays with CSIL
# ============================================
#
# Each week you'll add more features.
#
# Look for your workshop number: WORKSHOP 1, WORKSHOP 2, etc.
#
# ============================================

# ============================================
#    WORKSHOP 1: ADD YOUR INFO HERE!
# ============================================
# 
# Programmers usually put their name and info at the top.
# Fill in the comments below:
#
# Game created by: ___________________
# Date started: ___________________
# Our game is about: ___________________
#
# ============================================

import pygame
import sys
import random
import math

# Import your settings (colors, speeds, etc.)
from settings import *

# WORKSHOP 1: This print statement runs when the game starts!
print("=" * 40)
print("Starting", GAME_TITLE)
print("=" * 40)

# WORKSHOP 1 - YOUR CODE HERE:
# Add a print statement with your name!
# Example: print("Created by: Pooja")


# ============================================
#              SETUP
# ============================================

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

clock = pygame.time.Clock()

# Load fonts
font = pygame.font.Font(None, 32)
title_font = pygame.font.Font(None, 72)
small_font = pygame.font.Font(None, 24)


# ============================================
#              GAME VARIABLES
# ============================================
# 
# WORKSHOP 2: These variables store important game data!
#
# ============================================

# Player position
player_x = PLAYER_START_X
player_y = PLAYER_START_Y

# Game objects
bullets = []
enemies = []
particles = []  # For explosions!
last_shot_time = 0

# Game state
score = 0
lives = STARTING_LIVES
high_score = 0
game_state = "playing"

# WORKSHOP 2 - YOUR CODE HERE:
# Create your own variable! Ideas:
# player_name = "Star Destroyer"
# print("Ship name:", player_name)


# ============================================
#    STAR BACKGROUND (Parallax layers)
# ============================================

# Create three layers of stars for depth effect
stars_far = []    # Distant, slow, small
stars_mid = []    # Medium distance
stars_near = []   # Close, fast, bright

# Far stars (distant, slow)
for i in range(STAR_COUNT_FAR):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    speed = random.uniform(0.3, 0.6)
    size = 1
    brightness = random.randint(80, 150)
    stars_far.append([x, y, speed, size, brightness])

# Mid stars
for i in range(STAR_COUNT_MID):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    speed = random.uniform(0.8, 1.5)
    size = random.choice([1, 2])
    brightness = random.randint(150, 220)
    stars_mid.append([x, y, speed, size, brightness])

# Near stars (close, fast, bright)
for i in range(STAR_COUNT_NEAR):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    speed = random.uniform(2, 3)
    size = random.choice([2, 3])
    brightness = random.randint(220, 255)
    stars_near.append([x, y, speed, size, brightness])


# ============================================
#    WORKSHOP 3: HELPER FUNCTIONS
# ============================================

def is_alive(health):
    """
    WORKSHOP 3: Return True if health > 0, else False
    """
    # WORKSHOP 3 - YOUR CODE HERE:
    # if health > 0:
    #     return True
    # else:
    #     return False
    
    return True  # Default


def check_game_over(current_lives):
    """
    WORKSHOP 3: Return True if lives <= 0 (game over!)
    """
    # WORKSHOP 3 - YOUR CODE HERE:
    # if current_lives <= 0:
    #     return True
    # else:
    #     return False
    
    return False  # Default


def add_score(current_score, points):
    """
    WORKSHOP 3: Return current_score + points
    """
    # WORKSHOP 3 - YOUR CODE HERE:
    # return current_score + points
    
    return current_score  # Default


# ============================================
#    PARTICLE SYSTEM (for explosions)
# ============================================

def create_explosion(x, y):
    """Create explosion particles at position"""
    for i in range(PARTICLE_COUNT):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, PARTICLE_SPEED)
        vx = math.cos(angle) * speed
        vy = math.sin(angle) * speed
        color = random.choice([EXPLOSION_YELLOW, EXPLOSION_ORANGE, WHITE])
        lifetime = random.randint(15, PARTICLE_LIFETIME)
        particles.append([x, y, vx, vy, lifetime, color])


def update_particles():
    """Update and remove dead particles"""
    global particles
    for p in particles:
        p[0] += p[2]  # x += vx
        p[1] += p[3]  # y += vy
        p[4] -= 1     # lifetime -= 1
        p[2] *= 0.95  # Slow down
        p[3] *= 0.95
    particles = [p for p in particles if p[4] > 0]


def draw_particles():
    """Draw all particles with fading"""
    for p in particles:
        alpha = int(255 * (p[4] / PARTICLE_LIFETIME))
        size = max(1, int(3 * (p[4] / PARTICLE_LIFETIME)))
        pygame.draw.circle(screen, p[5], (int(p[0]), int(p[1])), size)


# ============================================
#    WORKSHOP 5: DRAWING FUNCTIONS
# ============================================

def draw_stars():
    """
    WORKSHOP 5: Draw parallax star background
    """
    # Draw and move each layer
    for star in stars_far:
        color = (star[4], star[4], star[4])
        pygame.draw.circle(screen, color, (int(star[0]), int(star[1])), star[3])
        
        # WORKSHOP 5 - YOUR CODE HERE:
        # Move stars down: star[1] = star[1] + star[2]
        # If off screen: if star[1] > SCREEN_HEIGHT: star[1] = 0
    
    for star in stars_mid:
        color = (star[4], star[4], int(star[4] * 0.9))
        pygame.draw.circle(screen, color, (int(star[0]), int(star[1])), star[3])
        # Same movement code for mid stars
    
    for star in stars_near:
        color = (star[4], star[4], int(star[4] * 0.8))
        pygame.draw.circle(screen, color, (int(star[0]), int(star[1])), star[3])
        # Same movement code for near stars


def draw_player():
    """
    WORKSHOP 5: Draw the player's spaceship
    """
    # Ship center position
    cx = player_x + PLAYER_WIDTH // 2
    cy = player_y + PLAYER_HEIGHT // 2
    
    # WORKSHOP 5: Uncomment to draw a cool spaceship!
    # 
    # # Engine glow (draw first, so it's behind)
    # engine_points = [
    #     (cx - 8, player_y + PLAYER_HEIGHT),
    #     (cx, player_y + PLAYER_HEIGHT + 15),
    #     (cx + 8, player_y + PLAYER_HEIGHT)
    # ]
    # pygame.draw.polygon(screen, PLAYER_ENGINE, engine_points)
    # 
    # # Main body (triangle)
    # body_points = [
    #     (cx, player_y),                              # Nose
    #     (player_x, player_y + PLAYER_HEIGHT),        # Left wing
    #     (cx, player_y + PLAYER_HEIGHT - 10),         # Bottom center
    #     (player_x + PLAYER_WIDTH, player_y + PLAYER_HEIGHT)  # Right wing
    # ]
    # pygame.draw.polygon(screen, PLAYER_COLOR, body_points)
    # 
    # # Cockpit (small triangle)
    # cockpit_points = [
    #     (cx, player_y + 8),
    #     (cx - 6, player_y + 20),
    #     (cx + 6, player_y + 20)
    # ]
    # pygame.draw.polygon(screen, PLAYER_ACCENT, cockpit_points)
    # 
    # # Wing details
    # pygame.draw.line(screen, PLAYER_ACCENT, (player_x + 5, player_y + PLAYER_HEIGHT - 5), 
    #                  (cx - 5, player_y + PLAYER_HEIGHT - 15), 2)
    # pygame.draw.line(screen, PLAYER_ACCENT, (player_x + PLAYER_WIDTH - 5, player_y + PLAYER_HEIGHT - 5),
    #                  (cx + 5, player_y + PLAYER_HEIGHT - 15), 2)
    
    # DEFAULT: Simple rectangle
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))


# ============================================
#    WORKSHOP 6: BULLET FUNCTIONS
# ============================================

def fire_bullet():
    """
    WORKSHOP 6: Create a new bullet
    """
    global last_shot_time
    current_time = pygame.time.get_ticks()
    
    # WORKSHOP 6 - YOUR CODE HERE:
    # if current_time - last_shot_time > FIRE_DELAY:
    #     bullet_x = player_x + PLAYER_WIDTH // 2
    #     bullet_y = player_y
    #     bullets.append([bullet_x, bullet_y])
    #     last_shot_time = current_time
    
    pass


def update_bullets():
    """
    WORKSHOP 6: Move bullets up
    """
    global bullets
    
    # WORKSHOP 6 - YOUR CODE HERE:
    # for bullet in bullets:
    #     bullet[1] = bullet[1] - BULLET_SPEED
    # bullets = [b for b in bullets if b[1] > -10]
    
    pass


def draw_bullets():
    """
    WORKSHOP 6: Draw bullets with glow effect
    """
    # WORKSHOP 6 - YOUR CODE HERE:
    # for bullet in bullets:
    #     bx, by = int(bullet[0]), int(bullet[1])
    #     # Outer glow
    #     pygame.draw.rect(screen, BULLET_GLOW, 
    #                      (bx - BULLET_WIDTH, by - 2, BULLET_WIDTH * 2, BULLET_HEIGHT + 4))
    #     # Inner bright part
    #     pygame.draw.rect(screen, BULLET_COLOR,
    #                      (bx - BULLET_WIDTH // 2, by, BULLET_WIDTH, BULLET_HEIGHT))
    
    pass


# ============================================
#    WORKSHOP 7: ENEMY FUNCTIONS
# ============================================

def spawn_enemy():
    """
    WORKSHOP 7: Randomly spawn enemies
    """
    # WORKSHOP 7 - YOUR CODE HERE:
    # if random.random() < ENEMY_SPAWN_RATE:
    #     enemy_x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
    #     enemy_y = -ENEMY_HEIGHT
    #     # Random enemy type (0, 1, or 2 for different colors)
    #     enemy_type = random.randint(0, 2)
    #     enemies.append([enemy_x, enemy_y, enemy_type])
    
    pass


def update_enemies():
    """
    WORKSHOP 7: Move enemies down
    """
    global enemies, lives, game_state
    
    # WORKSHOP 7 - YOUR CODE HERE:
    # for enemy in enemies:
    #     enemy[1] = enemy[1] + ENEMY_SPEED
    # 
    # for enemy in enemies[:]:
    #     if enemy[1] > SCREEN_HEIGHT:
    #         enemies.remove(enemy)
    #         lives = lives - 1
    #         if lives <= 0:
    #             game_state = "game_over"
    
    pass


def draw_enemies():
    """
    WORKSHOP 7: Draw enemies with different styles
    """
    # WORKSHOP 7 - YOUR CODE HERE:
    # colors = [ENEMY_RED, ENEMY_ORANGE, ENEMY_PURPLE]
    # 
    # for enemy in enemies:
    #     ex, ey = enemy[0], enemy[1]
    #     color = colors[enemy[2]]
    #     
    #     # Draw hexagon-ish enemy
    #     points = [
    #         (ex + ENEMY_WIDTH // 2, ey),
    #         (ex + ENEMY_WIDTH, ey + ENEMY_HEIGHT // 3),
    #         (ex + ENEMY_WIDTH, ey + ENEMY_HEIGHT * 2 // 3),
    #         (ex + ENEMY_WIDTH // 2, ey + ENEMY_HEIGHT),
    #         (ex, ey + ENEMY_HEIGHT * 2 // 3),
    #         (ex, ey + ENEMY_HEIGHT // 3)
    #     ]
    #     pygame.draw.polygon(screen, color, points)
    #     
    #     # Inner detail
    #     pygame.draw.circle(screen, WHITE, 
    #                        (ex + ENEMY_WIDTH // 2, ey + ENEMY_HEIGHT // 2), 5)
    
    pass


# ============================================
#    WORKSHOP 8: COLLISIONS + MENUS
# ============================================

def check_collisions():
    """
    WORKSHOP 8: Check bullet-enemy collisions
    """
    global score, bullets, enemies
    
    # WORKSHOP 8 - YOUR CODE HERE:
    # bullets_to_remove = []
    # enemies_to_remove = []
    # 
    # for bullet in bullets:
    #     for enemy in enemies:
    #         if (enemy[0] <= bullet[0] <= enemy[0] + ENEMY_WIDTH and
    #             enemy[1] <= bullet[1] <= enemy[1] + ENEMY_HEIGHT):
    #             bullets_to_remove.append(bullet)
    #             enemies_to_remove.append(enemy)
    #             score = score + POINTS_PER_ENEMY
    #             # Create explosion!
    #             create_explosion(enemy[0] + ENEMY_WIDTH // 2, 
    #                            enemy[1] + ENEMY_HEIGHT // 2)
    #             break
    # 
    # for b in bullets_to_remove:
    #     if b in bullets: bullets.remove(b)
    # for e in enemies_to_remove:
    #     if e in enemies: enemies.remove(e)
    
    pass


def draw_menu():
    """
    WORKSHOP 8: Draw start menu
    """
    screen.fill(BG_COLOR)
    draw_stars()
    
    # WORKSHOP 8 - YOUR CODE HERE:
    # # Title with glow effect
    # title = title_font.render(GAME_TITLE, True, NEON_CYAN)
    # title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
    # screen.blit(title, title_rect)
    # 
    # # Instructions
    # start_text = font.render("Press ENTER to Start", True, WHITE)
    # start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, 280))
    # screen.blit(start_text, start_rect)
    # 
    # # Controls
    # ctrl1 = small_font.render("Arrow Keys - Move", True, (150, 150, 150))
    # ctrl2 = small_font.render("Spacebar - Shoot", True, (150, 150, 150))
    # screen.blit(ctrl1, ctrl1.get_rect(center=(SCREEN_WIDTH // 2, 350)))
    # screen.blit(ctrl2, ctrl2.get_rect(center=(SCREEN_WIDTH // 2, 375)))
    # 
    # # High score
    # if high_score > 0:
    #     hs = font.render(f"High Score: {high_score}", True, YELLOW)
    #     screen.blit(hs, hs.get_rect(center=(SCREEN_WIDTH // 2, 430)))
    
    pass


def draw_game_over():
    """
    WORKSHOP 8: Draw game over screen
    """
    screen.fill(BG_COLOR)
    draw_stars()
    draw_particles()  # Show remaining explosions
    
    # WORKSHOP 8 - YOUR CODE HERE:
    # # Game Over text
    # go_text = title_font.render("GAME OVER", True, RED)
    # go_rect = go_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
    # screen.blit(go_text, go_rect)
    # 
    # # Final score
    # score_text = font.render(f"Final Score: {score}", True, WHITE)
    # screen.blit(score_text, score_text.get_rect(center=(SCREEN_WIDTH // 2, 250)))
    # 
    # # New high score?
    # if score >= high_score and score > 0:
    #     new_hs = font.render("NEW HIGH SCORE!", True, YELLOW)
    #     screen.blit(new_hs, new_hs.get_rect(center=(SCREEN_WIDTH // 2, 300)))
    # 
    # # Restart prompt
    # restart = font.render("Press ENTER to Play Again", True, WHITE)
    # screen.blit(restart, restart.get_rect(center=(SCREEN_WIDTH // 2, 380)))
    
    pass


def draw_hud():
    """
    Draw score and lives HUD
    """
    # Score
    score_text = font.render(f"Score: {score}", True, HUD_GREEN)
    screen.blit(score_text, (15, 15))
    
    # Lives as icons
    lives_label = small_font.render("Lives:", True, WHITE)
    screen.blit(lives_label, (15, 50))
    for i in range(lives):
        # Draw mini ship icons
        x = 70 + i * 25
        pygame.draw.polygon(screen, PLAYER_COLOR, [
            (x, 55), (x - 8, 68), (x + 8, 68)
        ])


def reset_game():
    """Reset game state"""
    global player_x, bullets, enemies, particles, score, lives
    player_x = PLAYER_START_X
    bullets = []
    enemies = []
    particles = []
    score = 0
    lives = STARTING_LIVES


# ============================================
#            MAIN GAME LOOP
# ============================================

running = True

while running:
    
    # ========== HANDLE EVENTS ==========
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_bullet()
            
            if game_state == "game_over" and event.key == pygame.K_RETURN:
                reset_game()
                game_state = "playing"
    
    # ========== GAME OVER STATE ==========
    if game_state == "game_over":
        update_particles()
        draw_game_over()
        pygame.display.flip()
        clock.tick(FPS)
        continue
    
    # ========================================
    #    WORKSHOP 4: PLAYER MOVEMENT
    # ========================================
    
    keys = pygame.key.get_pressed()
    
    # WORKSHOP 4 - YOUR CODE HERE:
    # if keys[pygame.K_LEFT]:
    #     player_x = player_x - PLAYER_SPEED
    # if keys[pygame.K_RIGHT]:
    #     player_x = player_x + PLAYER_SPEED
    # 
    # # Boundary checking
    # if player_x < 0:
    #     player_x = 0
    # if player_x > SCREEN_WIDTH - PLAYER_WIDTH:
    #     player_x = SCREEN_WIDTH - PLAYER_WIDTH
    
    # ========== UPDATE ==========
    update_bullets()
    spawn_enemy()
    update_enemies()
    check_collisions()
    update_particles()
    
    # ========== DRAW ==========
    screen.fill(BG_COLOR)
    draw_stars()
    draw_player()
    draw_bullets()
    draw_enemies()
    draw_particles()
    draw_hud()
    
    # ========== DISPLAY ==========
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
