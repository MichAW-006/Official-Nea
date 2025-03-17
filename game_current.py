import pygame
import random
from c_s import *
from variables import *
from button_store import *

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tiny Choices")
Game = game()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Rectangles
header_rect = pygame.Rect(0, 0, 800, 50)
stats_rect = pygame.Rect(0, 0, 400, 50)
choice_rect = pygame.Rect(400, 250, 420, 230)
history_rect = pygame.Rect(0, 50, 400, 350)
options_rect = pygame.Rect(0, 400, 400, 200)
settings_rect = pygame.Rect(400, 500, 400, 100)
blank_rect1 = pygame.Rect(400, 50, 400, 550)
blank_rect2 = pygame.Rect(0, 230, 400, 550)

# Start Up Buttons
new_game_button = Button(pygame.image.load('new_game.PNG').convert_alpha(), 400, 320, 1)
resume_button = Button(pygame.image.load('resume.PNG').convert_alpha(), 400, 400, 1)
options_button = Button(pygame.image.load('settings.PNG').convert_alpha(), 400, 480, 1)
quit_button = Button(pygame.image.load('quit.PNG').convert_alpha(), 400, 560, 1)

# Player property buttons
sell_buttons = []
find_button = pygame.Rect(600, 60, 150, 35)

# NPC buttons
npc_buttons = [pygame.Rect(20, 80 + (i * 50), 300, 40) for i in range(len(Game.npcs))]

# Relationship buttons
relationship_buttons = [pygame.Rect(20, 80 + (i * 50), 300, 40) for i in range(len(Game.player.relationships))]

potential_jobs = [pygame.Rect(20, 80 + (i * 50), 300, 40) for i in range(len(Game.jobs))]

club_buttons = [pygame.Rect(50, 230 + (i * 80), 300, 50) for i in range(len(Game.player.school.clubs))]
degree_buttons = [pygame.Rect(50, 230 + (i * 80), 300, 50) for i in range(len(Game.player.school.degrees))]
back_button = Button(pygame.image.load('back.PNG').convert_alpha(), 20, 20, 0.13)

# Main screen buttons
age_up_button = Button(pygame.image.load('age_up.PNG').convert_alpha(),200,450,0.27)
school_button = Button(pygame.image.load('school.PNG').convert_alpha(),80,505,0.3)
property_button = Button(pygame.image.load('property.PNG').convert_alpha(),200,550,0.27)
relationships_button = Button(pygame.image.load('relationships.PNG').convert_alpha(),320,505,0.3)
work_button = Button(pygame.image.load('work.PNG').convert_alpha(),80,505,0.3)



# Selected variables
selected_job = None
selected_player_property = None
selected_relationship = None
selected_npc = None
selected_property = None
selected_colour_scheme = None
show_clubs= None
selected_club = None
show_degrees =None

progress_bar_colours= [(220,20,60),(255,147,74),(128,240,78)]
# Game state
choices = show_choices_and_option(check_available_choices(Game.player))
make_choice = True

# Functions
def draw_progress_bar(x, y, value, max_value, width=200, height=20):
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)
    fill_width = (value / max_value) * (width - 4)
    if value/max_value > 0.7 :
        pygame.draw.rect(screen, progress_bar_colours[2], (x + 2, y + 2, fill_width, height - 4))
    elif value/max_value >0.35 :
        pygame.draw.rect(screen, progress_bar_colours[1], (x + 2, y + 2, fill_width, height - 4))
    else:
        pygame.draw.rect(screen, progress_bar_colours[0], (x + 2, y + 2, fill_width, height - 4))
        

def draw_start_up_screen():
    screen.blit(pygame.image.load('start_up.JPG'), (0, 0))
    new_game_button.draw(screen)
    resume_button.draw(screen)
    options_button.draw(screen)
    quit_button.draw(screen)

