from PIL import Image
import numpy as np

class CostGridCreator:
    def __init__(self, tile_size, sea_cost, land_cost):
        self.tile_size = tile_size
        self.sea_cost = sea_cost
        self.land_cost = land_cost

    def load_image(self, image_path):
        image = Image.open(image_path)
        image = image.convert('RGB')
        return np.array(image)

    def create_cost_grid(self, image_array):
        rows, cols, _ = image_array.shape
        grid_rows = rows // self.tile_size
        grid_cols = cols // self.tile_size

        cost_grid = np.zeros((grid_rows, grid_cols))

        for i in range(grid_rows):
            for j in range(grid_cols):
                tile = image_array[i * self.tile_size:(i + 1) * self.tile_size,
                       j * self.tile_size:(j + 1) * self.tile_size]
                avg_color = tile.mean(axis=(0, 1))
                if np.allclose(avg_color, [255, 255, 255]):  # White (Land)
                    cost_grid[i, j] = self.land_cost
                elif np.allclose(avg_color, [0, 0, 255]):  # Blue (Sea)
                    cost_grid[i, j] = self.sea_cost
                else:
                    if avg_color[2] > avg_color[0] and avg_color[2] > avg_color[1]:
                        cost_grid[i, j] = self.sea_cost  # Predominantly blue
                    else:
                        cost_grid[i, j] = self.land_cost  # Predominantly white

        return cost_grid
