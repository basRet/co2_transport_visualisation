import numpy as np
import pygame
from PIL import Image
import sys

OUTPUT_PATH_FINAL_FILE = 'created_images/final_image.png'

class MapVisualizer:
    '''
        this visualises an array of 0's or 1's in tile space
    '''
    def __init__(self, reachable_tiles_map, map_image_path, tile_size, start, final_image_overlay_name):
        pygame.init()
        self.final_image_overlay_name = final_image_overlay_name
        self.fuel_cost_map = reachable_tiles_map
        self.tile_size = tile_size
        self.map_img_width, self.map_img_height = Image.open(map_image_path).size
        self.map_image_path = map_image_path
        self.screen = pygame.display.set_mode((self.map_img_width, self.map_img_height))
        self.tile_map_width = int(self.map_img_width / self.tile_size)
        self.tile_map_height = int(self.map_img_height / self.tile_size)
        pygame.display.set_caption("Fuel Cost Map Visualization")
        self.start_coords = start
        self.alpha_surface = pygame.Surface(self.screen.get_size())
        self.alpha_surface.set_alpha(100)
        map_image = pygame.image.load(self.map_image_path)
        imagerect = map_image.get_rect()
        # self.alpha_surface.blit(map_image, imagerect)

    def draw_map(self):
        # Create a surface with a whole-canvas alpha for rectangles
        map_image = pygame.image.load(self.map_image_path)
        imagerect = map_image.get_rect()
        self.screen.blit(map_image, imagerect)

        # Draw the reachable tiles
        for i in range(self.tile_map_height):
            for j in range(self.tile_map_width):
                if self.fuel_cost_map[i][j] == 1:
                    rect = pygame.Rect(j * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size)
                    pygame.draw.rect(self.alpha_surface, (255, 0, 0), rect, 0)

        # draw start tile
        # pygame.draw.circle(self.alpha_surface, (0, 255, 0),
        #                    (self.start_coords[1] * self.tile_size + self.tile_size // 2,
        #                     self.start_coords[0] * self.tile_size + self.tile_size // 2), 5)


        self.screen.blit(self.alpha_surface, (0, 0), special_flags=pygame.BLEND_ALPHA_SDL2)

        pygame.display.flip()
        pygame.image.save(self.alpha_surface, f'{self.final_image_overlay_name}')
        pygame.image.save(self.screen, f'{OUTPUT_PATH_FINAL_FILE}')

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False
                        self.close()
            if running:
                self.draw_map()
                pygame.display.update()

    def close(self):
        pygame.quit()

