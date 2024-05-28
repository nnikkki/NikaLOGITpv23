import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 40
PLAYER_COLOR = (0, 255, 0)
WALL_COLOR = (0, 0, 255)
ENEMY_COLOR = (255, 0, 0)
GOAL_COLOR = (255, 255, 0)
CRYSTAL_COLOR = (0, 255, 255)
OBSTACLE_COLOR = (255, 165, 0)
BACKGROUND_COLOR = (0, 100, 0)  # Темно-зеленый фон
PLAYER_SPEED = 5
ENEMY_SPEED = 3
MAX_LEVELS = 10

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Лабиринт')

# Функция для создания начала и конца лабиринта
def create_start_end(walls, obstacles, crystals):
    start = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)
    end = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)
    while True:
        start.x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        start.y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if not any(start.colliderect(wall) for wall in walls):  # Проверяем, что начальная точка не на стене
            break
    while True:
        end.x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        end.y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if not any(end.colliderect(wall) for wall in walls) and end != start:  # Проверяем, что конечная точка не на стене и не совпадает с начальной
            break
    return start, end

# Функция для отображения начального окна с выбором начать игру или прочитать о управлении
def start_screen():
    font = pygame.font.Font(None, 36)
    start_text = font.render("Press ENTER to start", True, (255, 255, 255))
    controls_text = font.render("Press 'i' for controls", True, (255, 255, 255))
    while True:
        screen.fill(BACKGROUND_COLOR)  # Темно-зеленый фон
        screen.blit(player_title_image, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(controls_text, (SCREEN_WIDTH // 2 - controls_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

# Функция для отображения заставки игры и обработки событий
def title_screen():
    screen.blit(title_screen_image, (0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

# Функция для показа окна с предложением начать заново
def game_over_screen():
    font = pygame.font.Font(None, 50)
    game_over_text = font.render("Game Over", True, (255, 255, 255))
    restart_text = font.render("Press ENTER to restart", True, (255, 255, 255))
    while True:
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

# Загрузка изображений
player_title_image = pygame.image.load("png-klev.png")
player_title_image = pygame.transform.scale(player_title_image, (100, 100))
title_screen_image = pygame.image.load("Untitled.jpg")
title_screen_image = pygame.transform.scale(title_screen_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Основной игровой цикл
running = True
current_level = 1
lives = 5
collected_crystals = []
enemies = []

start_screen()  # Отображаем начальное окно

while current_level <= MAX_LEVELS:
    # Получение стен, препятствий и кристаллов для текущего уровня
    walls, obstacles, crystals = mazes[current_level - 1]
    
    # Создание начала и конец лабиринта для текущего уровня
    start, end = create_start_end(walls, obstacles, crystals)
    
    # Отрисовка начала и конца лабиринта
    pygame.draw.rect(screen, (255, 0, 255), start)
    pygame.draw.rect(screen, (255, 255, 0), end)
    
    # Основной игровой цикл для текущего уровня
    while running:
        screen.fill(BACKGROUND_COLOR)
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # Отрисовка элементов лабиринта
        # ...
        
        pygame.display.flip()
