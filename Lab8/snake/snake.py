import pygame
import random
import time

pygame.font.init()
pygame.init()

#Настройки
size = 30
half_size = size // 2
res = 750
res = res // size // 2 * 2 * size + size
FPS = 50
clock = pygame.time.Clock()
screen = pygame.display.set_mode((res, res))

#Цвета (в стиле неоновой змейки)
BG_COLOR = (20, 20, 20)       # Тёмный фон
APPLE_COLOR = (255, 0, 0)     # Красное яблоко
GRID_COLOR = (40, 40, 40)     # Цвет сетки

#Счёт и уровень
score = 0
level = 1
snake_start_position = res // 2 - half_size
length = 4


SNAKE_COLOR = (0, max(255 - level * 10, 50), 0)  # Чем выше уровень, тем темнее змейка
head_img = pygame.image.load("/home/nursultan/Projects python/PP2/Lab8/snake/snake_head_blue.png")  # Загружаем картинку головы
head_img = pygame.transform.scale(head_img, (size, size))  # Подгоняем под размер


#Анимация змейки    
snake_frame_speed = 5
frame_count = 0


#Направления
dirX, dirY = 0, size
direction = {"w": (0, -size), "s": (0, size), "a": (-size, 0), "d": (size, 0)}
snake = [(snake_start_position, snake_start_position)]
apple = (random.randrange(0, res - size, size), random.randrange(0, res - size, size))

#Шрифт
font = pygame.font.SysFont("Arial", 36, bold=True)

#Звуки
pygame.mixer.init()
eat_sound = pygame.mixer.Sound("/home/nursultan/Projects python/PP2/Lab8/snake/eat_sound.mp3")
pygame.mixer.music.set_volume(0.6) # Громкость от 0.0 до 1.0
game_over_sound = pygame.mixer.Sound("/home/nursultan/Projects python/PP2/Lab8/snake/game_over_sound.mp3")
pygame.mixer.music.load("/home/nursultan/Projects python/PP2/Lab8/snake/idea10.mp3")  
pygame.mixer.music.set_volume(0.6)  # Громкость от 0.0 до 1.0
pygame.mixer.music.play(-1)  # -1 означает бесконечное повторение

#Функция окончания игры
def game_over():
    game_over_sound.play()
    for i in range(5):
        screen.fill((255, 0, 0))  # Красный экран
        pygame.display.flip()
        time.sleep(0.1)
        screen.fill((0, 0, 0))  # Чёрный экран
        pygame.display.flip()
        time.sleep(0.1)
    text = font.render("You lose!", True, (255, 0, 0))
    screen.blit(text, (res // 3, res // 3))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


#Функция генерации яблока
def apple_spawn():
    global apple, score, length, level, FPS
    while True:
        apple = (random.randrange(0, res - size, size), random.randrange(0, res - size, size))
        if apple not in snake:
            break
    score += 1
    length += 1
    eat_sound.play()

    if score % 5 == 0:
        level += 1
        FPS += 2

#Функция рисования сетки
def draw_grid():
    for x in range(0, res, size):
        for y in range(0, res, size):
            pygame.draw.rect(screen, GRID_COLOR, (x, y, size, size), 1)


def draw_apple():
    for r in range(half_size, 0, -2):
        color = (255, r * 10, r * 10)  # Градиент от красного к чёрному
        pygame.draw.circle(screen, color, (apple[0] + half_size, apple[1] + half_size), r)



#Основной цикл игры
while True:
    pygame.display.set_caption(f"Snake | Score: {score} | Level: {level}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    for i, (x, y) in enumerate(snake):
        if i == len(snake) - 1:  # Если это голова
            screen.blit(head_img, (x, y))
        else:
            pygame.draw.rect(screen, (0, 160, 0), (x, y, size, size))

    
    #Фон и сетка
    screen.fill(BG_COLOR)
    draw_grid()

    #Рисуем яблоко с градиентом (теперь оно не перекрывается фоном)
    draw_apple()

    #Рисуем змейку (сначала тень, затем тело)
    for x, y in snake:
        pygame.draw.rect(screen, (0, 80, 0), (x-2, y-2, size+4, size+4), border_radius=10)  # Тень
        pygame.draw.rect(screen, SNAKE_COLOR, (x, y, size, size), border_radius=5)  # Тело змейки

    #Добавляем голову змейки поверх тела
    head_x, head_y = snake[-1]
    screen.blit(head_img, (head_x, head_y))


    #Логика движения змейки
    if frame_count % snake_frame_speed == 0:
        newX = snake[-1][0] + dirX
        newY = snake[-1][1] + dirY
        snake.append((newX, newY))
        snake = snake[-length:]

    #Проверка съедания яблока
    if apple[0] == snake[-1][0] and apple[1] == snake[-1][1]:
        apple_spawn()

    #Управление
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and (dirX, dirY) != direction["s"]:
        dirX, dirY = direction["w"]
    elif key[pygame.K_s] and (dirX, dirY) != direction["w"]:
        dirX, dirY = direction["s"]
    elif key[pygame.K_a] and (dirX, dirY) != direction["d"]:
        dirX, dirY = direction["a"]
    elif key[pygame.K_d] and (dirX, dirY) != direction["a"]:
        dirX, dirY = direction["d"]


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_m:  # Остановка музыки (нажатием на "M")
            pygame.mixer.music.stop()
        elif event.key == pygame.K_p:  # Включение музыки (нажатием на "P")
            pygame.mixer.music.play(-1)


    #Проверка на столкновение
    if (
        snake[-1][0] < 0 or snake[-1][0] >= res or
        snake[-1][1] < 0 or snake[-1][1] >= res
    ):
        game_over()
    
    elif snake[-1] in snake[:-1]:
        game_over()

    frame_count += 1
    clock.tick(FPS)
    pygame.display.flip()