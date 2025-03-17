import pygame
import random
from c_s import *
from variables import *

pygame.init()
Game=game()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Life Simulator")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
apply_for_job_button = Text_Button(500,450,200,50)
header_rect = pygame.Rect(0, 0, 800, 50)
back_button=Button(pygame.image.load('back.PNG').convert_alpha(),20,20,0.13)
potential_jobs = [pygame.Rect(20, 80 + (i * 50), 300, 40) for i in range(len(Game.jobs))]

selected_job = None

def draw_progress_bar(x, y, value, max_value, width=200, height=20):
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)  # Border
    fill_width = (value / max_value) * (width - 4)  # Fill width based on value
    pygame.draw.rect(screen, Game.colour_2, (x + 2, y + 2, fill_width, height - 4))

def draw_potential_jobs_screen():
    screen.fill(WHITE)
    pygame.draw.rect(screen, Game.colour_1, header_rect)
    back_button.draw(screen)
    screen.blit(Game.fonts[0].render("Job Opportunities", True, BLACK), (50, 15))


    for i in range(len(Game.jobs)):
        job_button = Text_Button(10, 80 + (i * 50), 395, 40)
        job_button.draw(screen,Game.colour_1,Game.colour_2)
        screen.blit(Game.fonts[0].render(f"{Game.jobs[i].title} ", True, BLACK), (job_button.x + 10, job_button.y + 10))

    
    # Display stats if an potential_job is selected
    if selected_job is not None:
        display_job(selected_job)

def display_job(potential_job):
    screen.blit(Game.fonts[0].render(f"Job Details", True, BLACK), (420, 70))
    screen.blit(render_text_list(wrap_text(f"{potential_job.title} at {potential_job.work_place}", Game.fonts[1], 350), Game.fonts[1], BLACK), (420, 100))
    screen.blit(Game.fonts[1].render(f"Salary: {potential_job.salary:,}", True, BLACK), (420, 140))
    screen.blit(Game.fonts[1].render(f"Experience Required: ", True, BLACK), (420, 165))
    draw_progress_bar(595,163,potential_job.experience_required,100)
    apply_for_job_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render(f"Apply For Job", True, BLACK), (apply_for_job_button.x+15, apply_for_job_button.y+15))


    j=0
    screen.blit(Game.fonts[1].render(f"Degree needed", True, BLACK), (420, 195))
    for degree in potential_job.education:
        screen.blit(Game.fonts[1].render(f"{degree}", True, BLACK), (420, 225+j))
        j+=20
            

running = True
while running:
    screen.fill(WHITE)  
    draw_potential_jobs_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i,btn in enumerate(Game.jobs):
                if btn.collidepoint(mouse_pos):
                    selected_job = Game.jobs[i]
                    break
                if selected_job is not None:
                    pass
                  
                        
                                

    pygame.display.flip()

pygame.quit()
