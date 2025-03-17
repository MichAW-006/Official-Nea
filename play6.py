import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Settings")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
PURPLE = (140, 70, 255)
LIGHT_PURPLE = (160, 90, 255)

# Color schemes
color_schemes = [
    [(128, 0, 128), (0, 0, 255), (0, 200, 0), (255, 0, 0)],  # Scheme 1
    [(255, 105, 180), (255, 165, 0), (173, 255, 47), (255, 255, 0)],  # Scheme 2
    [(255, 20, 147), (255, 140, 0), (0, 200, 200), (255, 215, 0)],  # Scheme 3
]

# Define fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

# Define button class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, oval=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.oval = oval

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color

        if self.oval:
            pygame.draw.ellipse(screen, current_color, self.rect)
        else:
            pygame.draw.rect(screen, current_color, self.rect)

        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

# Create UI elements
back_button = Button(10, 10, 60, 30, "back", WHITE, LIGHT_PURPLE, oval=True)
buttons = [
    Button(500, 100, 180, 50, "go back a year", PURPLE, LIGHT_PURPLE, oval=True),
    Button(450, 170, 180, 50, "text to speech", PURPLE, LIGHT_PURPLE, oval=True),
    Button(550, 220, 160, 50, "new game", PURPLE, LIGHT_PURPLE, oval=True),
    Button(500, 290, 180, 50, "sound effects", PURPLE, LIGHT_PURPLE, oval=True),
    Button(550, 360, 160, 50, "save game", PURPLE, LIGHT_PURPLE, oval=True),
    Button(450, 420, 200, 50, "colour blind filter", PURPLE, LIGHT_PURPLE, oval=True),
    Button(550, 490, 160, 50, "load game", PURPLE, LIGHT_PURPLE, oval=True),
    Button(150, 500, 120, 50, "english", PURPLE, LIGHT_PURPLE, oval=True),
    Button(300, 500, 120, 50, "other", PURPLE, LIGHT_PURPLE, oval=True),
]
#settings_buttons:
    
    
    
    # Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw header bar
    pygame.draw.rect(screen, PURPLE, (0, 0, screen_width, 50))
    settings_text = font.render("settings", True, BLACK)
    screen.blit(settings_text, (screen_width // 2 - settings_text.get_width() // 2, 10))

    # Draw back button
    back_button.draw(screen)

    # Draw color scheme labels
    labels = ["colour scheme 1", "colour scheme 2", "colour scheme 3"]
    for i, label in enumerate(labels):
        text_surface = font.render(label, True, BLACK)
        screen.blit(text_surface, (50, 80 + i * 100))

    # Draw color scheme swatches
    for i, scheme in enumerate(color_schemes):
        for j, color in enumerate(scheme):
            pygame.draw.rect(screen, color, (50 + j * 40, 120 + i * 100, 30, 30))

    # Draw language label
    lang_text = font.render("change languages", True, BLACK)
    screen.blit(lang_text, (50, 460))

    # Draw buttons
    for button in buttons:
        button.draw(screen)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