def draw_main_screen():
    screen.fill(WHITE)
    global selected_job, selected_player_property, selected_relationship, selected_npc, selected_property, relationship_buttons, selected_colour_scheme,show_clubs

    selected_job = None
    selected_player_property = None
    selected_relationship = None
    selected_npc = None
    selected_property = None
    selected_colour_scheme = None
    show_clubs = None
    relationship_buttons = [pygame.Rect(20, 80 + (i * 50), 300, 40) for i in range(len(Game.player.relationships))]


    pygame.draw.rect(screen, Game.colour_1, header_rect)
    pygame.draw.rect(screen, Game.colour_1, stats_rect)
    pygame.draw.rect(screen, Game.colour_2, choice_rect)
    pygame.draw.rect(screen, Game.colour_3, options_rect)
    pygame.draw.rect(screen, Game.colour_1, settings_rect)

    choice_1.draw(screen,Game.colour_1,Game.colour_2)
    choice_2.draw(screen,Game.colour_1,Game.colour_2)
    choice_3.draw(screen,Game.colour_1,Game.colour_2)

    age_up_button.draw(screen)
    
    relationships_button.draw(screen)
    if Game.player.age>17:
        property_button.draw(screen)
    if Game.player.age>4:
        school_button.draw(screen)
    if Game.player.age>20:
        work_button.draw(screen)

    screen.blit(Game.fonts[0].render(f"{Game.player.name} {Game.player.surname}", True, WHITE), (20, 15))
    screen.blit(Game.fonts[0].render("Stats", True, WHITE), (600, 15))
    screen.blit(Game.fonts[0].render("Settings", True, BLACK), (560, 550))
    screen.blit(render_text_list(wrap_text(choices[0], Game.fonts[1], 400), Game.fonts[1], BLACK), (420, 260))
    screen.blit(Game.fonts[1].render(f"{choices[1]}", True, BLACK), (450, 320))
    screen.blit(Game.fonts[1].render(f"{choices[2]}", True, BLACK), (450, 370))
    screen.blit(Game.fonts[1].render(f"{choices[3]}", True, BLACK), (450, 420))

    # Stats text
    screen.blit(Game.fonts[1].render(f"Age: {Game.player.age}", True, BLACK), (420, 80))
    screen.blit(Game.fonts[1].render(f"Money: {Game.player.money:,}", True, BLACK), (420, 100))

    # Progress Bars
    draw_progress_bar(420, 120, Game.player.health, 100)
    screen.blit(Game.fonts[1].render(f"Health: {Game.player.health}%", True, BLACK), (630, 120))

    draw_progress_bar(420, 145, Game.player.mood, 100)
    screen.blit(Game.fonts[1].render(f"Mood: {Game.player.mood}%", True, BLACK), (630, 145))

    draw_progress_bar(420, 170, Game.player.intelligence, 100)
    screen.blit(Game.fonts[1].render(f"Smarts: {Game.player.intelligence}%", True, BLACK), (630, 170))

    y_offset = 80
    for event_text in Game.history[-10:]:
        screen.blit(render_text_list(wrap_text(event_text, Game.fonts[1], 400), Game.fonts[1], BLACK), (10, y_offset))
        y_offset += 20

def draw_relationships_screen():
    screen.fill(WHITE)
    pygame.draw.rect(screen, Game.colour_1, header_rect)
    pygame.draw.rect(screen, WHITE, blank_rect1)
    back_button.draw(screen)

    for i in range(len(Game.player.relationships)):
        relationship_button = Text_Button(20, 80 + (i * 50), 300, 40)
        relationship_button.draw(screen,Game.colour_1,Game.colour_2)
        screen.blit(Game.fonts[0].render(f"{Game.player.relationships[i].name} {Game.player.relationships[i].surname} ", True, BLACK), (relationship_button.x + 10, relationship_button.y + 10))
    make_new_relationships_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render("Make New Friends", True, WHITE), (make_new_relationships_button.x + 10, make_new_relationships_button.y + 15))

    if selected_relationship is not None:
        display_relationships(selected_relationship)

