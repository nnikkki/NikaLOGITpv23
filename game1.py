import pygame
import random
import sys
from collections import deque # Импорт класса deque из модуля collections для эффективной работы с очередями более эффективным выбором для больших объемов данных или частых операций добавления и удаления.







# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800   # Ширина  окна
SCREEN_HEIGHT = 600   # Высота окна
CELL_SIZE = 40    # Размер клетки на игровом поле
PLAYER_SIZE = CELL_SIZE    # Размер игрока
CRYSTAL_SIZE = 20           # Размер кристалла
ENEMY_SIZE = CELL_SIZE     # Размер врага
HEART_SIZE = CELL_SIZE // 2      # Размер сердца
PLAYER_SPEED = 5           
ENEMY_SPEED = 3     
MAX_LEVELS = 10
LIVES = 3
CRYSTALS_REQUIRED = 5

# Загрузка и масштаб текстур
def load_and_scale_image(path, width, height):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (width, height))

player_texture = load_and_scale_image('png-klev.png', PLAYER_SIZE, PLAYER_SIZE)
enemy_texture = load_and_scale_image('123.png', ENEMY_SIZE, ENEMY_SIZE)
wall_texture = load_and_scale_image('wall.png', CELL_SIZE, CELL_SIZE)
goal_texture = load_and_scale_image('chest.png', CELL_SIZE, CELL_SIZE)
heart_texture = load_and_scale_image('heart.png', HEART_SIZE, HEART_SIZE)
crystal_texture = load_and_scale_image('gem.png', CRYSTAL_SIZE, CRYSTAL_SIZE)
background_texture = load_and_scale_image('cave.png', SCREEN_WIDTH, SCREEN_HEIGHT)

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Лабиринт')

# Функция для создания начала и конца лабиринта
def create_start_end(walls):
    start = pygame.Rect(0, 0, PLAYER_SIZE, PLAYER_SIZE)   # Создание клетки для начала лабиринта
    end = pygame.Rect(0, 0, PLAYER_SIZE, PLAYER_SIZE)   # Создание клетка для конца лабиринта
    while True:
        # Генерация случайной позиции начала лабиринта, не пересекающейся со стенами
        start.x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        start.y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if not any(start.colliderect(wall) for wall in walls):
            break
    while True:
        # Генерация случайной позиции конца лабиринта, не пересекающейся со стенами и не совпадающей с началом
        end.x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        end.y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if not any(end.colliderect(wall) for wall in walls) and end != start:
            break
    return start, end

def create_enemies(level, walls, start, end):
    enemies = []
    for _ in range(max(0, level - 3)):  # Враги появляются с 4 уровня
        while True:
            x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            enemy_rect = pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)   # Создание клетки для врага
            if not any(enemy_rect.colliderect(wall) for wall in walls) and not enemy_rect.colliderect(start) and not enemy_rect.colliderect(end):
                #Эта строка проверяет, что новая позиция врага (enemy_rect) не пересекается ни с одной стеной (wall) из списка walls, а также не пересекается с начальной (start) и конечной (end) позициями в лабиринте.
                direction = random.choice(['up', 'down', 'left', 'right'])
                enemies.append((enemy_rect, direction))   # Добавление врага в список
                break
    return enemies

def create_crystals_and_hearts(level, walls, enemies, start, end):
    objects = {'crystals': [], 'hearts': []}    # Словарь для хранения кристаллов и сердец .  два списка типо в одном
    placed_positions = set()   #проверяет не занята ли клетка уже 

    for obj_type, count in [('crystals', CRYSTALS_REQUIRED), ('hearts', 2 if level >= 4 else 0)]:
        for _ in range(count):
            while True:
                obj = pygame.Rect(random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                                  random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE,
                                  CRYSTAL_SIZE if obj_type == 'crystals' else HEART_SIZE,
                                  CRYSTAL_SIZE if obj_type == 'crystals' else HEART_SIZE)

                if not any(obj.colliderect(wall) for wall in walls) and \
                   not any(obj.colliderect(enemy[0]) for enemy in enemies) and \
                   not obj.colliderect(start) and \
                   not obj.colliderect(end) and \
                   obj.topleft not in placed_positions:
                    objects[obj_type].append(obj)
                    placed_positions.add(obj.topleft)
                    break

    return objects['crystals'], objects['hearts']

# Функция для генерации уровня
def generate_level(level):
    walls = []
    
    # Создание границ
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        walls.append(pygame.Rect(x, 0, CELL_SIZE, CELL_SIZE))
        walls.append(pygame.Rect(x, SCREEN_HEIGHT - CELL_SIZE, CELL_SIZE, CELL_SIZE))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        walls.append(pygame.Rect(0, y, CELL_SIZE, CELL_SIZE))
        walls.append(pygame.Rect(SCREEN_WIDTH - CELL_SIZE, y, CELL_SIZE, CELL_SIZE))
    
    # Создание случайных стен
    for _ in range(30):  
        while True:
            wall = pygame.Rect(random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                               random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE,
                               CELL_SIZE, CELL_SIZE)
            if not any(wall.colliderect(existing_wall) for existing_wall in walls):
                walls.append(wall)
                break

    start, end = create_start_end(walls)
    enemies = create_enemies(level, walls, start, end)
    crystals, hearts = create_crystals_and_hearts(level, walls, enemies, start, end)  # Обновленный вызов функции

    return walls, crystals, enemies, hearts, start, end

    return walls, crystals, enemies, hearts, start, end

