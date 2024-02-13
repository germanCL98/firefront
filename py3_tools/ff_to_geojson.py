import click
from forefirepy.ff2geojson import ffjson2geojson
import os
import shutil


@click.command()
@click.option("-input_dir", "input_dir", type=click.Path(exists=True))
def main(input_dir):
    # obtiene la ruta de la carpeta donde se van a guardar las simulaciones
    perimeters_dir = os.path.join(input_dir, "perimeters")

    # comprueba si existe la ruta. Si no, la crea
    if not os.path.exists(perimeters_dir):
        print('Carpeta no existe, creando carpeta de simulaciones')
        os.mkdir(perimeters_dir)

    # se itera sobre los elementos. Es posible que una simulacion devuelva mas de un perimetro
    # utilizando print[] dentro de un fichero .ff. Al llamar print[] se guarda un fichero
    # con el estado de la simulacion en el momento en el que se llama la funcion
    for file in os.listdir(input_dir):
        if file.split(".")[-1] == "ffgeojson":
            ff_geojson_path = f"{input_dir}/{file}"
            # ffjson2geojson devuelve la ruta del archivo geojson generado
            geojson_path = ffjson2geojson(ff_geojson_path)

            # se mueve a la carpeta de perimetros y elimina el ffgeojson
            counter = 0
            dest_file = f"{perimeters_dir}/simulation-{counter}_{os.path.basename(geojson_path)}"
            while os.path.exists(dest_file):
                counter += 1
                dest_file = f"{perimeters_dir}/simulation-{counter}_{os.path.basename(geojson_path)}"
            shutil.move(geojson_path, dest_file)
            os.remove(ff_geojson_path)

if __name__ == "__main__":
    main()


# # en el makefile tienes que poner en lat lon la coordenada que quieres que se inicie el incendio.
# ffjson2geojson("/mnt/c/Users/Cristobal/Documents/biodiversidad/firefront/examples/custom/0-2024-02-10T04-44-00Z.ffgeojson")