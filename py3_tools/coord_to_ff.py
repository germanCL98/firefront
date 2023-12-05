import click
from datetime import datetime

from forefirepy.ForeFire import *


@click.command()
@click.option("--lat", default=41.6, help="latitude of fire start")
@click.option("--lon", default=9.2, help="longitude of fire start")
@click.option("--crsin", default=4326, help="Input EPSG Code")
@click.option("--crsout", default=32632, help="Output EPSG Code")
@click.argument("fueltable", type=click.Path(exists=True))
@click.argument("landscape", type=click.Path(exists=True))
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

    timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%SZ")
    ff.loadData(nc=landscape, isoDate=timestamp)

    # json antes del incendio
    # ff.printOutput()

    ff.startFire(lon=x, lat=y)
    # valor por defecto
    ff.step(dt=12000)

    # json despues del incendio
    ff.printOutput()

    ff.saveFf(output_file)

    output_path = "/".join(output_file.split("/")[:-1])
    filename = output_file.split("/")[-1]
    os.system(f"cd {output_path}; forefire -i {filename}")

    # TODO convertir el fichero ffgeojson a geojson una vez terminada la simulacion

    # ff.convert_to_geojson(output_path + "0-2009-07-24T14-57-39Z.ffgeojson")
    # ff.convert_to_geojson(f"{output_path}/0-{timestamp}.ffgeojson")


if __name__ == "__main__":
    main()
