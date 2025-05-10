import pygame
import random
import time
import os
import psycopg2
from psycopg2 import Error
from datetime import datetime

pygame.font.init()
pygame.init()

# Database connection parameters
DB_PARAMS = {
    "host": "localhost",
    "database": "snake_game",
    "user": "postgres",
    "password": "12345678",
    "port": "5432"
}

# Game settings
size = 30
half_size = size // 2
res = 750
res = res // size // 2 * 2 * size + size
screen = pygame.display.set_mode((res, res))
clock = pygame.time.Clock()

# Colors
BG_COLOR = (20, 20, 20)
APPLE_COLOR = (255, 0, 0)
GRID_COLOR = (40, 40, 40)
WALL_COLOR = (100, 100, 100)

# Game state
score = 0
length = 4
apple_counter = 0
golden_apple = None
snake_frame_speed = 5
frame_count = 0
paused = False

# Snake and apple
snake_start_position = res // 2 - half_size
dirX, dirY = 0, size
direction = {"w": (0, -size), "s": (0, size), "a": (-size, 0), "d": (size, 0)}
snake = [(snake_start_position, snake_start_position)]
apple = (random.randrange(0, res - size, size), random.randrange(0, res - size, size))

# Database functions
def connect_db():
    return psycopg2.connect(**DB_PARAMS)

