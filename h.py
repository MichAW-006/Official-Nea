import pygame
import random
from c_s import *
from variables import *
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tiny Choices")
Game = game()
blank_rect = pygame.Rect(400, 50, 400, 550)
back_button=Button(pygame.image.load('back.PNG').convert_alpha(),40,20,0.13)
club_buttons = [pygame.Rect(50, 230 + (i * 80), 300, 50) for i in range(len(Game.player.school.clubs))]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
header_rect = pygame.Rect(0, 0, 800, 50)
join_club_button = Text_Button(500, 200, 200, 50)
study_harder_button = Text_Button(500, 300, 200, 50)
bunk_class_button = Text_Button(500, 400, 200, 50)
show_clubs= None
selected_club = None
def draw_progress_bar(x, y, value, max_value, width=200, height=20):
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)  # Border
    fill_width = (value / max_value) * (width - 4)  # Fill width based on value
    pygame.draw.rect(screen, Game.colour_2, (x + 2, y + 2, fill_width, height - 4))
def draw_school_screen():
    
    screen.fill(WHITE)
    pygame.draw.rect(screen, Game.colour_1, header_rect)
    back_button.draw(screen)
    
    screen.blit(Game.fonts[0].render("School", True, BLACK), (80, 15))
    screen.blit(Game.fonts[0].render(f"{Game.player.school.name}", True, BLACK), (20, 65))
    draw_progress_bar(120, 100, Game.player.school.attendance, 100)
    screen.blit(Game.fonts[1].render("Attendance:", True, BLACK), (20, 100))
    draw_progress_bar(120, 150, Game.player.school.behaviour, 100)
    screen.blit(Game.fonts[1].render("Behaviour:", True, BLACK), (20, 150))
    draw_progress_bar(120, 200, Game.player.school.grades, 100)
    screen.blit(Game.fonts[1].render("Grade:", True, BLACK), (20, 200))

    
    join_club_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[1].render("Join a Club", True, BLACK), (550, 215))
    study_harder_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[1].render("Study Harder", True, BLACK), (550, 315))
    bunk_class_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[1].render("Bunk Class", True, BLACK), (550, 415))
    if show_clubs is not None:
        display_clubs()
        
def draw_join(x,y):
    join_button = Text_Button(x+ 250 , y+8,45, 25)
    join_button.draw(screen,Game.colour_2,Game.colour_3)
    screen.blit((Game.fonts[2].render("Join", True, BLACK)), (x + 260, y  + 15))
  


def display_clubs(): 
    i=0
    for club in club_buttons:
        pygame.draw.rect(screen, Game.colour_1, club,border_radius=8)
        screen.blit(Game.fonts[0].render(f"{Game.player.school.clubs[i]}", True, BLACK), (club.x + 10, club.y + 10))
        draw_join(club.x,club.y)
        i+=1


running = True
while running:
    screen.fill(WHITE)  # Clear the screen

    draw_school_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if join_club_button.rect.collidepoint(mouse_pos):
                show_clubs = True
            for i,btn in enumerate(club_buttons):
                if btn.collidepoint(mouse_pos):
                    selected_club = Game.player.school.clubs[i]
                    break
            if selected_club is not None:
                Game.player.school.join_club(Game.player,selected_club)
                selected_club = None
            if bunk_class_button.rect.collidepoint(mouse_pos):
                Game.player.school.bunk_class(Game.player)
            if study_harder_button.rect.collidepoint(mouse_pos):
                Game.player.school.study(Game.player)



    pygame.display.flip()

pygame.quit()
