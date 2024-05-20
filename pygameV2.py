import pygame
import random
import sys

pygame.init()

def Maja(x, y, laius, kõrgus, ekraani_pind, värv):
    punktid = [(x, y - ((3 / 4.0) * kõrgus)), (x, y), (x + laius, y), (x + laius, y - (3 / 4.0) * kõrgus), (x, y - ((3 / 4.0) * kõrgus)), (x + laius / 2.0, y - kõrgus), (x + laius, y - (3 / 4.0) * kõrgus)]
    suurus = random.randint(1, 10)
    pygame.draw.lines(ekraani_pind, värv, False, punktid, suurus)

def Uks(x, y, laius, kõrgus, ekraani_pind, värv):
    uks_laius = laius // 6
    uks_kõrgus = kõrgus // 3
    punktid = [(x, y), (x, y - uks_kõrgus), (x + uks_laius, y - uks_kõrgus), (x + uks_laius, y)]
    suurus = random.randint(1, 10)
    pygame.draw.lines(ekraani_pind, värv, True, punktid, suurus)

def Aken(x, y, laius, kõrgus, ekraani_pind, värv):
    aken_laius = laius // 3
    aken_kõrgus = kõrgus // 3
    punktid = [(x + laius // 2, y - kõrgus // 2), (x + laius // 2, y - kõrgus // 2 - aken_kõrgus), (x + laius // 2 + aken_laius, y - kõrgus // 2 - aken_kõrgus), (x + laius // 2 + aken_laius, y - kõrgus // 2)]
    suurus = random.randint(1, 10)
    pygame.draw.lines(ekraani_pind, värv, True, punktid, suurus)

def Korsten(x, y, laius, kõrgus, ekraani_pind, värv):
    korsten_laius = laius // 10
    korsten_kõrgus = kõrgus // 5
    punktid = [(x + 2 * laius // 3, y - kõrgus), (x + 2 * laius // 3, y - kõrgus - korsten_kõrgus), (x + 2 * laius // 3 + korsten_laius, y - kõrgus - korsten_kõrgus), (x + 2 * laius // 3 + korsten_laius, y - kõrgus)]
    suurus = random.randint(1, 10)
    pygame.draw.lines(ekraani_pind, värv, True, punktid, suurus)

def drawHouse(x, y, width, height, ekraani_pind, color):
    points = [(x, y - ((3 / 4.0) * height)), (x, y), (x + width, y),
              (x + width, y - (3 / 4.0) * height), (x, y - ((3 / 4.0) * height)),
              (x + width / 2.0, y - height), (x + width, y - ((3 / 4.0) * height))]
    lineThickness = 3
    pygame.draw.lines(ekraani_pind, color, False, points, lineThickness)

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
fon = [r, g, b]

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
majavarv = [r, g, b]

ekraani_pind = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Juhuslikud objektid + majake")
ekraani_pind.fill(fon)
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
varv = [r, g, b]

ekraani_pind = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Juhuslikud kujundid")
ekraani_pind.fill(lGreen)

drawHouse(100, 400, 300, 400, ekraani_pind, red)
Maja(100, 400, 300, 400, ekraani_pind, majavarv)
Uks(100, 400, 300, 400, ekraani_pind, majavarv)
Aken(100, 400, 300, 400, ekraani_pind, majavarv)
Korsten(100, 400, 300, 400, ekraani_pind, majavarv)

for i in range(1, 10):
    x = random.randint(0, 620)
    y = random.randint(0, 460)
    pygame.draw.rect(ekraani_pind, varv, [x, y, 20, 20])

pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
pygame.quit()



#gameover=False 

#while not gameover:
#    youWin=pygame.image.load("win.jpg")
#    youWin=pygame.transform.scale(youWin, [300, 200])
#    ekraani_pind.blit(youWin,[180, 100])

#    pygame.display.flip()
#    for i in pygame.event.get():
#        if i.type==pygame.QUIT:
#            sys.exit()
#pygame.quit()
    
