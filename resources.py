import os
import pygame
import json
import sys
import ctypes


## Screen properties
pygame.init()
width, height = 640, 480
fpsClock = pygame.time.Clock()
WIN = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
if sys.platform == "win32":
    HWND = pygame.display.get_wm_info()['window']
    SW_MAXIMIZE = 3
    ctypes.windll.user32.ShowWindow(HWND, SW_MAXIMIZE)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (93.3,13.3,16.1)


## Application Values
FPS = 60
clock = pygame.time.Clock()
small_font = pygame.font.Font(None, 30)
large_font = pygame.font.Font(None, 50)
mini_font = pygame.font.Font(None, 18)

## App External Data
my_data = open("save.json")
save = json.load(my_data)

## App Internal Info
#icon = pygame.image.load('Assets/logo/yt_01.gif')
#pygame.display.set_icon(icon)
pygame.display.set_caption("Mario & Luigi : Partners In Time")

## Assets
# Title Screen
background = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "background.png")), (1300, 700))
logo_1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "logo.png")), (650, 500))
logo_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "logo_2.png")), (650, 500))
logo_3 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "logo_3.png")), (650, 500))


time_hole_1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole.png")), (650, 500))
time_hole_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_2.png")), (650, 500))
time_hole_3 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_3.png")), (650, 500))
time_hole_4 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_4.png")), (650, 500))
time_hole_5 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_5.png")), (650, 500))
time_hole_6 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_6.png")), (650, 500))
time_hole_7 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_7.png")), (650, 500))
time_hole_8 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_8.png")), (650, 500))
time_hole_9 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_9.png")), (650, 500))
time_hole_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_10.png")), (650, 500))
time_hole_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_11.png")), (650, 500))
time_hole_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_12.png")), (650, 500))
time_hole_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_13.png")), (650, 500))

time_hole_1_zoom = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole.png")), (800, 650))
time_hole_2_zoom = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_2.png")), (800, 650))
time_hole_3_zoom = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_3.png")), (800, 650))
time_hole_4_zoom = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_4.png")), (800, 650))
time_hole_5_zoom = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_5.png")), (800, 650))
time_hole_6_zoom = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_6.png")), (800, 650))
time_hole_7_zoom = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_7.png")), (800, 650))
time_hole_8_zoom = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_8.png")), (800, 650))
time_hole_9_zoom = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_9.png")), (800, 650))
time_hole_10_zoom = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_10.png")), (800, 650))
time_hole_11_zoom = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_11.png")), (800, 650))
time_hole_12_zoom = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_12.png")), (800, 650))
time_hole_13_zoom = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_13.png")), (800, 650))

time_hole_1_zoom_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole.png")), (950, 800))
time_hole_2_zoom_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_2.png")), (950, 800))
time_hole_3_zoom_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_3.png")), (950, 800))
time_hole_4_zoom_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_4.png")), (950, 800))
time_hole_5_zoom_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_5.png")), (950, 800))
time_hole_6_zoom_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_6.png")), (950, 800))
time_hole_7_zoom_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_7.png")), (950, 800))
time_hole_8_zoom_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_8.png")), (950, 800))
time_hole_9_zoom_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_9.png")), (950, 800))
time_hole_10_zoom_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_10.png")), (950, 800))
time_hole_11_zoom_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_11.png")), (950, 800))
time_hole_12_zoom_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_12.png")), (950, 800))
time_hole_13_zoom_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "time_hole_13.png")), (950, 800))

enemy_1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "enemy_1.png")), (228, 486))
enemy_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "enemy_2.png")), (228, 486))

kylie_1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "kylie_1.png")), (120, 160))
kylie_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "kylie_2.png")), (120, 160))
kylie_3 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "kylie_3.png")), (120, 160))
kylie_4 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "kylie_4.png")), (120, 160))
kylie_5 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "kylie_5.png")), (120, 160))
kylie_6 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "kylie_6.png")), (120, 160))
kylie_7 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "kylie_7.png")), (120, 160))

princess_1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "princess_1.png")), (272, 234))
princess_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "princess_2.png")), (272, 234))
princess_3 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "princess_3.png")), (272, 234))
princess_4 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "princess_4.png")), (272, 234))
princess_5 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "princess_5.png")), (272, 234))
princess_6 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "princess_6.png")), (272, 234))
princess_7 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "princess_7.png")), (272, 234))
princess_8 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "princess_8.png")), (272, 234))
princess_9 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "princess_9.png")), (272, 234))
princess_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "princess_10.png")), (272, 234))
princess_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "princess_11.png")), (272, 234))
princess_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "princess_12.png")), (272, 234))
princess_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/title_screen', "princess_13.png")), (272, 234))

## Music
# Title Screen
# Sound effect
title_screen_music = pygame.mixer.Sound("music/title.mp3")