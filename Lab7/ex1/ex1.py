import pygame
import sys
import time

pygame.init()
WIDTH, HEIGHT = 1400, 1050
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock_img = pygame.image.load("/home/nursultan/Projects python/PP2/Lab7/ex1/clock.png")
minute_hand = pygame.image.load("/home/nursultan/Projects python/PP2/Lab7/ex1/rightarm.png")
second_hand = pygame.image.load("/home/nursultan/Projects python/PP2/Lab7/ex1/leftarm.png")


clock_center = (WIDTH // 2, HEIGHT // 2)

def draw_hand(image, angle, center):
    """Функция поворота изображения и его отрисовки."""
    rotated_image = pygame.transform.rotate(image, -angle)
    rect = rotated_image.get_rect(center=center)
    screen.blit(rotated_image, rect)

fps = pygame.time.Clock()

run = True
while run:
    screen.fill((0, 0, 0)) 
    screen.blit(clock_img, (0, 0))  

    ltime = time.localtime()
    second = ltime.tm_sec
    minute = ltime.tm_min

    minute_angle = minute * 6  
    second_angle = second * 6  

    draw_hand(minute_hand, minute_angle, clock_center)
    draw_hand(second_hand, second_angle, clock_center)

    pygame.display.flip() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    fps.tick(60)  

pygame.quit()
sys.exit()
