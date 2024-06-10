import numpy as np
import pandas as pd
from pygamevisualizer import MapVisualizer

COST_CSV_PATH = 'data/2pix tile europe clean.csv'
TILE_SIZE = 2
MAP_IMG_PATH = 'data/europe_clean.png'
start = (109, 80)

def turntobooleans(value):
    if value > 50:
        return 0
    else:
        return 1

if __name__ == '__main__':
    fuel_cost_csv = pd.read_csv(COST_CSV_PATH)
    reachable_tiles_pd = fuel_cost_csv.applymap(turntobooleans)

    reachable_tiles=reachable_tiles_pd.to_numpy()
    reachable_tiles = reachable_tiles[:, 1:]

    # Visualize the results
    visualizer = MapVisualizer(reachable_tiles, MAP_IMG_PATH, TILE_SIZE, start)
    visualizer.draw_map()
    visualizer.run()


