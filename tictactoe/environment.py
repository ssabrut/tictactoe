import pygame
import numpy as np

class Board:
    def __init__(self):
        self.state = np.array([
            ['', '', ''], 
            ['', '', ''], 
            ['', '', '']
        ])

    def __handle_mouse_click(self, event, mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_i = mouse_pos[0] // 240
            clicked_j = mouse_pos[1] // 240
            if self.state[clicked_j][clicked_i] == '':
                self.state[clicked_j][clicked_i] = 'X'

    def __draw_board(self, screen):
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(screen, "black", (i*240, j*240, 240, 240), 5)
                self.__draw_symbol(screen, i, j)

    def __draw_symbol(self, screen, i, j):
        if self.state[j][i] != '':
            font = pygame.font.Font(None, 200)
            text = font.render(self.state[j][i], True, 'black')
            text_rect = text.get_rect(center=(i*240 + 120, j*240 + 120))
            screen.blit(text, text_rect)

    def render(self):
        pygame.init()
        screen = pygame.display.set_mode((720, 720))
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                mouse_pos = pygame.mouse.get_pos()
                self.__handle_mouse_click(event, mouse_pos)

            screen.fill("white")
            self.__draw_board(screen)
            pygame.display.flip()
            clock.tick(60)
        
        pygame.quit()