def display_relationships(npc):
    pygame.draw.rect(screen, WHITE, blank_rect1)
    screen.blit(Game.fonts[0].render(f"{npc.name}'s Stats", True, BLACK), (550, 20))
    screen.blit(Game.fonts[1].render(f"Age: {npc.age}", True, BLACK), (440, 120))
    draw_progress_bar(440, 150, npc.health, 100)
    screen.blit(Game.fonts[1].render("Health", True, BLACK), (655, 150))
    draw_progress_bar(440, 180, npc.relationship_level, 100)
    screen.blit(Game.fonts[1].render("Relationship", True, BLACK), (655, 180))
    screen.blit(Game.fonts[1].render("Money", True, BLACK), (655, 210))
    draw_progress_bar(440, 210, npc.money / 100, 100)

    conversate_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render("Have a chat", True, WHITE), (conversate_button.x + 10, conversate_button.y + 15))
    ask_for_money_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render("Ask for money", True, WHITE), (ask_for_money_button.x + 10, ask_for_money_button.y + 15))

    if npc.relationship_type == 'Sibling':
        start_fight_button.draw(screen,Game.colour_1,Game.colour_2)
        screen.blit(Game.fonts[0].render("Start a fight", True, WHITE), (start_fight_button.x + 10, start_fight_button.y + 15))
    elif npc.relationship_type == 'Significant Other':
        break_up_button.draw(screen,Game.colour_1,Game.colour_2)
        screen.blit(Game.fonts[0].render("End this relationship", True, WHITE), (start_fight_button.x + 10, start_fight_button.y + 15))
    elif npc.relationship_type == 'Friend':
        stop_being_friends.draw(screen,Game.colour_1,Game.colour_2)
        screen.blit(Game.fonts[0].render("Stop being friends", True, WHITE), (start_fight_button.x + 10, start_fight_button.y + 15))

def draw_settings_screen():
    pygame.draw.rect(screen, Game.colour_1, header_rect)
    back_button.draw(screen)
    screen.blit(Game.fonts[0].render('Settings', True, WHITE), (50, 15))
    reverse_year_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render("Go back a year", True, WHITE), (reverse_year_button.x + 10, reverse_year_button.y + 15))
    start_new_game_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render("New Life", True, WHITE), (start_new_game_button.x + 10, start_new_game_button.y + 15))
    sound_effects_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render("Sound effects", True, WHITE), (sound_effects_button.x + 10, sound_effects_button.y + 15))
    colour_blind_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render("Colour blind filter", True, WHITE), (colour_blind_button.x + 10, colour_blind_button.y + 15))
    save_game.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render("Save game", True, WHITE), (save_game.x + 10, save_game.y + 15))
    load_game_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render("Load Game", True, WHITE), (load_game_button.x + 10, load_game_button.y + 15))
    screen.blit(Game.fonts[0].render("Colours for Colour scheme", True, BLACK), (20, 52))
    change_colour_1_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render("Change main colour", True, WHITE), (change_colour_1_button.x + 10, change_colour_1_button.y + 15))
    change_colour_2_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render("Change secondary colour", True, WHITE), (change_colour_2_button.x + 10, change_colour_2_button.y + 15))
    change_colour_3_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render("Change tertiary colour", True, WHITE), (change_colour_3_button.x + 10, change_colour_3_button.y + 15))

    if selected_colour_scheme is not None:
        display_colours()

def display_colours():
    for colour_button in colour_buttons:
        colour_button.draw(screen)

def draw_potential_relationships_screen():
    screen.fill(WHITE)
    pygame.draw.rect(screen, Game.colour_1, header_rect)
    pygame.draw.rect(screen, WHITE, blank_rect1)
    back_button.draw(screen)

    for i in range(len(Game.npcs)):
        npc_button = Text_Button(20, 80 + (i * 50), 300, 40)
        npc_button.draw(screen,Game.colour_1,Game.colour_2)
        screen.blit(Game.fonts[0].render(f"{Game.npcs[i].name} {Game.npcs[i].surname} ", True, BLACK), (npc_button.x + 10, npc_button.y + 10))

    if selected_npc is not None:
        display_potential_relationships(selected_npc)

def display_potential_relationships(npc):
    screen.blit(Game.fonts[0].render(f"{npc.name}'s Stats", True, BLACK), (550, 20))
    screen.blit(Game.fonts[1].render(f"Age: {npc.age}", True, BLACK), (440, 120))
    draw_progress_bar(440, 150, npc.health, 100)
    screen.blit(Game.fonts[1].render("Health", True, BLACK), (655, 150))
    screen.blit(Game.fonts[1].render("Money", True, BLACK), (655, 180))
    draw_progress_bar(440, 180, npc.money / 100, 100)
    ask_to_be_friends_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render("Offer to be friends", True, WHITE), (ask_to_be_friends_button.x + 10, ask_to_be_friends_button.y + 15))
    ask_to_date_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[0].render("Ask to date", True, WHITE), (ask_to_date_button.x + 10, ask_to_date_button.y + 15))

