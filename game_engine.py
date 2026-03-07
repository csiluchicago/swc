import pygame
import sys
import random
import math

print("Loading game.py...")

try:
    from game import (
        # Constants
        SCREEN_WIDTH, SCREEN_HEIGHT,
        PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED,
        BULLET_WIDTH, BULLET_HEIGHT, BULLET_SPEED,
        ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_SPEED, ENEMY_SPAWN_RATE,
        STARTING_LIVES, POINTS_PER_ENEMY,
        
        # Week 4
        clamp_position,
        move_player_safe,
        move_bullet,
        is_bullet_off_screen,
        
        # Week 5
        update_all_bullets,
        should_spawn_enemy,
        move_enemy_down,
        is_enemy_off_screen,
        
        # Week 6
        create_enemy_at_top,
        get_living_enemies,
        count_alive_enemies,
        remove_escaped_enemies,
        
        # Week 7
        check_collision,
        check_bullet_hits_enemies,
        check_player_hit_by_enemy,
        
        # Week 8
        calculate_score,
        check_game_over,
        lose_life,
    )
    print(" Successfully loaded game functions")
except ImportError as e:
    print(f" Error loading game.py: {e}")
    sys.exit(1)

def check_week_4():
    try:
        r1 = clamp_position(100)
        r2 = move_player_safe(100, "left", 5)
        r3 = move_bullet(100, 10)
        r4 = is_bullet_off_screen(-5)
        return all(r is not None for r in [r1, r2, r3, r4])
    except:
        return False

def check_week_5():
    try:
        bullets = [{'x': 100, 'y': 50}]
        r1 = update_all_bullets(bullets)
        r2 = should_spawn_enemy(60, 60)
        r3 = move_enemy_down(100, 2)
        r4 = is_enemy_off_screen(600)
        return all(r is not None for r in [r1, r2, r3, r4])
    except:
        return False

def check_week_6():
    try:
        r1 = create_enemy_at_top()
        enemies = [
            {'x': 100, 'y': 100, 'alive': True},
            {'x': 200, 'y': 600, 'alive': True}
        ]
        r2 = get_living_enemies(enemies)
        r3 = count_alive_enemies(enemies)
        r4 = remove_escaped_enemies(enemies)
        return all(r is not None for r in [r1, r2, r3, r4])
    except:
        return False

def check_week_7():
    try:
        r1 = check_collision(0, 0, 10, 10, 5, 5, 10, 10)
        bullets = [{'x': 100, 'y': 100}]
        enemies = [{'x': 100, 'y': 100, 'alive': True}]
        r2 = check_bullet_hits_enemies(bullets, enemies)
        r3 = check_player_hit_by_enemy(100, 100, enemies)
        return all(r is not None for r in [r1, r2, r3])
    except:
        return False

def check_week_8():
    try:
        r1 = calculate_score(10)
        r2 = check_game_over(3)
        r3 = lose_life(3)
        return all(r is not None for r in [r1, r2, r3])
    except:
        return False

WEEK_4_READY = check_week_4()
WEEK_5_READY = check_week_5()
WEEK_6_READY = check_week_6()
WEEK_7_READY = check_week_7()
WEEK_8_READY = check_week_8()

print(f"\n{'='*50}")
print("FEATURES AVAILABLE:")
print(f"  Week 4 (Functions): {'y' if WEEK_4_READY else 'n'}")
print(f"  Week 5 (Loops): {'y' if WEEK_5_READY else 'n'}")
print(f"  Week 6 (Lists): {'y' if WEEK_6_READY else 'n'}")
print(f"  Week 7 (Collision): {'y' if WEEK_7_READY else 'n'}")
print(f"  Week 8 (Polish): {'y' if WEEK_8_READY else 'n'}")
print(f"{'='*50}\n")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SPACE_BLUE = (8, 12, 30)
NEON_CYAN = (0, 255, 255)
NEON_GREEN = (50, 255, 100)
LASER_BLUE = (100, 200, 255)
ENEMY_RED = (255, 60, 60)
ENEMY_ORANGE = (255, 150, 50)
ENEMY_PURPLE = (180, 80, 255)
HUD_GREEN = (100, 255, 150)
EXPLOSION_YELLOW = (255, 220, 100)
EXPLOSION_ORANGE = (255, 150, 50)


