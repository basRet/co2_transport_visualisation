import matplotlib.pyplot as plt

class MapVisualizer:
    def __init__(self, cost_grid):
        self.cost_grid = cost_grid

    def visualize(self, output_path):
        plt.imshow(self.cost_grid, cmap='coolwarm', interpolation='nearest')
        plt.colorbar(label='Travel Cost')
        plt.title('Travel Cost Map')
        plt.savefig(output_path)
        plt.show()