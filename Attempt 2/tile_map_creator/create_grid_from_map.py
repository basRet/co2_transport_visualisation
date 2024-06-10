from cost_grid_creator import CostGridCreator
from tile_map_visualizer import MapVisualizer
import pandas as pd

def do_europe():
    image_path = '../data/europe_clean.png'  # Replace with the path to your image
    tile_size = 2  # each tile is this many pixels
    distance_per_pixel = 5.13  # distance of one pixel on the map in kilometers, change this according to map used
    sea_cost_per_tonne_km = 0.02  # cost is 0.02 CO2eq per tonne-kilometer, according to ourworldindata.org
    land_cost_per_tonne_km = 0.4  # cost is 0.4 CO2eq per tonne-kilometer, according to ourworldindata.org
    sea_cost_per_tonne_per_tile = sea_cost_per_tonne_km * tile_size * distance_per_pixel
    land_cost_per_tonne_per_tile = land_cost_per_tonne_km * tile_size * distance_per_pixel

    output_path_img = f'../data/{tile_size}pix tile europe clean.png'  # Replace with desired output path
    output_path_csv = f'../data/{tile_size}pix tile europe clean.csv'

    # Create the cost grid, costs are in CO2eq per tonne per tile
    cost_grid_creator = CostGridCreator(tile_size, sea_cost_per_tonne_per_tile, land_cost_per_tonne_per_tile)
    image_array = cost_grid_creator.load_image(image_path)
    cost_grid = cost_grid_creator.create_cost_grid(image_array)
    pd.DataFrame(cost_grid).to_csv(output_path_csv)

    # Visualize the cost grid
    visualizer = MapVisualizer(cost_grid)
    visualizer.visualize(output_path_img)

def do_world():
    image_path = '../data/world double 4x smaller.png'  # Replace with the path to your image
    tile_size = 2  # each tile is this many pixels
    distance_per_pixel = 9.37*4  # distance of one pixel on the map in kilometers, change this according to map used
    sea_cost_per_tonne_km = 0.02  # cost is 0.02 CO2eq per tonne-kilometer, according to ourworldindata.org
    land_cost_per_tonne_km = 0.4  # cost is 0.4 CO2eq per tonne-kilometer, according to ourworldindata.org
    sea_cost_per_tonne_per_tile = sea_cost_per_tonne_km * tile_size * distance_per_pixel
    land_cost_per_tonne_per_tile = land_cost_per_tonne_km * tile_size * distance_per_pixel

    output_path_img = f'../data/{tile_size}pix tile world 4x smaller.png'  # Replace with desired output path
    output_path_csv = f'../data/{tile_size}pix tile world 4x smaller.csv'

    # Create the cost grid, costs are in CO2eq per tonne per tile
    cost_grid_creator = CostGridCreator(tile_size, sea_cost_per_tonne_per_tile, land_cost_per_tonne_per_tile)
    image_array = cost_grid_creator.load_image(image_path)
    cost_grid = cost_grid_creator.create_cost_grid(image_array)
    pd.DataFrame(cost_grid).to_csv(output_path_csv)

    # Visualize the cost grid
    visualizer = MapVisualizer(cost_grid)
    visualizer.visualize(output_path_img)

if __name__ == '__main__':
    # Configuration for europe
    do_world()
    print("finished")