particles = []
PARTICLE_COUNT = 12
PARTICLE_LIFETIME = 30
PARTICLE_SPEED = 4

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

def draw_particles(screen):
    """Draw all particles with fading"""
    for p in particles:
        alpha = int(255 * (p[4] / PARTICLE_LIFETIME))
        size = max(1, int(3 * (p[4] / PARTICLE_LIFETIME)))
        pygame.draw.circle(screen, p[5], (int(p[0]), int(p[1])), size)

stars_far = []
stars_mid = []
stars_near = []

def init_stars():
    """Initialize parallax star layers"""
    global stars_far, stars_mid, stars_near
    
    # Far stars (distant, slow)
    for i in range(40):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        speed = random.uniform(0.3, 0.6)
        size = 1
        brightness = random.randint(80, 150)
        stars_far.append([x, y, speed, size, brightness])
    
    # Mid stars
    for i in range(25):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        speed = random.uniform(0.8, 1.5)
        size = random.choice([1, 2])
        brightness = random.randint(150, 220)
        stars_mid.append([x, y, speed, size, brightness])
    
    # Near stars (close, fast, bright)
    for i in range(15):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        speed = random.uniform(2, 3)
        size = random.choice([2, 3])
        brightness = random.randint(220, 255)
        stars_near.append([x, y, speed, size, brightness])

def draw_stars(screen):
    """Draw and update parallax stars"""
    # Far stars
    for star in stars_far:
        color = (star[4], star[4], star[4])
        pygame.draw.circle(screen, color, (int(star[0]), int(star[1])), star[3])
        star[1] = star[1] + star[2]
        if star[1] > SCREEN_HEIGHT:
            star[1] = 0
            star[0] = random.randint(0, SCREEN_WIDTH)
    
    # Mid stars
    for star in stars_mid:
        color = (star[4], star[4], int(star[4] * 0.9))
        pygame.draw.circle(screen, color, (int(star[0]), int(star[1])), star[3])
        star[1] = star[1] + star[2]
        if star[1] > SCREEN_HEIGHT:
            star[1] = 0
            star[0] = random.randint(0, SCREEN_WIDTH)
    
    # Near stars
    for star in stars_near:
        color = (star[4], star[4], int(star[4] * 0.8))
        pygame.draw.circle(screen, color, (int(star[0]), int(star[1])), star[3])
        star[1] = star[1] + star[2]
        if star[1] > SCREEN_HEIGHT:
            star[1] = 0
            star[0] = random.randint(0, SCREEN_WIDTH)

 
