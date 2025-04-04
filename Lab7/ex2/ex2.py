import pygame 
import os

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

def show_hotkeys():
    print("🎵 Горячие клавиши музыкального плеера:")
    print("🔹 SPACE - Воспроизвести музыку")
    print("🔹 S - Остановить музыку")
    print("🔹 RIGHT  - Следующий трек")
    print("🔹 LEFT - Предыдущий трек")

show_hotkeys()

music_folder = "/home/nursultan/User Nurs/Projects python/PP2/Lab7/ex2/music"
musics = [os.path.join(music_folder, file) for file in os.listdir(music_folder) if file.endswith(".mp3")]

if not musics:
    print("⚠️ Нет доступных аудиофайлов в папке 'music'.")
    pygame.quit()
    exit()

track = 0
pygame.mixer.music.load(musics[track])

def play():
    pygame.mixer.music.unpause()  # Changed from pause() to unpause() for more logical behavior

def pause():
    pygame.mixer.music.pause()

def next():
    global track
    track = (track + 1) % len(musics)
    pygame.mixer.music.load(musics[track])
    play()

def prev():
    global track
    track = (track - 1) % len(musics)
    pygame.mixer.music.load(musics[track])
    play()

run = True
while run:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause()
            elif event.key == pygame.K_p:
                play()
            elif event.key == pygame.K_s:
                stop()
            elif event.key == pygame.K_RIGHT:
                next()
            elif event.key == pygame.K_LEFT:
                prev()
    pygame.display.flip()

pygame.quit()
