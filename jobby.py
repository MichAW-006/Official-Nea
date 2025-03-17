import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Life Simulator - Job Screen")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
HOVER_GREEN = (0, 255, 0)
HOVER_BLUE = (0, 0, 255)

# Fonts
title_font = pygame.font.Font(None, 36)
job_font = pygame.font.Font(None, 24)
detail_font = pygame.font.Font(None, 20)
button_font = pygame.font.Font(None, 22)

# Job data (example)
jobs = [
    {"title": "Software Engineer", "workplace": "Tech Corp", "education": "Bachelor's in CS", "salary": "$80,000"},
    {"title": "Teacher", "workplace": "City High School", "education": "Bachelor's in Education", "salary": "$50,000"},
    {"title": "Doctor", "workplace": "City Hospital", "education": "Medical Degree", "salary": "$120,000"},
]

selected_job = jobs[0]  # Default selected job

# Main loop
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(LIGHT_GRAY)

    # Draw title
    title_text = title_font.render("Job Opportunities", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 20))

    # Draw job list
    job_list_title = job_font.render("Available Jobs", True, BLACK)
    screen.blit(job_list_title, (50, 80))
    for i, job in enumerate(jobs):
        job_rect = pygame.Rect(50, 120 + i * 40, 300, 30)
        if job_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, GRAY, job_rect)  # Hover effect
        else:
            pygame.draw.rect(screen, WHITE, job_rect)
        pygame.draw.rect(screen, BLACK, job_rect, 1)  # Border
        job_text = job_font.render(job["title"], True, BLACK)
        screen.blit(job_text, (job_rect.x + 10, job_rect.y + 5))

    # Draw job details panel
    detail_panel = pygame.Rect(400, 80, 350, 400)
    pygame.draw.rect(screen, WHITE, detail_panel)
    pygame.draw.rect(screen, BLACK, detail_panel, 2)  # Border
    detail_title = job_font.render("Job Details", True, BLACK)
    screen.blit(detail_title, (410, 90))
    job_title_text = detail_font.render(f"Title: {selected_job['title']}", True, BLACK)
    workplace_text = detail_font.render(f"Workplace: {selected_job['workplace']}", True, BLACK)
    education_text = detail_font.render(f"Education: {selected_job['education']}", True, BLACK)
    salary_text = detail_font.render(f"Salary: {selected_job['salary']}", True, BLACK)
    screen.blit(job_title_text, (410, 130))
    screen.blit(workplace_text, (410, 160))
    screen.blit(education_text, (410, 190))
    screen.blit(salary_text, (410, 220))

    # Draw apply button
    apply_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 70, 200, 40)
    if apply_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, HOVER_GREEN, apply_button, border_radius=5)  # Hover effect
    else:
        pygame.draw.rect(screen, GREEN, apply_button, border_radius=5)
    pygame.draw.rect(screen, BLACK, apply_button, 2, border_radius=5)  # Border
    apply_text = button_font.render("Apply for Job", True, WHITE)
    screen.blit(apply_text, (apply_button.x + 20, apply_button.y + 10))

    # Draw back button
    back_button = pygame.Rect(20, SCREEN_HEIGHT - 70, 100, 40)
    if back_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, HOVER_BLUE, back_button, border_radius=5)  # Hover effect
    else:
        pygame.draw.rect(screen, BLUE, back_button, border_radius=5)
    pygame.draw.rect(screen, BLACK, back_button, 2, border_radius=5)  # Border
    back_text = button_font.render("Back", True, WHITE)
    screen.blit(back_text, (back_button.x + 25, back_button.y + 10))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
