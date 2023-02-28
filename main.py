import time
import pygame
from random import randrange as rnd
from Detect_Colission import detect_collision
from Paddle import Bate
from Block import Block
from Ball import Ball
import moviepy.editor


pygame.init()

WIDTH, HEIGHT = 1200, 800
ventana = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Videojuego")
fps = 60
dx, dy = 1, -1
clock = pygame.time.Clock()

# Agrego sonidos al juego y hago play del sonido de fondo
crash_sound = pygame.mixer.Sound("music/crash.mp3")
background = pygame.mixer.Sound("music/background.wav")
gameoverSound = pygame.mixer.Sound("music/gameover.mp3")
background.play(-1)

# Crea el objeto bate, y obtengo su rectángulo
bate = Bate(15,"images/bar.png")

# Pongo el bate en la parte inferior de la pantalla
bate.rect.move_ip(840,750)

# Crea el objeto win, obtengo su rectángulo
win = pygame.image.load("images/winner.jpg")
win_rect = win.get_rect()
win_rect.move_ip(300,250)

# ball settings
ball = Ball(10, 6)
ballRect = pygame.Rect(rnd(ball.rect, WIDTH - ball.rect), HEIGHT // 2, ball.rect, ball.rect)

# Crea el objeto bloque
bricks = []

for posx in range(30):
    for posy in range(8):
        bricks.append(Block(None,posx*40, posy*40))

# background image
img = pygame.image.load('images/background.jpg').convert()


def pausa():
    loop = 1
    font = pygame.font.Font('freesansbold.ttf', 32)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    text = font.render('Press Space to continue', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    ventana.fill(white)
    ventana.blit(text, textRect)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_SPACE:
                    ventana.fill((0, 0, 0))
                    loop = 0
        pygame.display.update()
        clock.tick(60)


jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

     # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()

    # drawing world
    ventana.blit(img, (0, 0))
    ventana.blit(bate.img, bate.rect)

    for brick in bricks:
        ventana.blit(brick.img,brick.rect)

    pygame.draw.circle(ventana, pygame.Color('white'), ballRect.center, ball.radius)
    # ball movement
    ballRect.x += ball.speed * dx
    ballRect.y += ball.speed * dy
    # collision left right
    if ballRect.centerx < ball.radius or ballRect.centerx > WIDTH - ball.radius:
        dx = -dx
    # collision top
    if ballRect.centery < ball.radius:
        dy = -dy
    # collision paddle
    if ballRect.colliderect(bate.rect) and dy > 0:
        crash_sound.play()
        dx, dy = detect_collision(dx, dy, ballRect, bate.rect)

    # collision blocks
    hit_index = ballRect.collidelist(bricks)
    if hit_index != -1:
        hit_rect = bricks.pop(hit_index)
        dx, dy = detect_collision(dx, dy, ballRect, hit_rect.rect)

    # Control del audio

    # SFX OFF
    elif keys[pygame.K_s]:
        gameoverSound.set_volume(0.0)
        crash_sound.set_volume(0.0)
    # SFX ON
    elif keys[pygame.K_d]:
        gameoverSound.set_volume(1.0)
        crash_sound.set_volume(1.0)

    # Baja volumen
    if keys[pygame.K_1] and pygame.mixer.music.get_volume() > 0.0:
        background.set_volume(background.get_volume() - 0.01)
    # Sube volumen
    if keys[pygame.K_2] and pygame.mixer.music.get_volume() < 1.0:
        background.set_volume(background.get_volume() + 0.01)

    # Desactivar sonido
    elif keys[pygame.K_m]:
        background.set_volume(0.0)
        gameoverSound.set_volume(0.0)
        crash_sound.set_volume(0.0)

    # Reactivar sonido
    elif keys[pygame.K_COMMA]:
        background.set_volume(1.0)
        gameoverSound.set_volume(1.0)
        crash_sound.set_volume(1.0)

        # Pausar juego
    elif keys[pygame.K_p]:
        pausa()

    # control
    if keys[pygame.K_LEFT] and bate.rect.left > 0:
        bate.rect.left -= bate.speed
    if keys[pygame.K_RIGHT] and bate.rect.right < WIDTH:
        bate.rect.right += bate.speed

    # win, game over

    if ballRect.bottom > HEIGHT:
        jugando = False
        background.stop()
        gameoverSound.play()
        video = moviepy.editor.VideoFileClip("images/gameover.mp4")
        video.preview()
        time.sleep(5)

    elif not len(bricks):
        ventana.blit(win,win_rect)
        video = moviepy.editor.VideoFileClip("video.mp4")
        video.preview()
        jugando = False
        time.sleep(5)


    # update screen
    pygame.display.flip()
    clock.tick(fps)



pygame.quit()