class SpaceShooter:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space Shooter")
        self.clock = pygame.time.Clock()
        
        # Fonts
        self.font_small = pygame.font.Font(None, 24)
        self.font_med = pygame.font.Font(None, 32)
        self.font_large = pygame.font.Font(None, 72)
        
        # Initialize stars
        init_stars()
        
        # Game state
        self.state = "menu"  # menu, playing, game_over
        self.reset_game()
        self.high_score = 0
        self.running = True
    
    def reset_game(self):
        """Reset game for new play"""
        self.player_x = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
        self.player_y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10
        self.bullets = []
        self.enemies = []
        self.frame_count = 0
        self.score = 0
        self.lives = STARTING_LIVES
        global particles
        particles = []
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        # Movement (Week 4)
        if self.state == "playing" and WEEK_4_READY:
            if keys[pygame.K_LEFT]:
                new_x = move_player_safe(self.player_x, "left", PLAYER_SPEED)
                if new_x is not None:
                    self.player_x = new_x
            if keys[pygame.K_RIGHT]:
                new_x = move_player_safe(self.player_x, "right", PLAYER_SPEED)
                if new_x is not None:
                    self.player_x = new_x
        
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                # Menu
                if self.state == "menu" and event.key == pygame.K_RETURN:
                    self.state = "playing"
                
                # Shooting
                if self.state == "playing" and event.key == pygame.K_SPACE:
                    self.fire_bullet()
                
                # Restart
                if self.state == "game_over" and event.key == pygame.K_RETURN:
                    self.reset_game()
                    self.state = "playing"
    
    def fire_bullet(self):
        bullet = {
            'x': self.player_x + PLAYER_WIDTH // 2 - BULLET_WIDTH // 2,
            'y': self.player_y
        }
        self.bullets.append(bullet)
    
    def update(self):
        if self.state != "playing":
            update_particles()
            return
        
        self.frame_count += 1
        
        # Update bullets
        if WEEK_5_READY:
            updated = update_all_bullets(self.bullets)
            if updated is not None:
                self.bullets = updated
        else:
            for bullet in self.bullets:
                if WEEK_4_READY:
                    new_y = move_bullet(bullet['y'], BULLET_SPEED)
                    if new_y is not None:
                        bullet['y'] = new_y
            if WEEK_4_READY:
                self.bullets = [b for b in self.bullets
                              if not is_bullet_off_screen(b['y'])]
        
        # Spawn enemies (Week 5+)
        if WEEK_5_READY and WEEK_6_READY:
            if should_spawn_enemy(self.frame_count, ENEMY_SPAWN_RATE):
                enemy = create_enemy_at_top()
                if enemy is not None:
                    # Add enemy type for color
                    enemy['type'] = random.randint(0, 2)
                    self.enemies.append(enemy)
        
        # Move enemies DOWN (Week 5)
        if WEEK_5_READY and self.enemies:
            for enemy in self.enemies:
                if enemy.get('alive', True):
                    new_y = move_enemy_down(enemy['y'], ENEMY_SPEED)
                    if new_y is not None:
                        enemy['y'] = new_y
        
        # Remove escaped enemies (Week 6)
        if WEEK_6_READY and self.enemies:
            result = remove_escaped_enemies(self.enemies)
            if result is not None:
                self.enemies, escaped = result
                
                # Lose lives for escaped enemies (Week 8)
                if WEEK_8_READY and escaped > 0:
                    for _ in range(escaped):
                        self.lives = lose_life(self.lives)
                    print(f"{escaped} enemies escaped! Lives: {self.lives}")
        
        # Check collisions (Week 7) - Do this BEFORE cleaning up dead enemies!
        if WEEK_7_READY and self.enemies and self.bullets:
            # Track which enemies are alive BEFORE collision check
            alive_before = set()
            for enemy in self.enemies:
                if enemy.get('alive', True):
                    alive_before.add(id(enemy))
            
            result = check_bullet_hits_enemies(self.bullets, self.enemies)
            if result is not None:
                self.bullets, self.enemies, hits = result
                
                # Create explosions ONLY for enemies that were alive → now dead
                if hits > 0:
                    for enemy in self.enemies:
                        # Was alive before BUT is dead now = just killed!
                        if id(enemy) in alive_before and not enemy.get('alive', True):
                            create_explosion(
                                enemy['x'] + ENEMY_WIDTH // 2,
                                enemy['y'] + ENEMY_HEIGHT // 2
                            )
                
                if WEEK_8_READY and hits > 0:
                    points = calculate_score(POINTS_PER_ENEMY)
                    if points is not None:
                        self.score += points * hits
        
        # NOW clean up dead enemies (after explosions are created)
        self.enemies = [e for e in self.enemies if e.get('alive', True)]
        
        # Check player hit (Week 7)
        if WEEK_7_READY and self.enemies:
            hit = check_player_hit_by_enemy(self.player_x, self.player_y, self.enemies)
            if hit:
                if WEEK_8_READY:
                    self.lives = lose_life(self.lives)
                # Remove enemy that hit player (with explosion)
                for enemy in self.enemies:
                    if enemy.get('alive', True):
                        if check_collision(
                            self.player_x, self.player_y, PLAYER_WIDTH, PLAYER_HEIGHT,
                            enemy['x'], enemy['y'], ENEMY_WIDTH, ENEMY_HEIGHT
                        ):
                            create_explosion(enemy['x'] + ENEMY_WIDTH // 2,
                                           enemy['y'] + ENEMY_HEIGHT // 2)
                            enemy['alive'] = False
        
        # Update particles
        update_particles()
        
        # Check game over (Week 8)
        if WEEK_8_READY:
            if check_game_over(self.lives):
                self.state = "game_over"
                if self.score > self.high_score:
                    self.high_score = self.score
    
    def draw_menu(self):
        """Draw menu screen"""
        self.screen.fill(SPACE_BLUE)
        draw_stars(self.screen)
        
        # Title
        title = self.font_large.render("SPACE SHOOTER", True, NEON_CYAN)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
        self.screen.blit(title, title_rect)
        
        # Start
        start = self.font_med.render("Press ENTER to Start", True, WHITE)
        start_rect = start.get_rect(center=(SCREEN_WIDTH // 2, 280))
        self.screen.blit(start, start_rect)
        
        # Controls
        ctrl1 = self.font_small.render("Arrow Keys - Move", True, (150, 150, 150))
        ctrl2 = self.font_small.render("Spacebar - Shoot", True, (150, 150, 150))
        self.screen.blit(ctrl1, ctrl1.get_rect(center=(SCREEN_WIDTH // 2, 350)))
        self.screen.blit(ctrl2, ctrl2.get_rect(center=(SCREEN_WIDTH // 2, 375)))
    
    def draw_game_over(self):
        """Draw game over screen"""
        self.screen.fill(SPACE_BLUE)
        draw_stars(self.screen)
        draw_particles(self.screen)
        
        # Game Over
        go = self.font_large.render("GAME OVER", True, ENEMY_RED)
        go_rect = go.get_rect(center=(SCREEN_WIDTH // 2, 150))
        self.screen.blit(go, go_rect)
        
        # Score
        score_text = self.font_med.render(f"Final Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, score_text.get_rect(center=(SCREEN_WIDTH // 2, 250)))
        
        # High score
        if self.score >= self.high_score and self.score > 0:
            hs = self.font_med.render("NEW HIGH SCORE!", True, EXPLOSION_YELLOW)
            self.screen.blit(hs, hs.get_rect(center=(SCREEN_WIDTH // 2, 300)))
        
        # Restart
        restart = self.font_med.render("Press ENTER to Play Again", True, WHITE)
        self.screen.blit(restart, restart.get_rect(center=(SCREEN_WIDTH // 2, 380)))
    
    def draw_playing(self):
        """Draw game screen"""
        self.screen.fill(SPACE_BLUE)
        draw_stars(self.screen)
        
        # Draw player
        pygame.draw.rect(self.screen, NEON_CYAN,
                        (self.player_x, self.player_y, PLAYER_WIDTH, PLAYER_HEIGHT))
        
        # Draw bullets
        for bullet in self.bullets:
            pygame.draw.rect(self.screen, LASER_BLUE,
                           (bullet['x'], bullet['y'], BULLET_WIDTH, BULLET_HEIGHT))
        
        # Draw enemies with colors!
        colors = [ENEMY_RED, ENEMY_ORANGE, ENEMY_PURPLE]
        for enemy in self.enemies:
            # Only draw living enemies
            if enemy.get('alive', True):
                color = colors[enemy.get('type', 0)]
                pygame.draw.rect(self.screen, color,
                               (enemy['x'], enemy['y'], ENEMY_WIDTH, ENEMY_HEIGHT))
        
        # Draw particles
        draw_particles(self.screen)
        
        # HUD
        score_text = self.font_med.render(f"Score: {self.score}", True, HUD_GREEN)
        self.screen.blit(score_text, (15, 15))
        
        # Lives as ship icons
        lives_label = self.font_small.render("Lives:", True, WHITE)
        self.screen.blit(lives_label, (15, 50))
        for i in range(self.lives):
            x = 70 + i * 25
            pygame.draw.polygon(self.screen, NEON_CYAN, [
                (x, 55), (x - 8, 68), (x + 8, 68)
            ])
        
        # Week indicator
        week = 4 if WEEK_4_READY else 3
        if WEEK_8_READY: week = 8
        elif WEEK_7_READY: week = 7
        elif WEEK_6_READY: week = 6
        elif WEEK_5_READY: week = 5
        
        week_text = self.font_small.render(f"Week {week}", True, (100, 100, 100))
        self.screen.blit(week_text, (SCREEN_WIDTH - 100, 15))
    
    def draw(self):
        if self.state == "menu":
            self.draw_menu()
        elif self.state == "game_over":
            self.draw_game_over()
        else:
            self.draw_playing()
        
        pygame.display.flip()
    
    def run(self):
        print("\nSpace Shooter Game!\n")
        
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()
        print("\nThanks for playing!")



if __name__ == "__main__":
    if not WEEK_4_READY:
        print("\n  Week 4 functions not complete!")
        print("Complete game_student_falling.py first.\n")
        response = input("Start anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(0)
    
    try:
        game = SpaceShooter()
        game.run()
    except Exception as e:
        print(f"\n Error: {e}")
        import traceback
        traceback.print_exc()
        pygame.quit()
        sys.exit(1)
