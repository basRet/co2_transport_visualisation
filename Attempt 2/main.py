import numpy as np
import pandas as pd
from pathfinding_new import pathfinder as pathfinder
from pygamevisualizer import MapVisualizer
import pygame
import sys
import os

MAP_IMG_PATH = 'data/europe_clean.png'
TEST_MAP = False
TILE_SIZE = 2
COST_CSV_PATH = f'data/{TILE_SIZE}pix tile europe clean.csv'

def center_pygame_window():
    os.environ['SDL_VIDEO_CENTERED'] = '1'

def select_start_parameters(map_image_path, tile_size):
    pygame.init()

    # Center the first window (fuel limit input)
    center_pygame_window()
    screen = pygame.display.set_mode((400, 100))
    pygame.display.set_caption("Enter Fuel Limit (CO2eq in kg per tonne)")
    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(50, 25, 300, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    fuel_limit = '150'
    selecting_fuel = True

    while selecting_fuel:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    selecting_fuel = False
                elif event.key == pygame.K_BACKSPACE:
                    fuel_limit = fuel_limit[:-1]
                else:
                    fuel_limit += event.unicode

        screen.fill((30, 30, 30))
        txt_surface = font.render(fuel_limit, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()

    # Convert fuel_limit to integer
    fuel_limit = int(fuel_limit)

    # Set up the screen for start location selection
    map_image = pygame.image.load(map_image_path)
    map_rect = map_image.get_rect()
    screen = pygame.display.set_mode(map_rect.size, pygame.NOFRAME)
    pygame.display.set_caption("Select Start Location")
    screen.blit(map_image, (0, 0))
    pygame.display.flip()

    # Center the window manually
    window_info = pygame.display.get_window_size()
    screen = pygame.display.set_mode(map_rect.size)  # Reset to normal mode
    screen.blit(map_image, (0, 0))
    pygame.display.flip()

    selecting_location = True
    start_coords = None

    while selecting_location:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                start_coords = (y // tile_size, x // tile_size)
                selecting_location = False

    pygame.quit()
    return fuel_limit, start_coords

def run_application():
    fuel_cost_csv = pd.read_csv(COST_CSV_PATH).to_numpy()
    fuel_cost_csv = fuel_cost_csv[:, 1:]

    while True:
        fuel_limit, start = select_start_parameters(MAP_IMG_PATH, TILE_SIZE)
        final_image_overlay_name = f'created_images/final_image_reachable_area_{fuel_limit}.png'

        # Instantiate Pathfinding and compute reachable tiles
        reachable_tiles = pathfinder(fuel_cost_csv, start, fuel_limit)

        # Visualize the results
        visualizer = MapVisualizer(reachable_tiles, MAP_IMG_PATH, TILE_SIZE, start, final_image_overlay_name)
        visualizer.draw_map()

        running_visualizer = True
        while running_visualizer:
            visualizer.run()
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        print("space detected")
                        running_visualizer = False
                        visualizer.close()
            except pygame.error: #visualizer closed itself because space was pressed
                running_visualizer = False

if __name__ == "__main__":
    if TEST_MAP:
        fuel_cost_csv = np.array([
            [1, 2, 2, 3],
            [2, 2, 1, 3],
            [3, 3, 1, 2],
            [1, 1, 1, 1]
        ])
        fuel_limit = 2  # in CO2eq per tonne of food
        start = (2, 2)

        final_image_overlay_name = f'created_images/final_image_reachable_area_{fuel_limit}.png'
        reachable_tiles = pathfinder(fuel_cost_csv, start, fuel_limit)
        visualizer = MapVisualizer(reachable_tiles, MAP_IMG_PATH, TILE_SIZE, start, final_image_overlay_name)
        visualizer.draw_map()
        visualizer.run()
    else:
        run_application()
