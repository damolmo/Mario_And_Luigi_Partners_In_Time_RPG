# Mario & Luigi RPG Game

# Global Imports
import os

os.system("pip3 install wget")
os.system("pip3 install pytube")
os.system("pip install pytube")
os.system("pip install pytube3")
os.system("pip3 install pygame")
os.system("pip install pygame")
#os.system("python -m pip install git+https://github.com/pytube/pytube")
os.system("pip install pillow")
os.system("pip install pyperclip")

import pyperclip
import pygame
import tkinter
import wget
import os
import json
import threading
import os.path
import time
from datetime import date
from datetime import datetime
from pathlib import Path
import pytube
from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
import urllib.request
import platform
import pyperclip
from os.path import exists

pygame.font.init() # Import font
pygame.mixer.init() # Import sounds

# Local imports
from resources import *

# Global variables
vec = pygame.math.Vector2

def vec_to_int(vector):
    return int(vector.x), int(vector.y)

def write_json () :
    data = json.dumps(save)
    with open('save.json', 'w') as save_file:
        save_file.write(data)

def check_app_data() :
    save["THREADS"]["TITLE_SCREEN"] = "YES"
    write_json()

def finalize_program() :
    save["THREADS"]["TITLE_SCREEN"] = "NO"
    write_json()

def create_window_animation() :

    while save["THREADS"]["TITLE_SCREEN"] == "YES" :
        create_windows(time_hole_1, enemy_1, princess_1, kylie_1, logo_1, 300, 70)
        clock.tick(5)
        create_windows(time_hole_2, enemy_1, princess_2, kylie_1, logo_1, 300, 70)
        clock.tick(5)
        create_windows(time_hole_3, enemy_1, princess_3, kylie_2, logo_1, 300, 70)
        clock.tick(5)
        create_windows(time_hole_4, enemy_2, princess_4, kylie_2, logo_2, 300, 70)
        clock.tick(5)
        create_windows(time_hole_5, enemy_2, princess_5, kylie_3, logo_2, 300, 70)
        clock.tick(5)
        create_windows(time_hole_6, enemy_2, princess_6, kylie_3, logo_2, 300, 70)
        clock.tick(5)
        create_windows(time_hole_7, enemy_1, princess_7, kylie_4, logo_1, 300, 70)
        clock.tick(5)
        create_windows(time_hole_8, enemy_1, princess_8, kylie_4, logo_1, 300, 70)
        clock.tick(5)
        create_windows(time_hole_9, enemy_1, princess_9, kylie_5, logo_1, 300, 70)
        clock.tick(5)
        create_windows(time_hole_10, enemy_2, princess_10, kylie_5, logo_3, 300, 70)
        clock.tick(5)
        create_windows(time_hole_11, enemy_2, princess_11, kylie_6, logo_3, 300, 70)
        clock.tick(5)
        create_windows(time_hole_12, enemy_2, princess_12, kylie_7, logo_3, 300, 70)
        clock.tick(5)
        create_windows(time_hole_13, enemy_2, princess_13, kylie_7, logo_3, 300, 70)
        clock.tick(5)

        create_windows(time_hole_1_zoom, enemy_1, princess_1, kylie_1, logo_1, 220, 20)
        clock.tick(5)
        create_windows(time_hole_2_zoom, enemy_1, princess_2, kylie_1, logo_1, 220, 20)
        clock.tick(5)
        create_windows(time_hole_3_zoom, enemy_1, princess_3, kylie_2, logo_1, 220, 20)
        clock.tick(5)
        create_windows(time_hole_4_zoom, enemy_2, princess_4, kylie_2, logo_2, 220, 20)
        clock.tick(5)
        create_windows(time_hole_5_zoom, enemy_2, princess_5, kylie_3, logo_2, 220, 20)
        clock.tick(5)
        create_windows(time_hole_6_zoom, enemy_2, princess_6, kylie_3, logo_2, 220, 20)
        clock.tick(5)
        create_windows(time_hole_7_zoom, enemy_1, princess_7, kylie_4, logo_1, 220, 20)
        clock.tick(5)
        create_windows(time_hole_8_zoom, enemy_1, princess_8, kylie_4, logo_1, 220, 20)
        clock.tick(5)
        create_windows(time_hole_9_zoom, enemy_1, princess_9, kylie_5, logo_1, 220, 20)
        clock.tick(5)
        create_windows(time_hole_10_zoom, enemy_2, princess_10, kylie_5, logo_3, 220, 20)
        clock.tick(5)
        create_windows(time_hole_11_zoom, enemy_2, princess_11, kylie_6, logo_3, 220, 20)
        clock.tick(5)
        create_windows(time_hole_12_zoom, enemy_2, princess_12, kylie_7, logo_3, 220, 20)
        clock.tick(5)
        create_windows(time_hole_13_zoom, enemy_2, princess_13, kylie_7, logo_3, 220, 20)
        clock.tick(5)

        create_windows(time_hole_1_zoom_2, enemy_1, princess_1, kylie_1, logo_1, 150, -10)
        clock.tick(5)
        create_windows(time_hole_2_zoom_2, enemy_1, princess_2, kylie_1, logo_1, 150, -10)
        clock.tick(5)
        create_windows(time_hole_3_zoom_2, enemy_1, princess_3, kylie_2, logo_1, 150, -10)
        clock.tick(5)
        create_windows(time_hole_4_zoom_2, enemy_2, princess_4, kylie_2, logo_2, 150, -10)
        clock.tick(5)
        create_windows(time_hole_5_zoom_2, enemy_2, princess_5, kylie_3, logo_2, 150, -10)
        clock.tick(5)
        create_windows(time_hole_6_zoom_2, enemy_2, princess_6, kylie_3, logo_2, 150, -10)
        clock.tick(5)
        create_windows(time_hole_7_zoom_2, enemy_1, princess_7, kylie_4, logo_1, 150, -10)
        clock.tick(5)
        create_windows(time_hole_8_zoom_2, enemy_1, princess_8, kylie_4, logo_1, 150, -10)
        clock.tick(5)
        create_windows(time_hole_9_zoom_2, enemy_1, princess_9, kylie_5, logo_1, 150, -10)
        clock.tick(5)
        create_windows(time_hole_10_zoom_2, enemy_2, princess_10, kylie_5, logo_3, 150, -10)
        clock.tick(5)
        create_windows(time_hole_11_zoom_2, enemy_2, princess_11, kylie_6, logo_3, 150, -10)
        clock.tick(5)
        create_windows(time_hole_12_zoom_2, enemy_2, princess_12, kylie_7, logo_3, 150, -10)
        clock.tick(5)
        create_windows(time_hole_13_zoom_2, enemy_2, princess_13, kylie_7, logo_3, 150, -10)
        clock.tick(5)

        


