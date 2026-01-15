#Building a singing keyboard for my computer locally

import pygame
import keyboard 

pygame.mixer.init()
sounds = {
    'a': pygame.mixer.Sound("cow-mooing-343423.mp3"),
    'n': pygame.mixer.Sound("woofbig2-40265.mp3"),
    'u': pygame.mixer.Sound("goofy-ahh-car-horn-200870.mp3"),
    'r': pygame.mixer.Sound("horse-neigh-390297.mp3"),
}

print("Press keys to play sounds....(ESC TO QUIT!!!)")

while True:
    for key in sounds:
        if keyboard.is_pressed(key):
            sounds[key].play()
    if keyboard.is_pressed('esc'):
        break 