def draw_property_card(x, y, width, height, property):
    card_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, Game.colour_3, card_rect, border_radius=10)

    name_surface = Game.fonts[0].render(property.type, True, BLACK)
    screen.blit(name_surface, (x + 10, y + 10))

    price_surface = Game.fonts[2].render(f"Price: ${property.price:,}", True, BLACK)
    screen.blit(price_surface, (x + 10, y + 50))

    draw_progress_bar(x + 80, y + 80, property.condition, 100, 100, 10)
    condition_text = Game.fonts[2].render("Condition:", True, BLACK)
    condition_number = Game.fonts[2].render(f"{property.condition}%", True, BLACK)
    screen.blit(condition_text, (x + 10, y + 80))
    screen.blit(condition_number, (x + 183, y + 80))

    location_surface = Game.fonts[2].render(f"Location: {property.location}", True, BLACK)
    screen.blit(location_surface, (x + 10, y + 110))

    buy_text = Game.fonts[2].render("Buy with cash", True, WHITE)
    mort_text = Game.fonts[2].render("Apply for mortgage", True, WHITE)
    buy_button = Text_Button(x + 10, y + height - 40, width - 20, 25)
    buy_button.draw(screen,Game.colour_1,Game.colour_2)
    mortgage_button = Text_Button(x + 10, y + height - 70, width - 20, 25)
    mortgage_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(buy_text, (x + 20, y + height - 35))
    screen.blit(mort_text, (x + 20, y + height - 65))

    return card_rect, buy_button, mortgage_button

def draw_owned_property_card(x, y, width, height, property):
    card_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, Game.colour_3, card_rect, border_radius=10)

    name_surface = Game.fonts[0].render(property.type, True, BLACK)
    screen.blit(name_surface, (x + 10, y + 10))

    price_surface = Game.fonts[2].render(f"Price: ${property.price:,}", True, BLACK)
    screen.blit(price_surface, (x + 10, y + 50))

    draw_progress_bar(x + 80, y + 80, property.condition, 100, 100, 10)
    condition_text = Game.fonts[2].render("Condition:", True, BLACK)
    condition_number = Game.fonts[2].render(f"{property.condition}%", True, BLACK)
    screen.blit(condition_text, (x + 10, y + 80))
    screen.blit(condition_number, (x + 183, y + 80))

    location_surface = Game.fonts[2].render(f"Location: {property.location}", True, BLACK)
    screen.blit(location_surface, (x + 10, y + 110))

    sell_button = Text_Button(x + 10, y + height - 40, width - 20, 25)
    sell_button.draw(screen,Game.colour_1,Game.colour_2)
    sell_text = Game.fonts[2].render("Sell this", True, WHITE)
    screen.blit(sell_text, (x + 20, y + height - 35))

    return card_rect, sell_button

def draw_properties_screen():
    screen.fill(WHITE)
    pygame.draw.rect(screen, Game.colour_1, find_button)
    screen.blit(Game.fonts[1].render("Find Properties", True, BLACK), (613, 72))

    pygame.draw.rect(screen, Game.colour_1, header_rect)
    back_button.draw(screen)
    title_surface = Game.fonts[0].render("Owned Properties", True, BLACK)
    screen.blit(title_surface, (50, 20))
    back_button.draw(screen)
    money_surface = Game.fonts[2].render(f"Money: ${Game.player.money}", True, BLACK)
    screen.blit(money_surface, (800 - 200, 20))

    card_width = 210
    card_height = 220
    margin = 20

    sell_buttons = []

    for i, property in enumerate(Game.player.properties):
        row = i // 3
        col = i % 3
        x = 50 + col * (card_width + margin)
        y = 100 + row * (card_height + margin)
        card_rect, sell_button = draw_owned_property_card(x, y, card_width, card_height, property)
        sell_buttons.append((sell_button, property))

    return sell_buttons

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
            