# Функция для отрисовки уровня
def draw_level(walls, crystals, enemies, hearts, player, end, level, collected_crystals, lives, invincible):
    screen.blit(background_texture, (0, 0))  # Отрисовка фона игрового поля
    screen.blit(goal_texture, end)   # Отрисовка цели
    if invincible:   #неуязвим
        color = (255, 255, 0) if pygame.time.get_ticks() % 500 < 250 else (0, 255, 0)  # Мигающий эффект если убрать текстуру то будет мигать 
    else:
        color = (0, 255, 0)
    screen.blit(player_texture, player.topleft)
    for wall in walls:
        screen.blit(wall_texture, wall.topleft)
    for crystal in crystals:
        screen.blit(crystal_texture, crystal.topleft)
    for enemy_rect, direction in enemies:
        screen.blit(enemy_texture, enemy_rect.topleft)
    for heart in hearts:
        screen.blit(heart_texture, heart.topleft)

    # Отображение номера уровня
    font = pygame.font.Font(None, 36)
    level_text = font.render("Level: " + str(level), True, (255, 255, 255))
    screen.blit(level_text, (20, 20))

    # Отображение количества собранных кристаллов
    crystal_text = font.render("Crystals: " + str(collected_crystals), True, (255, 255, 255))
    screen.blit(crystal_text, (20, 60))

    # Отображение количества жизней
    lives_text = font.render("Lives: " + str(lives), True, (255, 255, 255))
    screen.blit(lives_text, (20, 100))

# Функция для обновления экрана и событий
def update_screen():
    pygame.display.flip()
    pygame.time.Clock().tick(30)

# Функция для показа экрана победы
def win_screen():
    screen.fill((0, 255, 0))
    font = pygame.font.Font(None, 74)
    win_text = font.render("You Win!", True, (255, 255, 255))
    screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, SCREEN_HEIGHT // 2 - win_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

# Функция для показа экрана game over
def game_over_screen():
    screen.fill((255, 0, 0))
    font = pygame.font.Font(None, 74)
    game_over_text = font.render("Game Over", True, (255, 255, 255))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

# Функция для движения врагов
def move_enemies(enemies, walls):
    for i, (enemy_rect, direction) in enumerate(enemies):
        if direction == 'up':
            enemy_rect.move_ip(0, -ENEMY_SPEED)
        elif direction == 'down':
            enemy_rect.move_ip(0, ENEMY_SPEED)
        elif direction == 'left':
            enemy_rect.move_ip(-ENEMY_SPEED, 0)
        elif direction == 'right':
            enemy_rect.move_ip(ENEMY_SPEED, 0)
         # Проверка столкновений врагов со стенами
        if enemy_rect.top < 0 or enemy_rect.bottom > SCREEN_HEIGHT or any(enemy_rect.colliderect(wall) for wall in walls):
            if direction == 'up':
                direction = 'down'
            elif direction == 'down':
                direction = 'up'
            elif direction == 'left':
                direction = 'right'
            elif direction == 'right':
                direction = 'left'
        enemies[i] = (enemy_rect, direction)

# Основная функция игры
def main_game():
    level = 1
    lives = LIVES
    player = pygame.Rect(0, 0, PLAYER_SIZE, PLAYER_SIZE)
    walls = []
    crystals = []
    enemies = []
    hearts = []
    start = pygame.Rect(0, 0, PLAYER_SIZE, PLAYER_SIZE)
    end = pygame.Rect(0, 0, PLAYER_SIZE, PLAYER_SIZE)
    
    invincible = False
    invincible_start_time = 0

    while level <= MAX_LEVELS:  
        walls, crystals, enemies, hearts, start, end = generate_level(level)
        crystals, hearts = create_crystals_and_hearts(level, walls, enemies, start, end) 
        player.topleft = start.topleft
        collected_crystals = 0
        level_completed = False

        while not level_completed:      # Цикл обработки игровых событий на уровне
            for event in pygame.event.get(): # Обработка всех событий в очереди
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()    # Получение состояния всех клавиш
            if keys[pygame.K_LEFT] and player.left > 0 and not any(player.move(-PLAYER_SPEED, 0).colliderect(wall) for wall in walls):
                player.move_ip(-PLAYER_SPEED, 0)
            if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH and not any(player.move(PLAYER_SPEED, 0).colliderect(wall) for wall in walls):
                player.move_ip(PLAYER_SPEED, 0)
            if keys[pygame.K_UP] and player.top > 0 and not any(player.move(0, -PLAYER_SPEED).colliderect(wall) for wall in walls):
                player.move_ip(0, -PLAYER_SPEED)
            if keys[pygame.K_DOWN] and player.bottom < SCREEN_HEIGHT and not any(player.move(0, PLAYER_SPEED).colliderect(wall) for wall in walls):
                player.move_ip(0, PLAYER_SPEED)

            move_enemies(enemies, walls)

            for crystal in crystals:
                if player.colliderect(crystal):
                    crystals.remove(crystal)
                    collected_crystals += 1

            for heart in hearts:
                if player.colliderect(heart):
                    hearts.remove(heart)
                    lives = min(lives + 1, 5)

            # Проверка состояния неуязвимости
            if invincible:
                if pygame.time.get_ticks() - invincible_start_time > 3000:
                    invincible = False

            for enemy in enemies:
                if player.colliderect(enemy[0]) and not invincible:
                    lives -= 1
                    player.topleft = start.topleft
                    invincible = True
                    invincible_start_time = pygame.time.get_ticks()
                    if lives <= 0:
                        game_over_screen()
                        pygame.quit()
                        sys.exit()

            if collected_crystals >= CRYSTALS_REQUIRED and player.colliderect(end):
                level_completed = True
                level += 1
                if level > MAX_LEVELS:
                    win_screen()
                    pygame.quit()
                    sys.exit()

            draw_level(walls, crystals, enemies, hearts, player, end, level, collected_crystals, lives, invincible)
            update_screen()

if __name__ == '__main__':
    main_game()

