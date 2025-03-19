class Button():
    def __init__(self,image,x,y,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, surface):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
      
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Colour_Button:
    def __init__(self, x, y, width, height,color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.x = x
        self.y = y
        self.hover_color =  hover_color

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect,border_radius=8)
        else:
            pygame.draw.rect(screen, self.color, self.rect,border_radius=8)
    

class Text_Button:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = None
        self.x = x
        self.y = y
        self.hover_color =  None

    def draw(self, screen,color, hover_color):
        self.color = color
        self.hover_color = hover_color
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect,border_radius=8)
        else:
            pygame.draw.rect(screen, self.color, self.rect,border_radius=8)

      #......................................
      pink_button = Colour_Button (50, 80, 30,30, (255, 209, 220), (255, 209, 220))
blue_button = Colour_Button (50, 120, 30,30, (174, 198, 207) ,(174, 198, 207) )
green_button = Colour_Button (50, 160, 30,30, (189, 222, 192) , (189, 222, 192))
yellow_button = Colour_Button (50, 200, 30,30, (255, 255, 153), (255, 255, 153))
purple_button = Colour_Button (50, 240, 30,30, (207, 186, 240) , (207, 186, 240) )
orange_button = Colour_Button (100, 80, 30,30, (255, 179, 128), (255, 179, 128))
mint_button = Colour_Button (100, 120, 30,30,(170, 240, 209) , (170, 240, 209) )
peach_button = Colour_Button (100, 160, 30,30, (255, 218, 185), (255, 218, 185))
lavender_button = Colour_Button (100, 200, 30,30, (220, 208, 255), (220, 208, 255))
coral_button = Colour_Button (100, 240, 30,30, (255, 188, 178), (255, 188, 178))
lilac_button = Colour_Button (150, 80, 30,30, (200, 162, 200) , (200, 162, 200) )
rose_button = Colour_Button (150, 120, 30,30, (255, 192, 203), (255, 192, 203))
teal_button = Colour_Button (150, 160, 30,30, (130, 203, 184), (130, 203, 184))
salmon_button = Colour_Button (150, 200, 30,30, (255, 155, 170), (255, 155, 170))
mauve_button = Colour_Button (150, 240, 30,30, (224, 176, 255) , (224, 176, 255) )
aqua_button = Colour_Button (200, 80, 30,30, (183, 236, 240) , (183, 236, 240))
buttercup_button = Colour_Button (200, 120, 30,30, (255, 253, 182)  , (255, 253, 182) )
lime_button = Colour_Button (200, 160, 30,30, (216,243,161), (216,243,161))
apricot_button = Colour_Button (200, 200, 30,30, (253,217,181), (253,217,181))
periwrinkle_button = Colour_Button (200, 240, 30,30, (197,208,230), (197,208,230))
colour_buttons =[
                pink_button, blue_button, green_button, yellow_button, purple_button, orange_button,
                mint_button, peach_button, lavender_button, coral_button, lilac_button, rose_button,
                teal_button, salmon_button, mauve_button, aqua_button, buttercup_button, lime_button,
                apricot_button, periwrinkle_button
   ]

choice_1 = Text_Button(420, 310, 360, 40)
choice_2 = Text_Button(420, 360, 360, 40)
choice_3 = Text_Button(420, 410, 360, 40)

reverse_year_button = Text_Button(500, 100, 180, 50)
start_new_game_button = Text_Button(450, 180, 180, 50)
sound_effects_button = Text_Button(550, 250, 160, 50)
save_game = Text_Button(500, 320, 180, 50)
colour_blind_button = Text_Button(550, 390, 180, 50)
load_game_button = Text_Button(450, 450, 200, 50)
change_colour_1_button = Text_Button(50, 300, 200, 50)
change_colour_2_button = Text_Button(50, 400, 200, 50)
change_colour_3_button = Text_Button(50, 500, 200, 50)

ask_to_be_friends_button = Text_Button(500, 400, 200, 50)
ask_to_date_button = Text_Button(500, 300, 200, 50)

conversate_button = Text_Button(500, 400, 200, 50)
stop_being_friends = Text_Button(500, 500, 200, 50)
break_up_button = Text_Button(500, 500, 200, 50)
make_new_relationships_button = Text_Button(500, 200, 200, 50)
start_fight_button = Text_Button(500, 500, 200, 50)
ask_for_money_button = Text_Button(500, 300, 200, 50)


apply_for_job_button = Text_Button(500,450,200,50)

join_club_button = Text_Button(500, 200, 200, 50)
study_harder_button = Text_Button(500, 300, 200, 50)
bunk_class_button = Text_Button(500, 400, 200, 50)
work_harder_button = Text_Button(500, 200, 200, 50)
ask_for_promotion_button = Text_Button(500, 300, 200, 50)
quit_job_button = Text_Button(500, 400, 200, 50)
find_job_button = Text_Button(570, 100, 170, 50)