def draw_work_screen():
    screen.fill(WHITE)
    pygame.draw.rect(screen, Game.colour_1, header_rect)
    back_button.draw(screen)
    screen.blit(Game.fonts[0].render("Work", True, BLACK), (80, 15))
    screen.blit(Game.fonts[0].render(f"{Game.player.job.title}", True, BLACK), (20, 65))
    draw_progress_bar(120, 100, Game.player.job.work_ethic, 100)
    screen.blit(Game.fonts[1].render("Work Ethic:", True, BLACK), (20, 100))
    draw_progress_bar(163, 150, Game.player.job.work_life_balance, 10)
    screen.blit(Game.fonts[1].render("Work life balance:", True, BLACK), (20, 150))


    find_job_button.draw(screen,Game.colour_3,Game.colour_2)
    screen.blit(Game.fonts[1].render("Find a new job", True, BLACK), (find_job_button.x+20, find_job_button.y+15))
    work_harder_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[1].render("Work Harder", True, BLACK), (work_harder_button.x+50, work_harder_button.y+15))
    ask_for_promotion_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[1].render("Ask for a promotion", True, BLACK), (ask_for_promotion_button.x+30, ask_for_promotion_button.y+15))
    quit_job_button.draw(screen,Game.colour_1,Game.colour_2)
    screen.blit(Game.fonts[1].render("Quit Job", True, BLACK), (quit_job_button.x+60, quit_job_button.y+15))

def draw_potential_properties_screen():
    screen.fill(WHITE)
    pygame.draw.rect(screen, Game.colour_1, header_rect)
    back_button.draw(screen)

    title_surface = Game.fonts[0].render("Available Properties", True, BLACK)
    screen.blit(title_surface, (50, 20))

    money_surface = Game.fonts[2].render(f"Money: ${Game.player.money}", True, BLACK)
    screen.blit(money_surface, (800 - 200, 20))

    card_width = 210
    card_height = 220
    margin = 20
    properties_per_row = 3

    buttons = []

    for i, property in enumerate(Game.properties):
        row = i // properties_per_row
        col = i % properties_per_row
        x = 50 + col * (card_width + margin)
        y = 100 + row * (card_height + margin)
        card_rect, buy_button, mortgage_button = draw_property_card(x, y, card_width, card_height, property)
        buttons.append((buy_button, mortgage_button, property))

    return buttons

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
    if Game.player.age<=18:
        join_club_button.draw(screen,Game.colour_1,Game.colour_2)
        screen.blit(Game.fonts[1].render("Join a Club", True, BLACK), (550, 215))
        study_harder_button.draw(screen,Game.colour_1,Game.colour_2)
        screen.blit(Game.fonts[1].render("Study Harder", True, BLACK), (550, 315))
        bunk_class_button.draw(screen,Game.colour_1,Game.colour_2)
        screen.blit(Game.fonts[1].render("Bunk Class", True, BLACK), (550, 415))

    if Game.player.age>18:
        screen.blit(Game.fonts[0].render("Choose Degree", True, BLACK), (50, 230))
        study_harder_button.draw(screen,Game.colour_1,Game.colour_2)
        screen.blit(Game.fonts[1].render("Study Harder", True, BLACK), (550, 315))
        bunk_class_button.draw(screen,Game.colour_1,Game.colour_2)
        screen.blit(Game.fonts[1].render("Bunk Class", True, BLACK), (550, 415))
    if show_degrees is not None:

        for i, degree in enumerate(Game.player.school.degrees):
            pygame.draw.rect(screen, Game.colour_1, degree,border_radius=8)
            screen.blit(Game.fonts[0].render(f"{degree[i]}", True, BLACK), (  10,  10))
            

    if show_clubs is not None:
        display_clubs()
        
  


def display_clubs(): 
    i=0
    for club in club_buttons:
        pygame.draw.rect(screen, Game.colour_1, club,border_radius=8)
        screen.blit(Game.fonts[0].render(f"{Game.player.school.clubs[i]}", True, BLACK), (club.x + 10, club.y + 10))
        join_button = Text_Button(club.x+ 250 , club.y+8,45, 25)
        join_button.draw(screen,Game.colour_2,Game.colour_3)
        screen.blit((Game.fonts[2].render("Join", True, BLACK)), (club.x + 260, club.y  + 15))
        i+=1
