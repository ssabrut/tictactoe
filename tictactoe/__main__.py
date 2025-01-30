import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True

board = np.array([
    ['', '', ''], 
    ['', '', ''], 
    ['', '', '']
])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    # Handle mouse clicks
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        clicked_i = mouse_pos[0] // 240
        clicked_j = mouse_pos[1] // 240
        print(board)
        if board[clicked_j][clicked_i] == '':
            board[clicked_j][clicked_i] = 'X'

    # render board and pieces
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, "black", (i*240, j*240, 240, 240), 5)
            if board[j][i] != '':
                font = pygame.font.Font(None, 200)
                text = font.render(board[j][i], True, 'black')
                text_rect = text.get_rect(center=(i*240 + 120, j*240 + 120))
                screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()