def setup_database(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(50) PRIMARY KEY,
                current_level INTEGER DEFAULT 1
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS user_scores (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) REFERENCES users(username),
                score INTEGER,
                level INTEGER,
                timestamp TIMESTAMP
            );
        """)
        conn.commit()

def get_or_create_user(conn, username):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT current_level FROM users WHERE username = %s", (username,))
            result = cur.fetchone()
            if result:
                return result[0]
            cur.execute("INSERT INTO users (username, current_level) VALUES (%s, 1)", (username,))
            conn.commit()
            return 1
    except Error as e:
        print(f"Error with user: {e}")
        conn.rollback()
        return 1

def save_score(conn, username, score, level):
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO user_scores (username, score, level, timestamp) VALUES (%s, %s, %s, %s)",
                (username, score, level, datetime.now())
            )
            conn.commit()
            print("Score saved successfully.")
    except Error as e:
        print(f"Error saving score: {e}")
        conn.rollback()

def update_user_level(conn, username, new_level):
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET current_level = %s WHERE username = %s", (new_level, username))
            conn.commit()
    except Error as e:
        print(f"Error updating level: {e}")
        conn.rollback()

# Level configurations
LEVELS = {
    1: {"speed": 50, "walls": [], "apple_respawn_time": 5000},
    2: {
        "speed": 60,
        "walls": [(0, y) for y in range(0, res, size)] + [(res-size, y) for y in range(0, res, size)] +
                 [(x, 0) for x in range(0, res, size)] + [(x, res-size) for x in range(0, res, size)],
        "apple_respawn_time": 6000
    },
    3: {
        "speed": 70,
        "walls": [(res//2, y) for y in range(size*5, res-size*5, size)] +
                 [(x, res//2) for x in range(size*5, res-size*5, size)],
        "apple_respawn_time": 7000
    }
}

# Game settings
size = 30
half_size = size // 2
res = 750
res = res // size // 2 * 2 * size + size
screen = pygame.display.set_mode((res, res))
clock = pygame.time.Clock()

# Colors
BG_COLOR = (20, 20, 20)
APPLE_COLOR = (255, 0, 0)
GRID_COLOR = (40, 40, 40)
WALL_COLOR = (100, 100, 100)

# Game state
score = 0
length = 4
apple_counter = 0
golden_apple = None
snake_frame_speed = 5
frame_count = 0
paused = False

# Snake and apple
snake_start_position = res // 2 - half_size
dirX, dirY = 0, size
direction = {"w": (0, -size), "s": (0, size), "a": (-size, 0), "d": (size, 0)}
snake = [(snake_start_position, snake_start_position)]
apple = (random.randrange(0, res - size, size), random.randrange(0, res - size, size))

# Font
font = pygame.font.SysFont("Arial", 36, bold=True)

# File paths
BASE_DIR = os.path.dirname(__file__)
head_img_path = os.path.join(BASE_DIR, "snake_head_blue.png")
eat_sound_path = os.path.join(BASE_DIR, "eat_sound.mp3")
game_over_sound_path = os.path.join(BASE_DIR, "game_over_sound.mp3")
bg_music_path = os.path.join(BASE_DIR, "idea10.mp3")

# Load assets with error handling
try:
    head_img = pygame.image.load(head_img_path)
    head_img = pygame.transform.scale(head_img, (size, size))
    pygame.mixer.init()
    eat_sound = pygame.mixer.Sound(eat_sound_path)
    game_over_sound = pygame.mixer.Sound(game_over_sound_path)
    pygame.mixer.music.load(bg_music_path)
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)
except pygame.error as e:
    print(f"Error loading assets: {e}")
    pygame.quit()
    quit()

# Get username
username = input("Enter your username: ").strip() or "guest"

# Database setup and user check
try:
    conn = connect_db()
    setup_database(conn)
    current_level = get_or_create_user(conn, username)
    print(f"Welcome, {username}! Current Level: {current_level}")
    FPS = LEVELS[current_level]["speed"]
    apple_respawn_time = LEVELS[current_level]["apple_respawn_time"]
except Error as e:
    print(f"Database error: {e}")
    conn = None
    current_level = 1
    FPS = LEVELS[1]["speed"]
    apple_respawn_time = LEVELS[1]["apple_respawn_time"]

# Functions
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
    if conn:
        save_score(conn, username, score, current_level)
    time.sleep(2)
    pygame.quit()
    quit()

def apple_spawn():
    global apple, score, length, apple_counter, golden_apple, level, FPS, current_level
    apple_counter += 1
    if apple_counter % 5 == 0:
        while True:
            golden_apple = (random.randrange(0, res - size, size), random.randrange(0, res - size, size))
            if golden_apple not in snake and golden_apple not in LEVELS[current_level]["walls"]:
                break
    else:
        while True:
            apple = (random.randrange(0, res - size, size), random.randrange(0, res - size, size))
            if apple not in snake and apple not in LEVELS[current_level]["walls"]:
                break
        score += 1
        length += 1
        eat_sound.play()
    if score >= 10 and current_level < 3:
        new_level = min(current_level + 1, 3)
        update_user_level(conn, username, new_level)
        print(f"Level up! New Level: {new_level}")
        level = new_level
        current_level = new_level
        FPS = LEVELS[current_level]["speed"]
        apple_respawn_time = LEVELS[current_level]["apple_respawn_time"]

def draw_grid():
    for x in range(0, res, size):
        for y in range(0, res, size):
            pygame.draw.rect(screen, GRID_COLOR, (x, y, size, size), 1)

def draw_apple():
    for r in range(half_size, 0, -2):
        color = (255, r * 10, r * 10)
        pygame.draw.circle(screen, color, (apple[0] + half_size, apple[1] + half_size), r)

def draw_golden_apple():
    if golden_apple:
        pygame.draw.circle(screen, (255, 215, 0), (golden_apple[0] + half_size, golden_apple[1] + half_size), half_size)

def draw_walls():
    for wall in LEVELS[current_level]["walls"]:
        pygame.draw.rect(screen, WALL_COLOR, (wall[0], wall[1], size, size))

def show_pause():
    text = font.render("Paused (P to Resume, S to Save)", True, (255, 255, 255))
    screen.blit(text, (res // 4, res // 3))
    pygame.display.flip()

# Main game loop
last_apple_spawn_time = pygame.time.get_ticks()
while True:
    pygame.display.set_caption(f"Snake | Score: {score} | Level: {current_level}")
    if paused:
        show_pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_s and conn:
                    save_score(conn, username, score, current_level)
        continue

    screen.fill(BG_COLOR)
    draw_grid()
    draw_walls()
    draw_apple()
    draw_golden_apple()

    # Draw snake
    SNAKE_COLOR = (0, max(255 - current_level * 50, 50), 0)
    for x, y in snake:
        pygame.draw.rect(screen, (0, 80, 0), (x-2, y-2, size+4, size+4), border_radius=10)
        pygame.draw.rect(screen, SNAKE_COLOR, (x, y, size, size), border_radius=5)
    head_x, head_y = snake[-1]
    screen.blit(head_img, (head_x, head_y))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_p:
                paused = True
            elif event.key == pygame.K_n:
                pygame.mixer.music.play(-1)
            elif event.key in (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d):
                new_dirX, new_dirY = direction[chr(event.key)]
                if (new_dirX, new_dirY) != (-dirX, -dirY):
                    dirX, dirY = new_dirX, new_dirY

    # Move snake
    if frame_count % snake_frame_speed == 0:
        newX, newY = snake[-1][0] + dirX, snake[-1][1] + dirY
        snake.append((newX, newY))
        snake = snake[-length:]

        # Check apple collision
        if (newX, newY) == apple:
            apple_spawn()
        elif golden_apple and (newX, newY) == golden_apple:
            golden_apple = None
            score += 2
            length += 2
            eat_sound.play()

        # Check wall and boundary collision
        if (newX, newY) in LEVELS[current_level]["walls"] or \
           newX < 0 or newX >= res or newY < 0 or newY >= res or \
           (newX, newY) in snake[:-1]:
            game_over()

    # Update apple
    if pygame.time.get_ticks() - last_apple_spawn_time > apple_respawn_time:
        apple = (random.randrange(0, res - size, size), random.randrange(0, res - size, size))
        while apple in snake or apple in LEVELS[current_level]["walls"]:
            apple = (random.randrange(0, res - size, size), random.randrange(0, res - size, size))
        last_apple_spawn_time = pygame.time.get_ticks()

    frame_count += 1
    clock.tick(FPS)
    pygame.display.flip()

# Cleanup
if conn:
    conn.close()