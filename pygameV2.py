import pygame, sys, random

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
LGreen = [153, 255, 153]
LBlue = [153, 204, 255]

#pygame.mixer.music.load("zvuk.mp3")
#pygame.mixer.music.play(2)
# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(LBlue)

clock = pygame.time.Clock()  # lisame kell
playerImage = pygame.image.load("111.png")
playerImage.fill(red)
enemyImage = pygame.image.load("rabbit.png")
enemyImage.fill(blue)
posX, posY = 0, 0  # kiirus ja asukoht
speedX, speedY = 3, 3
score = 0
enemyCounter = 0
totalEnemies = 40
enemies = []

# koordinaatide loomine ja lisamine massiivi
for i in range(10):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    enemies.append(pygame.Rect(posX, posY, 60, 73))

gameover = False
while not gameover:
    clock.tick(60)
    # mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    # player liikumine
    player = pygame.Rect(posX, posY, 120, 140)
    screen.blit(playerImage, player)

    posX += speedX
    posY += speedY

    if posX > screenX - playerImage.get_rect().width or posX < 0:
        speedX = -speedX

    if posY > screenY - playerImage.get_rect().height or posY < 0:
        speedY = -speedY

    enemyCounter += 1
    if enemyCounter == totalEnemies:
        enemyCounter = 0
        enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0, screenY - 100), 60, 73))

    for enemy in enemies[:]:
        if player.colliderect(enemy):
            enemies.remove(enemy)
            score += 1

    for enemy in enemies:
        screen.blit(enemyImage, enemy)

    pygame.display.flip()
    screen.fill(LBlue)

    print(score)
    if score >= 20:
        gameover = True

pygame.quit()
sys.exit()