# Game loop
current_screen = "start up"
running = True
while running:
    screen.fill(WHITE)

    if current_screen == "main":
        Game.history = check_history(Game.history)
        draw_main_screen()
    elif current_screen == "relationships":
        draw_relationships_screen()
    elif current_screen == "properties":
        sell_buttons = draw_properties_screen()
    elif current_screen == 'work':
        draw_work_screen()
    elif current_screen == "potential relationships":
        draw_potential_relationships_screen()
    elif current_screen == "potential properties":
        buttons = draw_potential_properties_screen()
    elif current_screen == 'potential jobs':
        draw_potential_jobs_screen()
    elif current_screen == "school":
        draw_school_screen()
    elif current_screen == "start up":
        draw_start_up_screen()
    elif current_screen == "settings":
        draw_settings_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if current_screen == "main":
                if age_up_button.rect.collidepoint(mouse_pos):
                    Game.random_yearly_actions()
                    Game.history.append('')
                    Game.player.age += 1
                    Game.history.append(f"Age {Game.player.age - 1}: {choices[0]}")
                    Game.history.append('')
                    make_choice = True
                    choices = show_choices_and_option(check_available_choices(Game.player))
                elif choice_1.rect.collidepoint(mouse_pos) and make_choice:
                    Game.player.choice_results('a', choices)
                    make_choice = False
                elif choice_2.rect.collidepoint(mouse_pos) and make_choice:
                    Game.player.choice_results('b', choices)
                    make_choice = False
                elif choice_3.rect.collidepoint(mouse_pos) and make_choice:
                    Game.player.choice_results('c', choices)
                    make_choice = False
                elif property_button.rect.collidepoint(mouse_pos):
                    current_screen = "properties"
                elif relationships_button.rect.collidepoint(mouse_pos):
                    current_screen = "relationships"
                elif school_button.rect.collidepoint(mouse_pos) and Game.player.age<21:
                    current_screen = "school"
                elif settings_rect.collidepoint(mouse_pos):
                    current_screen = "settings"
                elif work_button.rect.collidepoint(mouse_pos) and Game.player.age>18:
                    if Game.player.job is not None:
                        current_screen = "work"
                    else:
                        current_screen = 'potential jobs'


            elif current_screen == 'start up':
                if new_game_button.rect.collidepoint(mouse_pos):
                    current_screen = "main"
                if quit_button.rect.collidepoint(mouse_pos):
                    running = False
                if options_button.rect.collidepoint(mouse_pos):
                    current_screen = "settings"

            elif current_screen == 'properties':
                if back_button.rect.collidepoint(mouse_pos):
                    current_screen = "main"
                elif find_button.collidepoint(mouse_pos):
                    current_screen = "potential properties"
                for sell_button, property in sell_buttons:
                    if sell_button.rect.collidepoint(mouse_pos):
                        Game.history.append(property.sell(Game.player))
                        current_screen = "main"

            elif current_screen == 'potential properties':
                if back_button.rect.collidepoint(mouse_pos):
                    current_screen = "properties"
                for buy_button, mortgage_button, property in buttons:
                    if buy_button.rect.collidepoint(mouse_pos):
                        Game.history.append(property.buy(Game.player, False))
                        current_screen = "main"
                    elif mortgage_button.rect.collidepoint(mouse_pos):
                        Game.history.append(property.buy(Game.player, True))
                        current_screen = "main"

            elif current_screen == "relationships":
                if back_button.rect.collidepoint(mouse_pos):
                    current_screen = "main"
                for i, btn in enumerate(relationship_buttons):
                    if btn.collidepoint(mouse_pos):
                        selected_relationship = Game.player.relationships[i]
                        break
                if selected_relationship is not None:
                    if ask_for_money_button.rect.collidepoint(mouse_pos):
                        response = selected_relationship.ask_for_money(Game.player)
                        Game.history.append(response)
                        Game.history.append('')
                        current_screen = "main"
                    if conversate_button.rect.collidepoint(mouse_pos):
                        response = selected_relationship.have_conversation(Game.player)
                        Game.history.append(response)
                        Game.history.append('')
                        current_screen = "main"
                    if start_fight_button.rect.collidepoint(mouse_pos) and selected_relationship.relationship_type == 'Sibling':
                        Game.history.append(selected_relationship.start_fight(Game.player))
                        Game.history.append('')
                        current_screen = "main"
                    elif stop_being_friends.rect.collidepoint(mouse_pos) and selected_relationship.relationship_type == 'Friend':
                        Game.history.append(selected_relationship.end_friendship(Game.player))
                        Game.history.append('')
                        current_screen = "main"
                    elif break_up_button.rect.collidepoint(mouse_pos) and selected_relationship.relationship_type == 'Significant Other':
                        Game.history.append(selected_relationship.break_up(Game.player))
                        Game.history.append('')
                        current_screen = "main"
                if make_new_relationships_button.rect.collidepoint(mouse_pos):
                    current_screen = "potential relationships"
            elif current_screen =='school':
                if back_button.rect.collidepoint(mouse_pos):
                    current_screen = "main"
                if join_club_button.rect.collidepoint(mouse_pos):
                    show_clubs = True
                for i,btn in enumerate(club_buttons):
                    if btn.collidepoint(mouse_pos):
                        selected_club = Game.player.school.clubs[i]
                        break
                if selected_club is not None:
                    Game.player.school.join_club(Game.player,selected_club)
                    current_screen = "main"
                    show_clubs = None
                    selected_club = None
                if bunk_class_button.rect.collidepoint(mouse_pos):
                    Game.player.school.bunk_class(Game.player)
                    current_screen = "main"
                if study_harder_button.rect.collidepoint(mouse_pos):
                    Game.player.school.study(Game.player)
                    current_screen = "main"

            elif current_screen == "settings":
                if back_button.rect.collidepoint(mouse_pos):
                    current_screen = "main"
                if reverse_year_button.rect.collidepoint(mouse_pos):
                    Game.go_back_year()
                    current_screen = 'main'
                if change_colour_1_button.rect.collidepoint(mouse_pos):
                    selected_colour_scheme = 1
                if change_colour_2_button.rect.collidepoint(mouse_pos):
                    selected_colour_scheme = 2
                if change_colour_3_button.rect.collidepoint(mouse_pos):
                    selected_colour_scheme = 3
                for colour_button in colour_buttons:
                    if colour_button.rect.collidepoint(mouse_pos):
                        if selected_colour_scheme == 1:
                            Game.Change_Colour_Style_1(colour_button.color)
                        elif selected_colour_scheme == 2:
                            Game.Change_Colour_Style_2(colour_button.color)
                        elif selected_colour_scheme == 3:
                            Game.Change_Colour_Style_3(colour_button.color)
                if start_new_game_button.rect.collidepoint(mouse_pos):
                    Game = game()

            elif current_screen == "potential relationships":
                if back_button.rect.collidepoint(mouse_pos):
                    current_screen = "relationships"
                for i, btn in enumerate(npc_buttons):
                    if btn.collidepoint(mouse_pos):
                        selected_npc = Game.npcs[i]
                        break
                if selected_npc is not None:
                    if ask_to_date_button.rect.collidepoint(mouse_pos):
                        Game.history.append(selected_npc.to_date(Game.player))
                        Game.history.append('')
                        current_screen = "main"
                    if ask_to_be_friends_button.rect.collidepoint(mouse_pos):
                        Game.history.append(selected_npc.be_friends(Game.player))
                        Game.history.append('')
                        current_screen = "main"


            elif current_screen == 'potential jobs':
                if back_button.rect.collidepoint(mouse_pos):
                    if Game.player.job is None:
                        current_screen = "main"
                    else:
                        current_screen = "work"

                for i,btn in enumerate(potential_jobs):
                    if btn.collidepoint(mouse_pos):
                        selected_job = Game.jobs[i]
                        break
                    if selected_job is not None:
                        if apply_for_job_button.rect.collidepoint(mouse_pos):
                            Game.history.append(selected_job.apply_for_job(Game.player))
                            Game.history.append('')
                            current_screen = "main"

                    
            elif current_screen == 'work':
                if back_button.rect.collidepoint(mouse_pos):
                    current_screen = "main"
                if quit_job_button.rect.collidepoint(mouse_pos):
                    Game.history.append(Game.player.job.quit_job(Game.player))
                    Game.history.append('')
                    current_screen = 'main'
                if work_harder_button.rect.collidepoint(mouse_pos):
                    pass
                if ask_for_promotion_button.rect.collidepoint(mouse_pos):
                    Game.history.append(Game.player.job.promote(Game.player))
                if find_job_button.rect.collidepoint(mouse_pos):
                    current_screen = 'potential jobs'
    pygame.display.flip()

pygame.quit()
