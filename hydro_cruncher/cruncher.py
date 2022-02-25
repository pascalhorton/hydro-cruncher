import sys
from pathlib import Path
from pysheds.grid import Grid
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt


class Cruncher:
    def __init__(self):
        self.dem_file_path = None
        self.area_file_path = None
        self.catchments_file_path = None
        self.working_dir = None
        self.output_dir = None
        self.output_model = None
        self.dem = None
        self.dem_data = None
        self.flow_acc = None

    def set_dem_file_path(self, path):
        self.dem_file_path = Path(path)

    def set_area_file_path(self, path):
        self.area_file_path = Path(path)

    def set_catchments_file_path(self, path):
        self.catchments_file_path = Path(path)

    def set_working_dir(self, path):
        self.working_dir = Path(path)

    def set_output_dir(self, path):
        self.output_dir = Path(path)

    def set_output_model(self, path):
        self.output_model = Path(path)

    def process(self):
        print('Processing data...')
        self.load_dem()
        self.compute_flow_accumulation()

    def load_dem(self):
        # Read file
        if self.dem_file_path.suffix in ['.asc', '.txt']:
            self.dem = Grid.from_ascii(self.dem_file_path)
            self.dem_data = self.dem.read_ascii(self.dem_file_path)
        elif self.dem_file_path.suffix in ['.tif', '.tiff']:
            self.dem = Grid.from_raster(self.dem_file_path)
            self.dem_data = self.dem.read_raster(self.dem_file_path)
        else:
            raise 'DEM file format not supported.'

    def compute_flow_accumulation(self):
        # Fill pits in DEM
        pit_filled_dem = self.dem.fill_pits(self.dem_data)

        # Fill depressions in DEM
        flooded_dem = self.dem.fill_depressions(pit_filled_dem)

        # Resolve flats in DEM
        inflated_dem = self.dem.resolve_flats(flooded_dem)

        # Compute D8 flow directions from DEM
        dirmap = (64, 128, 1, 2, 4, 8, 16, 32)
        flow_dir = self.dem.flowdir(inflated_dem, dirmap=dirmap)

        # Compute flow accumulation
        self.flow_acc = self.dem.accumulation(flow_dir, dirmap=dirmap)

    def plot_dem(self):

        fig, ax = plt.subplots(figsize=(8, 6))
        fig.patch.set_alpha(0)

        plt.imshow(self.dem_data, extent=self.dem.extent, cmap='terrain', zorder=1)
        plt.colorbar(label='Elevation (m)')
        plt.grid(zorder=0)
        plt.title('Digital elevation map', size=14)
        plt.tight_layout()
