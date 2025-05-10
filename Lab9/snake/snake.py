import pygame
import random
import time
import os

pygame.font.init()
pygame.init()

# Настройки
size = 30
half_size = size // 2
res = 750
res = res // size // 2 * 2 * size + size
FPS = 50
clock = pygame.time.Clock()
screen = pygame.display.set_mode((res, res))

# Цвета (в стиле неоновой змейки)
BG_COLOR = (20, 20, 20)       # Тёмный фон
APPLE_COLOR = (255, 0, 0)     # Красное яблоко
GRID_COLOR = (40, 40, 40)     # Цвет сетки

# Счёт и уровень
score = 0
level = 1
snake_start_position = res // 2 - half_size
length = 4
apple_counter = 0
golden_apple = None

SNAKE_COLOR = (0, max(255 - level * 10, 50), 0)  # Чем выше уровень, тем темнее змейка

# Пути к файлам (делаем код кроссплатформенным)
BASE_DIR = os.path.dirname(__file__)
head_img_path = os.path.join(BASE_DIR, "snake_head_blue.png")
eat_sound_path = os.path.join(BASE_DIR, "eat_sound.mp3")
game_over_sound_path = os.path.join(BASE_DIR, "game_over_sound.mp3")
bg_music_path = os.path.join(BASE_DIR, "idea10.mp3")

# Загрузка изображения головы змейки
head_img = pygame.image.load(head_img_path)
head_img = pygame.transform.scale(head_img, (size, size))

# Звуки
pygame.mixer.init()
eat_sound = pygame.mixer.Sound(eat_sound_path)
game_over_sound = pygame.mixer.Sound(game_over_sound_path)

pygame.mixer.music.load(bg_music_path)
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)

# Анимация змейки    
snake_frame_speed = 5
frame_count = 0
З
# Направления
dirX, dirY = 0, size
direction = {"w": (0, -size), "s": (0, size), "a": (-size, 0), "d": (size, 0)}
snake = [(snake_start_position, snake_start_position)]
apple = (random.randrange(0, res - size, size), random.randrange(0, res - size, size))

# Шрифт
font = pygame.font.SysFont("Arial", 36, bold=True)

# Функция окончания игры
def game_over():
    game_over_sound.play()
    for _ in range(5):
        screen.fill((255, 0, 0))
        pygame.display.flip()
        time.sleep(0.1)
        screen.fill((0, 0, 0))
        pygame.display.flip()
        time.sleep(0.1)
    text = font.render("You lose!", True, (255, 0, 0))
    screen.blit(text, (res // 3, res // 3))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Генерация яблока
def apple_spawn():
    global apple, score, length, level, FPS, apple_counter, golden_apple

    apple_counter += 1  # Увеличиваем счётчик обычных яблок

    if apple_counter % 5 == 0:  # Проверяем, кратен ли счётчик 4
        while True:
            golden_apple = (random.randrange(0, res - size, size), random.randrange(0, res - size, size))
            if golden_apple not in snake:
                break
    else:
        while True:
            apple = (random.randrange(0, res - size, size), random.randrange(0, res - size, size))
            if apple not in snake:
                break
        score += 1
        length += 1
        eat_sound.play()

    # Увеличение уровня и FPS при достижении определённого счёта
    if score // 5 > level - 1: #score // 5 вычисляет текущий уровень, level - 1 — это текущий уровень
        level += 1
        FPS += 10
    

# Функция рисования сетки
def draw_grid():
    for x in range(0, res, size):
        for y in range(0, res, size):
            pygame.draw.rect(screen, GRID_COLOR, (x, y, size, size), 1)

def draw_apple():
    for r in range(half_size, 0, -2):
        color = (255, r * 10, r * 10)  # Градиент от красного к чёрному
        pygame.draw.circle(screen, color, (apple[0] + half_size, apple[1] + half_size), r)

def draw_golden_apple():
    if golden_apple:
        pygame.draw.circle(screen, (255, 215, 0), (golden_apple[0] + half_size, golden_apple[1] + half_size), half_size)


# Таймер для обновления яблока
apple_respawn_time = 5000  # Время до появления нового яблока (в миллисекундах)
last_apple_spawn_time = pygame.time.get_ticks()  # Время последнего появления яблока


#-----------------------------------------------------------------------------------------------------------------


# Основной цикл игры
while True:
    pygame.display.set_caption(f"Snake | Score: {score} | Level: {level}")

    screen.fill(BG_COLOR)
    draw_grid()
    draw_apple()
    draw_golden_apple()

    # Рисуем змейку
    for x, y in snake:
        pygame.draw.rect(screen, (0, 80, 0), (x-2, y-2, size+4, size+4), border_radius=10)
        pygame.draw.rect(screen, SNAKE_COLOR, (x, y, size, size), border_radius=5)

    head_x, head_y = snake[-1]
    screen.blit(head_img, (head_x, head_y))

    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_p:
                pygame.mixer.music.play(-1)
            elif event.key in (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d):
                new_dirX, new_dirY = direction[chr(event.key)]
                if (new_dirX, new_dirY) != (-dirX, -dirY):
                    dirX, dirY = new_dirX, new_dirY

    # Движение змейки
    if frame_count % snake_frame_speed == 0:
        newX, newY = snake[-1][0] + dirX, snake[-1][1] + dirY
        snake.append((newX, newY))
        snake = snake[-length:]

    # Проверка на съедание яблок
    if (newX, newY) == apple:
        apple_spawn()
    elif golden_apple and (newX, newY) == golden_apple:  # Добавляем проверку для золотого яблока
        golden_apple = None  # Убираем золотое яблоко после съедания
        score += 2  # Увеличиваем очки за золотое яблоко
        length += 2  # Увеличиваем длину змейки
        eat_sound.play()

    # Обновление обычного яблока через заданное время
    if pygame.time.get_ticks() - last_apple_spawn_time > apple_respawn_time:
        apple = (random.randrange(0, res - size, size), random.randrange(0, res - size, size))
        last_apple_spawn_time = pygame.time.get_ticks()  # Сбрасываем таймер появления яблока

    

    # Проверка на столкновение
    if newX < 0 or newX >= res or newY < 0 or newY >= res or (newX, newY) in snake[:-1]:
        game_over()

    frame_count += 1
    clock.tick(FPS)
    pygame.display.flip()
