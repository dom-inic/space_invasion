# # debugger for the main file for running the game
# import sys

# import pygame

# def run_game():
#     pygame.init()
    
#     screen = pygame.display.set_mode((1200,800))
#     pygame.display.set_caption("alien invasion")
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()

#         pygame.display.flip()

# run_game()
from tkinter import *
root = Tk()
root.minsize=(400,400)
root.mainloop()
