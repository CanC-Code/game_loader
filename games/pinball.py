import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pinball Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font for text
font = pygame.font.Font(None, 48)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Clear the screen
    screen.fill(BLACK)

    # Display a placeholder message
    text = font.render("Pinball Game - Work in Progress", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.fill(BLACK)
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
