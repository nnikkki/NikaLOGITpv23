import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 40
PLAYER_SIZE = CELL_SIZE
CRYSTAL_SIZE = 20
ENEMY_SIZE = CELL_SIZE
PLAYER_COLOR = (0, 255, 0)
WALL_COLOR = (0, 0, 0)
ENEMY_COLOR = (255, 0, 0)
GOAL_COLOR = (255, 255, 0)
CRYSTAL_COLOR = (0, 255, 255)
START_END_BACKGROUND_COLOR = (0, 100, 0)
LEVEL_BACKGROUND_COLOR = (139, 69, 19)
PLAYER_SPEED = 5
ENEMY_SPEED = 3
MAX_LEVELS = 10
LIVES = 5

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Лабиринт')

# Load images
player_image = pygame.image.load("png-klev.png")
player_image = pygame.transform.scale(player_image, (PLAYER_SIZE, PLAYER_SIZE))
enemy_image = pygame.image.load("123.png")
enemy_image = pygame.transform.scale(enemy_image, (ENEMY_SIZE, ENEMY_SIZE))
player_title_image = pygame.image.load("png-klev.png")
player_title_image = pygame.transform.scale(player_title_image, (100, 100))

# Function to create start and end points of the maze
def create_start_end(walls):
    start = pygame.Rect(0, 0, PLAYER_SIZE, PLAYER_SIZE)
    end = pygame.Rect(0, 0, PLAYER_SIZE, PLAYER_SIZE)
    while True:
        start.x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        start.y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if not any(start.colliderect(wall) for wall in walls):
            break
    while True:
        end.x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        end.y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if not any(end.colliderect(wall) for wall in walls) and end != start:
            break
    return start, end

