import sys
import argparse
from hydro_cruncher import cruncher
from pathlib import Path


def check_arguments(args):
    if not args.output_dir:
        print(f'The output directory was not provided.')
        sys.exit(1)
    if not args.output_model:
        print(f'The desired hydrological model was not provided.')
        sys.exit(1)


def check_paths_exist(args):
    dem_file_path = Path(args.dem_file_path)
    if not dem_file_path.exists():
        print(f'The DEM file was not found.')
        sys.exit(1)
    if not dem_file_path.is_file():
        print(f'The provided DEM path is not a file.')
        sys.exit(1)

    area_file_path = Path(args.area_file_path)
    if area_file_path.exists():
        if not area_file_path.is_file():
            print(f'The provided path for the delineation of the study area is not a file.')
            sys.exit(1)

    path_working_dir = Path(args.working_dir)
    if not path_working_dir.exists():
        path_working_dir.mkdir(parents=True, exist_ok=True)

    path_output = Path(args.output_dir)
    if not path_output.exists():
        path_output.mkdir(parents=True, exist_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description='Preprocess data for hydrological models.')
    parser.add_argument('dem_file_path', type=str,
                        help='path to the DEM file.')
    parser.add_argument('area_file_path', type=str,
                        help='path to a file approximately delineating the region of interest.')
    parser.add_argument('--working-dir', type=str, required=True, metavar='DIR',
                        help='working directory to store intermediate outputs.')
    parser.add_argument('--output-dir', type=str, required=True, metavar='DIR',
                        help='output directory to save the results.')
    parser.add_argument('--output-model', type=str, required=True,
                        help='hydrological model to produce the files for.')

    args = parser.parse_args()

    check_arguments(args)
    check_paths_exist(args)

    crunch = cruncher.Cruncher()

    crunch.set_dem_file_path(args.dem_file_path)
    crunch.set_area_file_path(args.area_file_path)
    crunch.set_working_dir(args.working_dir)
    crunch.set_output_dir(args.output_dir)
    crunch.set_output_model(args.output_model)

    crunch.process()


if __name__ == "__main__":
    main()
