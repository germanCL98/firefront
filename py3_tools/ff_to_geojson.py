import click
from forefirepy.ff2geojson import ffjson2geojson

# TODO tienes que coger la ruta absoluta del ffgeojson generado cuando tiras 
# forefire -i result.ff (o como se llame el output generado por make test (vease 
# makefile)). Para que tire el forefire -i tienes que estar en el directorio (te tienes 
# que ir al directorio examples/custom)

# en el makefile tienes que poner en lat lon la coordenada que quieres que se inicie el incendio.
ffjson2geojson("/mnt/c/Users/Cristobal/Documents/biodiversidad/firefront/examples/custom/0-2024-02-10T04-44-00Z.ffgeojson")