def create_windows(animation, enemy, enemy_2, friend, logo, hole_width, hole_height) :

    # Background color
    WIN.fill("#000000")

    # Background image
    WIN.blit(background, (0, 0))

    # Time hole animation
    WIN.blit(animation, (hole_width, hole_height))

    # Second boss
    #WIN.blit(enemy_2, (470, 20))

    # Game logo
    WIN.blit(logo, (300, 50))

    # First boss
    WIN.blit(enemy, (20, 50))

    # First friend
    WIN.blit(friend, (1050, 300))


    # Copyright str
    nintendo_copyright = small_font.render("© 2005 – 2006 NINTENDO", 1, BLACK)
    WIN.blit(nintendo_copyright, (20, 20))

    my_copyright =  small_font.render("© 2022 daviiid99", 1, BLACK)
    WIN.blit(my_copyright, (1100, 20))


    all_copyright = mini_font.render("DEVELOPED BY ALPHADREAM", 1, BLACK)
    WIN.blit(all_copyright, (530, 580))

    all_copyright = mini_font.render("ALL RIGHTS, INCLUDING THE COPYRIGHTS OF GAME, SCENARIO, MUSIC AND PROGRAM", 1, BLACK)
    WIN.blit(all_copyright, (350, 600))


    pygame.display.update()



class Main :


    def __init__(self) :
        pygame.init()
        self.running = True
        self.screen = WIN
        self.rect = self.screen.get_rect()
        self.mouse = vec()
        self.mouse_visible = True
        self.clock = pygame.time.Clock()
        self.music_time = 0

    def check_click(self, mouse) :
        if self.rect.collidepoint(mouse):
            finalize_program()
            write_json()

    def user_control(self) :

        while save["THREADS"]["TITLE_SCREEN"] == "YES" :
            for event in pygame.event.get():

                if event.type == pygame.QUIT :
                    run = False
                    pygame.quit()


                if event.type == pygame.MOUSEBUTTONDOWN :
                    self.check_click(event.pos)

    def play_music(self) :

        while save["THREADS"]["TITLE_SCREEN"] == "YES" :
            self.music_time +=1
            
            if self.music_time >=63 :
                title_screen_music.play()
                self.music_time = 0


    def start_threads(self) :
        check_app_data()

        # Create two new threads
        thread_1 = threading.Thread(target = self.user_control, name ="mouse")
        thread_2 = threading.Thread(target = create_window_animation, name="ui")
        thread_3 = threading.Thread(target = self.play_music, name="ui")


        # Start Both Threads
        thread_2.start()
        thread_1.start()
        thread_3.start()

        start = self.user_control()

        # Wait for both threads to end
        while save["THREADS"]["TITLE_SCREEN"] == "YES" :
            thread_2.join()
            thread_1.join()
            thread_3.join()

        

    def start_program(self) :
        while self.running :
            self.start_threads()


game = Main()
game.start_program()