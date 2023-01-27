'''

    Game: Angry Hearts
    File: main.py

    Contents: The Main file to Start the Game!

    Requirements: Pygame, sys, random, math
    Supporting Modules: interface.py, physics_engine.py, maps.py, objects.py

'''
import pygame
import sys
import random
from math import *

import physics_engine
import objects
import maps
import interface

pygame.init()
width = 1500
height = 700
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

physics_engine.init(display)
objects.init(display)
maps.init(display)
interface.init(display)

background = (149, 197, 204)

def close():
    pygame.quit()
    sys.exit()

def start_game(map):
    map.draw_map()

def GAME():
    map = maps.Maps()

    welcome = interface.Label(700, 100, 400, 200, None, background)
    welcome.add_text("Angry Hearts", 80, "Fonts/arfmoochikncheez.ttf", (236, 240, 241))

    caption1 = interface.Label(700, 150, 400, 200, None, background)
    caption1.add_text("Check out this Angry Birds-inspired game I coded from scratch!", 30, "Fonts/arfmoochikncheez.ttf", (236, 240, 241))

    caption2 = interface.Label(700, 200, 400, 200, None, background)
    caption2.add_text("Launch hearts from a catapult at some of my interests to show them some love!<3", 30, "Fonts/arfmoochikncheez.ttf", (236, 240, 241))

    caption3 = interface.Label(700, 250, 400, 200, None, background)
    caption3.add_text("Hold down your mouse and pull back on the heart to aim and release to launch!", 30, "Fonts/arfmoochikncheez.ttf", (236, 240, 241))

    start = interface.Button(500, 400, 300, 100, start_game, (244, 208, 63), (247, 220, 111))
    start.add_text("START GAME", 60, "Fonts/arfmoochikncheez.ttf", background)

    exit = interface.Button(1000, 400, 300, 100, close, (241, 148, 138), (245, 183, 177))
    exit.add_text("QUIT", 60, "Fonts/arfmoochikncheez.ttf", background)

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit.isActive():
                    exit.action()
                if start.isActive():
                    start_game(map)

        display.fill(background)

        start.draw()
        caption1.draw()
        caption2.draw()
        caption3.draw()
        exit.draw()
        welcome.draw()

        pygame.display.update()
        clock.tick(60)

GAME()
