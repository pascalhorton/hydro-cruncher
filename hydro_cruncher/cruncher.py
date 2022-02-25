import sys
from pathlib import Path
import numpy as np
import geopandas as gpd


class Cruncher:
    def __init__(self):
        self.dem_file_path = None
        self.area_file_path = None
        self.working_dir = None
        self.output_dir = None
        self.output_model = None

    def set_dem_file_path(self, path):
        self.dem_file_path = path

    def set_area_file_path(self, path):
        self.area_file_path = path

    def set_working_dir(self, path):
        self.working_dir = path

    def set_output_dir(self, path):
        self.output_dir = path

    def set_output_model(self, path):
        self.output_model = path

    def process(self):
        print('Processing data...')


