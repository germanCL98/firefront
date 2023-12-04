import click
from datetime import datetime

from forefirepy.ForeFire import *


@click.command()
@click.option("--lat", default=41.6, help="latitude of fire start")
@click.option("--lon", default=9.2, help="longitude of fire start")
@click.option("--crsin", default=4326, help="Input EPSG Code")
@click.option("--crsout", default=32632, help="Output EPSG Code")
@click.argument("output_file", type=click.Path())
def main(lat, lon, crsin, crsout, output_file):
    [x, y] = reproject(
        [lon, lat],
        inEpsg="epsg:" + crsin,
        outEpsg="epsg:" + crsout,
    )

    ff = Forefire()
    ff.configBasicFf(lon=x, lat=y)
    ff.saveFf(output_file)

    # os.system(f"cd {output_path}; forefire -i {filename}")
    os.system(f"forefire -i {output_file}")

    # ff.convert_to_geojson(output_path + "0-2009-07-24T14-57-39Z.ffgeojson")
    ff.convert_to_geojson("0-2009-07-24T14-57-39Z.ffgeojson")


if __name__ == "__main__":
    main()