# Function to display the start screen with options to start or read controls
def start_screen():
    font = pygame.font.Font(None, 36)
    start_text = font.render("Press ENTER to start", True, (255, 255, 255))
    controls_text = font.render("Press 'i' for controls", True, (255, 255, 255))
    
    running = True
    while running:
        screen.fill(START_END_BACKGROUND_COLOR)
        screen.blit(player_title_image, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(controls_text, (SCREEN_WIDTH // 2 - controls_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                elif event.key == pygame.K_i:
                    show_controls_screen()

# Function to display the controls screen
def show_controls_screen():
    font = pygame.font.Font(None, 36)
    controls = [
        "Controls:",
        "Arrow keys to move",
        "Avoid enemies",
        "Collect all crystals to proceed",
        "Press ENTER to return"
    ]
    
    running = True
    while running:
        screen.fill(START_END_BACKGROUND_COLOR)
        for i, line in enumerate(controls):
            text = font.render(line, True, (255, 255, 255))
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 100 + i * 40))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False

# Function to display the game over screen
def game_over_screen():
    font = pygame.font.Font(None, 50)
    game_over_text = font.render("Game Over", True, (255, 255, 255))
    restart_text = font.render("Press ENTER to restart", True, (255, 255, 255))
   
    while True:
        screen.fill(START_END_BACKGROUND_COLOR)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

# Function to display the win screen
def win_screen():
    font = pygame.font.Font(None, 50)
    win_text = font.render("You Win!", True, (255, 255, 255))
    restart_text = font.render("Press ENTER to restart", True, (255, 255, 255))
    controls_text = font.render("Press 'i' for controls", True, (255, 255, 255))
    while True:
        screen.fill(START_END_BACKGROUND_COLOR)
        screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, SCREEN_HEIGHT // 2 -win_text.get_height() // 2))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(controls_text, (SCREEN_WIDTH // 2 - controls_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

# Function to generate the maze walls
def generate_maze():
    walls = []
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        walls.append(((x, 0), (x, SCREEN_HEIGHT)))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        walls.append(((0, y), (SCREEN_WIDTH, y)))
    return walls

# Function to generate the level
def generate_level(level):
    walls = generate_maze()
    
    obstacles = []
    for _ in range(10):
        obstacle = pygame.Rect(random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                               random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE,
                               CELL_SIZE, CELL_SIZE)
        if obstacle.collidelist([pygame.Rect(wall[0], (CELL_SIZE, CELL_SIZE)) for wall in walls]) == -1:
            obstacles.append(obstacle)
    
    crystals = []
    for _ in range(5):
        while True:
            crystal = pygame.Rect(random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                                  random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE,
                                  CRYSTAL_SIZE, CRYSTAL_SIZE)
            if crystal.collidelist([pygame.Rect(wall[0], (CELL_SIZE, CELL_SIZE)) for wall in walls]) == -1:
                crystals.append(crystal)
                break
    
    start, end = create_start_end(walls)
    
    enemies = []
    if level >= 3:
        for _ in range(3):
            while True:
                enemy = pygame.Rect(random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                                    random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE,
                                    ENEMY_SIZE, ENEMY_SIZE)
                if enemy.collidelist(obstacles) == -1 and enemy.collidelist(crystals) == -1 and all(not pygame.Rect(wall[0], (CELL_SIZE, CELL_SIZE)).colliderect(enemy) for wall in walls) and enemy != start and enemy != end:
                    enemies.append(enemy)
                    break

    return walls, obstacles, crystals, start, end, enemies

# Function to draw the level
def draw_level(walls, obstacles, crystals, start, end, enemies):
    screen.fill(LEVEL_BACKGROUND_COLOR)  # Brown background
    pygame.draw.rect(screen, GOAL_COLOR, end)
    for wall in walls:
        pygame.draw.line(screen, WALL_COLOR, wall[0], wall[1], 5)
    for obstacle in obstacles:
        pygame.draw.rect(screen, WALL_COLOR, obstacle)
    for crystal in crystals:
        pygame.draw.rect(screen, CRYSTAL_COLOR, crystal)
    for enemy in enemies:
        screen.blit(enemy_image, enemy)

# Function to update the screen
def update_screen():
    pygame.display.flip()
    pygame.time.Clock().tick(30)

# Main game function
def main_game():
    start_screen()
    level = 1
    lives = LIVES
    while level <= MAX_LEVELS and lives > 0:
        walls, obstacles, crystals, start, end, enemies = generate_level(level)

        player = start.copy()
        collected_crystals = 0
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.left > 0:
                player.move_ip(-PLAYER_SPEED, 0)
            if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
                player.move_ip(PLAYER_SPEED, 0)
            if keys[pygame.K_UP] and player.top > 0:
                player.move_ip(0, -PLAYER_SPEED)
            if keys[pygame.K_DOWN] and player.bottom < SCREEN_HEIGHT:
                player.move_ip(0, PLAYER_SPEED)

            # Check for collisions with walls
            if any(pygame.Rect(wall[0], (CELL_SIZE, CELL_SIZE)).colliderect(player) for wall in walls):
                player = start.copy()

            # Check for crystal collection
            crystal_index = player.collidelist(crystals)
            if crystal_index != -1:
                del crystals[crystal_index]
                collected_crystals += 1

            # Check if player reached the goal
            if collected_crystals >= 5 and player.colliderect(end):
                level += 1
                break
                        # Check for collisions with enemies
            if player.collidelist(enemies) != -1:
                lives -= 1
                if lives <= 0:
                    game_over_screen()
                    return
                player = start.copy()

            draw_level(walls, obstacles, crystals, start, end, enemies)
            screen.blit(player_image, player)

            # Display level and lives
            font = pygame.font.Font(None, 36)
            level_text = font.render(f"Level: {level}", True, (255, 255, 255))
            lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
            crystals_text = font.render(f"Crystals: {collected_crystals}/5", True, (255, 255, 255))
            screen.blit(level_text, (10, 10))
            screen.blit(lives_text, (10, 50))
            screen.blit(crystals_text, (10, 90))

            update_screen()

        if level > MAX_LEVELS:
            win_screen()

# Start the game
main_game()
pygame.quit()

