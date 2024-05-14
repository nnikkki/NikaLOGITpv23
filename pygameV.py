import pygame
import math

pygame.init()
ekraani_pind = pygame.display.set_mode((800, 600))
ekraani_pind.fill((135, 206, 235))  # Небо голубого цвета

# Рисование солнца в углу
pygame.draw.circle(ekraani_pind, (255, 255, 0), (60, 60), 50)
for i in range(0, 360, 30):
    angle = math.radians(i)
    x = 60 + 90 * math.cos(angle)
    y = 60 + 90 * math.sin(angle)
    pygame.draw.line(ekraani_pind, (255, 255, 0), (60, 60), (x, y), 5)

# Рисование облаков
cloud_colors = [(255, 255, 255), (245, 245, 245)]
cloud_positions = [(200, 150), (500, 120)]  # Изменено расположение облаков
for i in range(len(cloud_positions)):
    pygame.draw.circle(ekraani_pind, cloud_colors[i], cloud_positions[i], 50)
    pygame.draw.circle(ekraani_pind, cloud_colors[i], (cloud_positions[i][0] + 50, cloud_positions[i][1]), 50)
    pygame.draw.circle(ekraani_pind, cloud_colors[i], (cloud_positions[i][0] + 100, cloud_positions[i][1]), 50)
    pygame.draw.circle(ekraani_pind, cloud_colors[i], (cloud_positions[i][0] + 150, cloud_positions[i][1]), 50)

# Рисование травы
pygame.draw.rect(ekraani_pind, (34, 139, 34), [0, 500, 800, 100])

# Рисование травинок
for i in range(0, 800, 10):
    height = 500 + (i % 30)
    pygame.draw.line(ekraani_pind, (0, 128, 0), (i, 500), (i, height), 3)

# Рисование расширенного изображения
pilt = pygame.image.load("111.png")
pilt = pygame.transform.scale(pilt, (200, 150))  # Расширяем размер изображения
pilt_rect = pilt.get_rect(bottomleft=(50, 600))  # Помещаем изображение на траву
ekraani_pind.blit(pilt, pilt_rect)

# Функция для рисования цветка из треугольников
def draw_triangle_flower(x, y):
    # Стебель
    pygame.draw.line(ekraani_pind, (0, 255, 0), (x, 500), (x, y), 5)
    # Центр цветка
    pygame.draw.circle(ekraani_pind, (255, 0, 0), (x, y - 10), 15)
    # Лепестки цветка (треугольники)
    for i in range(0, 360, 45):
        angle = math.radians(i)
        petal_x = x + 40 * math.cos(angle)
        petal_y = y - 10 + 40 * math.sin(angle)
        pygame.draw.polygon(ekraani_pind, (255, 105, 180), [(x, y - 10), (petal_x, petal_y), (x + 20 * math.cos(angle + math.pi / 8), y - 10 + 20 * math.sin(angle + math.pi / 8))])

# Рисование 10 цветов из треугольников
flower_positions = [(100, 450), (200, 460), (300, 440), (400, 470), (500, 430),
                    (600, 450), (150, 480), (250, 440), (350, 460), (450, 430)]
for pos in flower_positions:
    draw_triangle_flower(pos[0], pos[1])

tekst = "Tere, Pygame"
meie_font = pygame.font.SysFont("Verdana", 36)
teksti_pilt = meie_font.render(tekst, False, (250, 250, 100))
ekraani_pind.blit(teksti_pilt, (300, 30))

pygame.display.flip()

# Ожидание закрытия окна пользователем
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
