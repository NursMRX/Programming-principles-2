import pygame
import sys
import random
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Гонки")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
ROAD_COLOR = (100, 100, 100)

# Границы дороги
ROAD_LEFT = 120
ROAD_RIGHT = 720

# Игровые переменные
SPEED = 5
SCORE = 0
MONEY = 0
COINS_TO_INCREASE_SPEED = 5
ENEMY_SPEED_INCREMENT = 0.5
FPS = 60

# Загрузка изображений
try:
    # Фон дороги
    background_img = pygame.image.load("/home/nursultan/Projects python/PP2/Lab9/racer/background.png").convert()
    background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Машина игрока
    player_img = pygame.image.load("/home/nursultan/Projects python/PP2/Lab9/racer/Player.png").convert_alpha()
    player_img = pygame.transform.scale(player_img, (50, 80))
    
    # Машина врага
    enemy_img = pygame.image.load("/home/nursultan/Projects python/PP2/Lab9/racer/Enemy.png").convert_alpha()
    enemy_img = pygame.transform.scale(enemy_img, (50, 80))
    
    # Монетка (используем одну картинку для всех типов)
    coin_img = pygame.image.load("/home/nursultan/Projects python/PP2/Lab9/racer/coin.png").convert_alpha()
    coin_img = pygame.transform.scale(coin_img, (40, 40))
except Exception as e:
    print(f"Ошибка загрузки изображений: {e}")
    pygame.quit()
    sys.exit()

# Шрифты
font = pygame.font.SysFont(None, 36)
game_over_font = pygame.font.SysFont(None, 72)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.randint(1, 3)  # 1, 2, 3 для трех типов монет
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.reset_position()
        self.value = self.type  # Значение монеты
        
    def reset_position(self):
        self.rect.center = (random.randint(ROAD_LEFT+40, ROAD_RIGHT-120), 
        random.randint(-100, -40))
        self.speed = random.randint(2, 5)
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.reset_position()
        self.speed = SPEED
        
    def reset_position(self):
        self.rect.center = (random.randint(ROAD_LEFT+40, ROAD_RIGHT-40), -100)
    
    def update(self):
        global SCORE
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.reset_position()
    
    def increase_speed(self, increment):
        self.speed += increment

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
        self.speed = 5
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
            self.rect.x -= self.speed
        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            self.rect.x += self.speed
        
        # Ограничение движения в пределах дороги
        if self.rect.left < ROAD_LEFT:
            self.rect.left = ROAD_LEFT
        if self.rect.right > ROAD_RIGHT:
            self.rect.right = ROAD_RIGHT

def main():
    clock = pygame.time.Clock()
    background_y = 0
    global MONEY, SCORE
    
    # Создание спрайтов
    player = Player()
    enemy = Enemy()
    coin = Coin()
    
    # Группы спрайтов
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player, enemy, coin)
    
    enemies = pygame.sprite.Group(enemy)
    coins = pygame.sprite.Group(coin)
    
    # Таймер для увеличения скорости
    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 1000)
    
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == INC_SPEED:
                enemy.speed += 0.1
        
        # Движение фона
        background_y += SPEED
        if background_y >= SCREEN_HEIGHT:
            background_y = 0
        
        # Отрисовка
        screen.blit(background_img, (0, background_y - SCREEN_HEIGHT))
        screen.blit(background_img, (0, background_y))
        
        # Обновление спрайтов
        all_sprites.update()
        
        # Проверка столкновений с врагом
        if pygame.sprite.spritecollide(player, enemies, False):
            pygame.mixer.Sound("/home/nursultan/Projects python/PP2/Lab9/racer/crash.wav").play()
            game_over_text = game_over_font.render("GAME OVER", True, RED)
            screen.blit(game_over_text, (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2 - 36))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False
            
        # Проверка сбора монет
        hits = pygame.sprite.spritecollide(player, coins, True)
        for hit in hits:
            MONEY += hit.value
            if MONEY % COINS_TO_INCREASE_SPEED == 0:
                enemy.increase_speed(ENEMY_SPEED_INCREMENT)
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
        
        # Отрисовка всех спрайтов
        all_sprites.draw(screen)
        
        # Отображение счета
        score_text = font.render(f"Счет: {SCORE}", True, BLACK)
        money_text = font.render(f"Монеты: {MONEY}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(money_text, (10, 50))
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()