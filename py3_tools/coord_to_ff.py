import click

from forefirepy.ForeFire import *


@click.command()
@click.option("--lat", default=41.6, help="latitude of fire start")
@click.option("--lon", default=9.2, help="longitude of fire start")
@click.option("--crsin", default=4326, help="Input EPSG Code")
@click.option("--crsout", default=32632, help="Output EPSG Code")
@click.option(
    "--fueltable",
    default="./fuels.ff",
    type=click.Path(exists=True),
    help="Fuels table file path",
)
@click.option(
    "--landscape",
    default="./landscape.nc",
    type=click.Path(exists=True),
    help="Landscape file path",
)
@click.argument("output_file", type=click.Path())
def main(lat, lon, crsin, crsout, fueltable, landscape, output_file):
    [x, y] = reproject(
        [lon, lat],
        inEpsg=f"epsg:{crsin}",
        outEpsg=f"epsg:{crsout}",
    )

    ff = Forefire()

    # ff.configBasicFf(lon=x, lat=y)
    ff.setFuels(fuelsTableFile=fueltable)
    ff.setProjection(proj=crsout)
    ff.loadData(nc=landscape)
    ff.startFire(lon=x, lat=y)
    # valor por defecto
    ff.step(dt=12000)

    ff.saveFf(output_file)

    # os.system(f"cd {output_path}; forefire -i {filename}")
    os.system(f"forefire -i {output_file}")

    # ff.convert_to_geojson(output_path + "0-2009-07-24T14-57-39Z.ffgeojson")
    ff.convert_to_geojson("0-2009-07-24T14-57-39Z.ffgeojson")


if __name__ == "__main__":
    main()
